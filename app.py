import streamlit as st
import pickle
import requests
import pandas as pd

# Load environment variables


def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=2125dc66c4a8d106b6a49c9bdbe9a1c3&language=en-US'.format(movie_id)
    response = requests.get(url)
    data = response.json()
    

    return "https://image.tmdb.org/t/p/w500/"+ data["poster_path"]



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(
            enumerate(distances)
        ),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_movie_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # Fetch movie poster using movie_id and fetch by tmdb API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movie_posters

similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies  = pd.DataFrame(movies_dict)

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Select a movie ',
    movies['title'].values
)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    col1 , col2 , col3 ,col4 , col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
# if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            # Movie card with border
            st.markdown(
                f"""
                <div style="border:1px solid #ddd; padding:10px; border-radius:5px; text-align:center;">
                    <h4>{names[idx]}</h4>
                    <img src="{posters[idx]}" alt="{names[idx]}" style="width:100%; border-radius:5px;">
                </div>
                """,
                unsafe_allow_html=True
            )