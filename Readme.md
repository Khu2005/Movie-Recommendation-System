# Movie Recommendation System

## Description
This project recommends movies based on the selected movie. It uses the movie overview to find similar movies.

## Dataset
IMDb Top 1000 Movies Dataset
link - https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows

## Technologies Used
- Python
- Pandas
- NLTK
- Scikit-learn
- Streamlit

## How It Works
Load the movie dataset.
Clean the movie overview text.
Convert the text into TF-IDF vectors.
Calculate cosine similarity.
Show the top 5 similar movies.


## How to Run

### Clone the Repository
git clone https://github.com/Khu2005/Movie-Recommendation-System.git

### Open the Project Folder
cd Movie-Recommendation-System

### Install Required Libraries
pip install -r requirements.txt

### Run the Project
python -m streamlit run app.py


## Git Commands

### Initialize Git
git init

### Add Files
git add .

### Commit Changes
git commit -m "Initial commit"

### Create Main Branch
git branch -M main

### Connect to GitHub
git remote add origin https://github.com/Khu2005/Movie-Recommendation-System.git

### Push to GitHub
git push -u origin main

## Deploy on Render

1. Login to Render.
2. Click New + and select Web Service
3. Connect your GitHub repository.
4. Select Movie-Recommendation-System
5. Enter the following commands.

### Build Command
pip install -r requirements.txt

### Start Command
python -m streamlit run app.py --server.port=$PORT --server.address=0.0.

6. Click Create Web Service.
7. Wait for the deployment to finish.
8. Open the Render URL to use the application.

