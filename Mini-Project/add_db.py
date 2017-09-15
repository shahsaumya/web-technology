from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *
import csv
from datetime import date
client = RecombeeClient(
    'sns', 'cqLZqZnboKlyVKS7EhhYYyM8BflGRDlizngZbljA3kp67tjd1FKfH3WaXLNSXl7F')
# client.send(ResetDatabase())
client.send(AddItemProperty('title', 'string'))
client.send(AddItemProperty('genre', 'set'))
client.send(AddItemProperty('imdbId', 'string'))
client.send(AddItemProperty('tmdbId', 'string'))
