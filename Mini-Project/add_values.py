from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *
import csv
client = RecombeeClient('web-tech-sns', 'uwwPlhjPTvJH5ALXh6J2aEcIEcoorlXatCxB0xGgmWieOtkCQXok1wL3bd7Ni7JV')
movie=[]
with open('ml-latest-small/movies.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        Id = row[0]
        movie_title = row[1]
        movie_genre = row[2]
        genres = movie_genre.split('|')
        request = SetItemValues(Id,
        {
            "title":movie_title,
            "genre":genres
        },
            cascade_create=True
        )
        movie.append(request)

try:
    print('Send')
    client.send(Batch(movie))

except APIException as e:
    print(e)
