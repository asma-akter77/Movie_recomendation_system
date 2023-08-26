import pandas as pd
import streamlit as st
import pickle
import requests


movies_dict = pickle.load(open('model3.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

def recomend(x):
    mov_lst = movies[movies['title']==x].index[0]
    distance = similarity[mov_lst]
    mov_lst = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    rcmd_mov_poster = []
    for i in mov_lst:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch poster from api

        recommended_movies.append (movies.iloc[i[0]].title)
        rcmd_mov_poster.append(fetch_poster(movie_id))
    return recommended_movies,rcmd_mov_poster


def fetch_poster(id):
    responce = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8'.format(id))
    x = responce.json()
    return 'https://image.tmdb.org/t/p/original'+x['poster_path']


st.markdown("<h1 style='text-align: center; color: red;'>Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: red;'>Relate your choice with help of Machine Learning</h5>", unsafe_allow_html=True)

Selected_Movie_Name = st.selectbox(
    'Relate your choice with help of Machine Learning',
  movies['title'].values)

if st.button('--Find Your Next Choice--'):
    name,poster = recomend(Selected_Movie_Name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
       st.text(name[0])
       st.image(poster[0])

    with col2:
       st.text(name[1])
       st.image(poster[1])

    with col3:
       st.text(name[2])
       st.image(poster[2])

    with col4:
       st.text(name[3])
       st.image(poster[3])

    with col5:
       st.text(name[4])
       st.image(poster[4])
        
st.divider()
st.caption(':blue[Asma Akter] :sunglasses:')
st.caption('Data Science Engineer')
