import streamlit as st
import nltk
import sklearn
import pandas as pd
import pickle
import joblib

st.title("Movie Recommendation System")


# Loading movies dataframe
df = pd.read_pickle("movies.pkl")

similarity=joblib.load('similarity.joblib')

st.write("Movies Shape :", df.shape)
st.write("Similarity Shape :", similarity.shape)
st.write("Similarity Type :", type(similarity))
st.write("Movies Columns :", df.columns)

movies_name = df['title'].values

# Recommendation Function
def recommend(movie):

    movie_index = df[df['title']==movie].index[0]

    recommendations = similarity[movie_index]

    movie_list = sorted(list(enumerate(recommendations)),reverse=True,key=lambda x:x[1])[1:6]


    recommended_movies = []


    for i in movie_list:

        recommended_movies.append(df.iloc[i[0]].title)

    return recommended_movies



# Dropdown Menu
name_movies = st.selectbox("Enter the Movie Name",movies_name)


# Button
if st.button("Recommend"):

    try:
        recommendations = recommend(name_movies)

        st.write("### Recommended Movies")

        for movie in recommendations:
            st.write(movie)

    except Exception as e:
        st.error(e)