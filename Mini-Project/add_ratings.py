from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *
import csv
client = RecombeeClient('sns', 'cqLZqZnboKlyVKS7EhhYYyM8BflGRDlizngZbljA3kp67tjd1FKfH3WaXLNSXl7F')
ratings=[]

interaction = AddDetailView("22", "96588",#optional parameters:
                )
ratings.append(interaction)


try:
    print('sending')
    client.send(Batch(ratings))
    print('Send')

except APIException as e:
    print(e)