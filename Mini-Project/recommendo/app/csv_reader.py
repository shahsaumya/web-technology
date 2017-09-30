from app.models import Movies
import csv
reader = csv.reader(open("/home/saumya/Desktop/WT/Mini-Project/ml-latest-small/combined.csv"))

for row in reader:
   mid = row[0]
   title = row[1]
   genre = row[2]
   imdb = row[3]
   tmdb = row[4]

   Movies.objects.get_or_create(movieId = mid,title = title,genres = genre,imdbId = imdb,tmdbId = tmdb)