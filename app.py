import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv("movies.csv")   

df = load_data()

st.title("🎬 Movie Recommendation System")
st.markdown("Search for movies and get similar recommendations.")


movie_name = st.text_input("Enter a movie name:")

if movie_name:
    results = df[df['title'].str.contains(movie_name, case=False, na=False)]

    if not results.empty:
        st.subheader("Search Results")
        st.dataframe(results[['title', 'genres', 'vote_average', 'director']].head(10))

        genre = results.iloc[0]['genres'].split()[0] if pd.notna(results.iloc[0]['genres']) else None
        if genre:
            st.subheader(f"Recommended Movies in {genre}")
            recs = df[df['genres'].str.contains(genre, na=False)].sort_values(
                by="vote_average", ascending=False
            ).head(5)
            st.table(recs[['title', 'genres', 'vote_average']])
    else:
        st.warning("No movies found. Try another name.")
