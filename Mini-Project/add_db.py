from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *
import csv
from datetime import date
client = RecombeeClient('web-tech-sns', 'uwwPlhjPTvJH5ALXh6J2aEcIEcoorlXatCxB0xGgmWieOtkCQXok1wL3bd7Ni7JV')
# client.send(ResetDatabase())
client.send(AddItemProperty('title','string'))
client.send(AddItemProperty('genre','set'))
client.send(AddItemProperty('imdbId','string'))
client.send(AddItemProperty('tmdbId','string'))