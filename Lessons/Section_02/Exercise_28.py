# create a dictionary
movie = {
  "title": "The Godfather",
  "director": "Francis Ford Coppola",
  "year": 1972,
  "rating": 9.2
}
# access the year
print(movie['year'])
# update the dictionary
movie['rating'] = (movie['rating'] + 9.3)/2
print(movie['rating'])
# create a dictionary from scratch
movie = {}
movie['title'] = "The Godfather"
movie['director'] = "Francis Ford Coppola"
movie['year'] = 1972
movie['rating'] = 9.2
# add a list to a dictionary
movie['actors'] = ['Marlon Brando', 'Al Pacino', 'James Caan']
movie['other_details'] = {
  'runtime': 175,
  'language': 'English'
}
print(movie)
