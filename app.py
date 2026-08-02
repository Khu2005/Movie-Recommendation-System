import streamlit as st
import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


nltk.download('stopwords')

df = pd.read_csv("imdb_top_1000.csv")

print("Dataset Loaded Successfully")
print(df.head())

df['Overview'] = df['Overview'].fillna('')

stop_words = set(stopwords.words('english'))

def convert_to_lowercase(text):
    return text.lower()

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def remove_stopwords(text):
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

df['clean_text'] = df['Overview'].apply(convert_to_lowercase)
df['clean_text'] = df['clean_text'].apply(remove_punctuation)
df['clean_text'] = df['clean_text'].apply(remove_stopwords)

print("Text Preprocessing Completed")

tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
tfidf_matrix = tfidf.fit_transform(df['clean_text'])

print("TF-IDF Matrix Shape:", tfidf_matrix.shape)

cosine_sim = cosine_similarity(tfidf_matrix)

print("Cosine Similarity Matrix Shape:", cosine_sim.shape)

def recommend(movie):

    if movie not in df['Series_Title'].values:
        return ["Movie not found"]

    movie_index = df[df['Series_Title'] == movie].index[0]

    similarity = list(enumerate(cosine_sim[movie_index]))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    scores = scores[1:6]

    recommended = []

    for i in similarity:
        recommended.append(df.iloc[i[0]].Series_Title)

    return recommended


print("\nTesting Recommendation Function")

print("\nThe Dark Knight")
print(recommend("The Dark Knight"))

print("\nTitanic")
print(recommend("Titanic"))

print("\nAvatar")
print(recommend("Avatar"))



st.title("🎬 Movie Recommendation System")

st.write("Select a movie to get similar movie recommendations.")

selected_movie = st.selectbox(
    "Select Movie",
    sorted(df['Series_Title'].unique())
)

if st.button("Recommend"):

    movies = recommend(selected_movie)

    if movies[0] == "Movie not found":
        st.error("Movie not found in the dataset.")

    else:
        st.subheader("Top 5 Recommended Movies")

        for i in range(len(movies)):
            st.write(f"{i+1}. {movies[i]}")