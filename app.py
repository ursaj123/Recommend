# git commit -m "Initial Commit"  # for taking files to staging area
# for recovering file from last commit git checkout filename and -f for all files
# git diff tells the difference within the files after being commited
# git diff --staged tells the differnces within the last commit 
# git rm filename removes and deletes the files permanently
# git rm --cached filenmae removes the files from the staged area but remain at hard disk
# touch .gitignore filename will make a file in which we can write the name of the file which we don't want to push 
# git branch branchname will create a new VM sort of thing so that we can experiment with the project 
# without affecting the actual project.
# we can access brach by git checkout branchname and list all branches by git branch 
# can merge any new branch by git merge branchname so that main branch will change
# git remote add origin https://github.com/ursaj123/Recommender-System.git will add my local repo to
# github.
# can add ssh if we don't have access to the github repo, by following commands given in documentation

import streamlit as st 
import numpy as np
import pandas as pd
import pickle 
import requests

# first assests.get('https://api.themoviedb.org/3/movie/{}?api_key=1764936a71137b0074282bd7b7a64dc1&language=en-US'.format(movie_id))
    data = request.json() # now it will be a dictionary
    # now there is a pinging the title
st.title("Movie Recommender System")

# then gathering all the required resources
movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].values
similarity_matrix = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    request = requoster path attribute in data
    return 'https://image.tmdb.org/t/p/w500' + data['poster_path']
    # so this will be a complete path 
    

def recommend(movie_name, movies, similarity_matrix):
    # remember movies is a dataframe
    index = movies[movies['title']==movie_name].index
    index = index[0]
    # now we have the index number of the movie and we have to determine the top 5 movies of this dataset
    recommended_movies_index = list(np.argsort(similarity_matrix[index]))[::-1][1:6] # to recommend top 6 movies
    recommended_movies = movies['title'][recommended_movies_index]
    recommended_movies_id = movies['id'][recommended_movies_index]
    recommended_movies_poster_paths = [fetch_poster(x) for x in recommended_movies_id]
    # now we have to fetch the posters from TMDB API with the help of movie ID's
    return recommended_movies_poster_paths, list(recommended_movies)


# now first making a drop down list from which user will select
# a movie, then we will recommend movies similar to that movie 
movie = st.selectbox('More movies like this!!', movies_list)

recommended_movies_poster_paths, recommended_movies = recommend(movie, movies, similarity_matrix)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
   st.write(recommended_movies[0])
   st.image(recommended_movies_poster_paths[0])
with col2:
   st.write(recommended_movies[1])
   st.image(recommended_movies_poster_paths[1])
with col3:
   st.write(recommended_movies[2])
   st.image(recommended_movies_poster_paths[2])
with col4:
   st.write(recommended_movies[3])
   st.image(recommended_movies_poster_paths[3])
with col5:
   st.write(recommended_movies[4])
   st.image(recommended_movies_poster_paths[4])

#st.write('You selected:', movie)