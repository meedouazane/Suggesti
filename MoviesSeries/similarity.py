import pandas as pd
import random
import requests
import json
from django.http import JsonResponse

#precalculated models
similarity_df_Movie = pd.read_csv('/PATH/Movies_similarity.csv', index_col=0)
similarity_df_Series = pd.read_csv('/PATH/Series_similarity.csv', index_col=0)


def check(name):
  """
  checking if input is valid title
  and determine if it's movie or series and pass it to the right
  similarity dataframe
  name: input title from user
  """
  #Using themoviedb API to verify the name
  url = "https://api.themoviedb.org/3/search/multi"
  headers = {
    "accept": "application/json",
    "Authorization": "YOUR KEY FROM themoviedb"
  }
  params = {
    "query": name
  }
  response = requests.get(url, headers=headers, params=params)
  response = response.json()
  # check if input is series or movie
  media_type = response['results'][0]['media_type']

  if media_type == 'movie':
    try:
      seguelist = suggest_Movies(name)
    except Exception as e:
      return JsonResponse({'status': 'error', 'message': f"Error finding suggestions: {str(e)}"}, status=500)
    return seguelist
  if media_type == 'tv':
    try:
      seguelist = suggest_Series(name)
    except Exception as e:
      return JsonResponse({'status': 'error', 'message': f"Error finding suggestions: {str(e)}"}, status=500)
    return seguelist


def suggest_Series(name, suggest_number=3):
  """
  Get most similar Series to inputted series using precalculated model
  name: valid name of series
  suggest_number: number of titles that it will be returned
  """
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
  """
  Get most similar Movies to inputted series using precalculated model
  name: valid name of Movie
  suggest_number: number of titles that it will be returned
  """
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
