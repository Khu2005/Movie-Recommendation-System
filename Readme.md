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
└── runtime.txt
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


### 1. Clone the Repository

```bash
git clone https://github.com/Khu2005/Movie-Recommendation-System.git
```

### 2. Navigate to the Project Folder

```bash
cd Movie-Recommendation-System
```

### 3. Install the Required Packages

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m streamlit run app.py
```

The application will start on your local machine. Open the URL displayed in the terminal (usually `http://localhost:8501`) in your web browser.

## Git Commands

### Initialize Git Repository

```bash
git init
```

### Add Files

```bash
git add .
```

### Commit Changes

```bash
git commit -m "Initial commit - Movie Recommendation System"
```

### Create Main Branch

```bash
git branch -M main
```

### Add GitHub Repository

```bash
git remote add origin https://github.com/Khu2005/Movie-Recommendation-System.git
```

### Push the Project

```bash
git push -u origin main
```

## Deployment on Render

1. Create an account on Render and sign in.
2. Click **New +** → **Web Service**.
3. Connect your GitHub account.
4. Select the **Movie-Recommendation-System** repository.
5. Configure the deployment:
   - **Environment:** Python
   - ## Render Deployment Configuration

       ### Build Command

      ```bash
      pip install -r requirements.txt
      ```
      This command installs all the required dependencies before deployment.

      ### Start Command

      ```bash
      python -m streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
     ```
6. Click **Create Web Service**.
7. Wait for the deployment to complete.
8. Open the generated Render URL to use the application.

9.RenderLink :-https://movie-recommendation-system-2-j3zg.onrender.com
## Output
- Select a movie from the dropdown list.
- Click the **Recommend** button.
- The application displays the top 5 similar movie recommendations.

## Author
Khushi Shah