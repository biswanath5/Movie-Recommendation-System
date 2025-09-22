# 🎬 Movie Recommendation System
## App link: https://movie-recommendation-system-str.streamlit.app/

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-green)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 📌 Overview
This project is a **Movie Recommendation System** built with Python.  
It suggests movies similar to a given movie using **content-based filtering** on metadata such as genres, overview, cast, and crew.

The system is available in two forms:  
- 📒 **Jupyter Notebook** – Step-by-step implementation  
- 🌐 **Streamlit Web App** – Interactive movie search and recommendations  

---

## 📂 Dataset
The project uses a sample **Movies Metadata dataset** (`movies.csv`).

**Columns Used:**
| Column        | Description                          |
|---------------|--------------------------------------|
| `title`       | Movie title                           |
| `genres`      | Movie genres                          |
| `overview`    | Short description                     |
| `cast`        | Main actors                           |
| `crew`        | Directors, writers, producers        |
| `vote_average`| Average rating                        |

**Source:** Movies Metadata dataset (sample included in the repo)

---

## ⚙️ Features
- 🔍 Search for any movie  
- 🎭 Get **top-5 similar movie recommendations**  
- 📊 Visualize dataset insights:
  - Ratings distribution  
  - Top genres  
- 🚀 **Interactive and user-friendly Streamlit web app**

---

## 🛠️ Tech Stack
| Technology      | Purpose                            |
|-----------------|----------------------------------|
| Python          | Data processing and recommendation logic |
| Pandas & NumPy  | Data manipulation                  |
| Scikit-learn    | Content-based similarity computation |
| Streamlit       | Web app interface                  |
| Matplotlib & Seaborn | Visualizations / EDA          |

---

## 🚀 How to Run Locally

### 1️⃣ Clone Repository
```bash
git clone https://github.com/biswanath5/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Run Jupyter Notebook
```bash
jupyter notebook "Movie Recommendation System.ipynb"
```
### 4️⃣ Run Streamlit App
```bash
streamlit run app.py
```

Open the URL shown in your terminal to access the interactive app.

## Screenshots
<img width="947" height="402" alt="image" src="https://github.com/user-attachments/assets/fffaf6b4-8501-42ce-ae08-4ade75032a22" />
