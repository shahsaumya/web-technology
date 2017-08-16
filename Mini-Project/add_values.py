from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *
import csv
client = RecombeeClient('sns', 'cqLZqZnboKlyVKS7EhhYYyM8BflGRDlizngZbljA3kp67tjd1FKfH3WaXLNSXl7F')
# movie=[]
# with open('ml-latest-small/movies.csv') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         Id = row[0]
#         movie_title = row[1]
#         movie_genre = row[2]
#         genres = movie_genre.split('|')
#         request = AddItem(Id)
#         request = SetItemValues(Id,
#         {
#             "title":movie_title,
#             "genre":genres
#         },
#             cascade_create=True
#         )
#         movie.append(request)

# try:
#     print('Send')
#     client.send(Batch(movie))

# except APIException as e:
#     print(e)

links = []
with open('ml-latest-small/links.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        Id = row[0]
        movie_imdb = row[1]
        movie_tmdb = row[2]
        request = SetItemValues(Id,
        {
            "imdbId":movie_imdb,
            "tmdbId":movie_tmdb
        },
            cascade_create=True
        )
        links.append(request)

try:
    print('Send')
    client.send(Batch(links))

except APIException as e:
    print(e)
