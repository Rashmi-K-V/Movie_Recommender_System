# 🎬 Movie Recommendation System

A **content-based movie recommendation system** built using Python that suggests similar movies based on textual and metadata similarity. The system leverages **cosine similarity** over processed movie features and provides recommendations through an interactive **Streamlit web application**.

---

## 📌 Project Overview

This project recommends movies similar to a given movie title by analyzing features such as:
- Movie overview
- Genres
- Keywords
- Cast and crew information

The recommendation engine computes similarity scores using **cosine similarity**, returning the most relevant movies based on feature overlap.



## 🚀 Features

- Content-based movie recommendations  
- Uses cosine similarity for ranking movies  
- Interactive web interface built with Streamlit  
- Fast inference using precomputed similarity matrix  
- Simple and explainable recommendation logic  



## 🗂 Dataset

**TMDB 5000 Movies Dataset**

- Source: The Movie Database (TMDB)
- Contains metadata for ~5000 movies
- Key attributes used:
  - `title`
  - `overview`
  - `genres`
  - `keywords`
  - `cast`
  - `crew`

The dataset was preprocessed and transformed into feature vectors for similarity computation.



## 🧠 Recommendation Approach

1. **Data Preprocessing**
   - Extracted relevant features from the dataset
   - Converted text data into numerical form using **Bag of words model**
   - Combined multiple features into a single representation

2. **Similarity Computation**
   - Used **cosine similarity** to measure closeness between movies
   - Generated a similarity matrix for fast lookup

3. **Recommendation Logic**
   - Given a movie title, retrieve its index
   - Rank movies based on similarity score
   - Return top N similar movies (excluding the selected movie)



## 🖥️ Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Streamlit**
- **Pickle**



## ▶️ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/Rashmi-K-V/movie-recommender-system.git
cd movie-recommender-system
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit app
```bash
streamlit run app.py
```



