import streamlit as st
import pandas as pd
import string
from sklearn.feature_extraction.text import TfidfVectorizer,ENGLISH_STOP_WORDS
from sklearn.metrics.pairwise import cosine_similarity

# Download stopwords
# nltk.download('stopwords')

# Load dataset
df = pd.read_csv("imdb_top_1000.csv")

# Handle missing values
df['Overview'] = df['Overview'].fillna('')

# Stopwords
stop_words = set(ENGLISH_STOP_WORDS)

# Preprocessing Functions
def convert_to_lowercase(text):
    return text.lower()

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def remove_stopwords(text):
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

# Clean text
df['recommendation_clean_text'] = df['Overview'].apply(convert_to_lowercase)
df['recommendation_clean_text'] = df['recommendation_clean_text'].apply(remove_punctuation)
df['recommendation_clean_text'] = df['recommendation_clean_text'].apply(remove_stopwords)

# TF-IDF
tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
tfidf_matrix = tfidf.fit_transform(df['recommendation_clean_text'])

# Cosine Similarity
cosine_sim = cosine_similarity(tfidf_matrix)

# Recommendation Function
def recommend_movies(movie_name, top_n=5):

    movie_index = df[df['Series_Title'] == movie_name].index[0]

    similarity_scores = list(enumerate(cosine_sim[movie_index]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    similarity_scores = similarity_scores[1:top_n+1]

    recommendations = []

    for movie in similarity_scores:
        recommendations.append(df.iloc[movie[0]]['Series_Title'])

    return recommendations


st.title("🎬 Movie Recommendation System")

movie = st.selectbox(
    "Select a Movie",
    sorted(df['Series_Title'].unique())
)

if st.button("Recommend"):

    recommendations = recommend_movies(movie)

    st.subheader("Recommended Movies")

    for i, rec in enumerate(recommendations, start=1):
        st.write(f"{i}. {rec}")