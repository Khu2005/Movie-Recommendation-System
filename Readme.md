# Movie Recommendation System

## Description
This project is a Content-Based Movie Recommendation System developed using Python. It recommends movies based on the similarity of their movie overviews using TF-IDF Vectorization and Cosine Similarity. A Streamlit web application is provided for user interaction.

## Dataset
IMDb Top 1000 Movies Dataset
link - https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows

## Technologies Used
- Python
- Pandas
- NLTK
- Scikit-learn
- Streamlit

## Features
- Load and preprocess movie data.
- Convert movie overviews into TF-IDF vectors.
- Calculate similarity using Cosine Similarity.
- Recommend the top 5 similar movies.
- Interactive web interface using Streamlit.

## Project Structure
```
Movie-Recommendation-System/
│── app.py
│── imdb_top_1000.csv
│── requirements.txt
│── README.md
└── .gitignore
```

## Installation

1. Clone the repository:
```
git clone <repository_link>
```

2. Navigate to the project folder:
```
cd Movie-Recommendation-System
```

3. Install the required packages:
```
pip install -r requirements.txt
```

## How to Run

Run the Streamlit application using:

```
python -m streamlit run app.py
```

After running the command, open the URL displayed in the terminal (usually `http://localhost:8501`) in your web browser.

## Output
- Select a movie from the dropdown list.
- Click the **Recommend** button.
- The application displays the top 5 similar movie recommendations.

## Author
Khushi Shah