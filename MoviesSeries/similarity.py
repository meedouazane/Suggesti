import pandas as pd
import random
import requests
import json

similarity_df_Movie = pd.read_csv('/home/m311/ML/DL/NLP/suggesti/Movies_similarity.csv', index_col=0)
similarity_df_Series = pd.read_csv('/home/m311/ML/DL/NLP/suggesti/Series_similarity.csv', index_col=0)

def check(name):
  url = "https://api.themoviedb.org/3/search/multi"
  headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NTRkY2FjZGFkOTFjYTJkMGRkYTdjMDlkNDZiNzQyNCIsIm5iZiI6MTcyNjMxMjI4OS4yNzQwNjIsInN1YiI6IjY2ZTU2ZGQ2NmEyYmRkNDAwNGZkNjI3YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Bihu-ZijiItyKPu3FmL80Rn_LQO1foFho3rovkqtCzc"
  }
  params = {
    "query": name
  }
  response = requests.get(url, headers=headers, params=params)
  response = response.json()
  media_type = response['results'][0]['media_type']

  if media_type == 'movie':
    return suggest_Movies(name)
  if media_type == 'tv':
    return suggest_Series(name)

def suggest_Series(name, suggest_number=3):
  name = name.title()
  series = []
  try:
    series = list(similarity_df_Series[name].sort_values(ascending=False).index)
  except TypeError:
    return list(similarity_df_Series[name][:suggest_number].index)
  series = series[:20]
  if name in series:
      series = [x for x in series if x != name]
  series_list = random.sample(series, suggest_number)
  return series_list


def suggest_Movies(name, suggest_number=3):
  name = name.title()
  movies = []
  try:
    movies = list(similarity_df_Movie[name].sort_values(ascending=False).index)
  except TypeError:
    return list(similarity_df_Movie[name].index)[:suggest_number]
  movies = movies[:20]
  if movies in movies:
      series = [x for x in movies if x != name]
  movies_list = random.sample(movies, suggest_number)
  return movies_list
