from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *
client = RecombeeClient('sns', 'cqLZqZnboKlyVKS7EhhYYyM8BflGRDlizngZbljA3kp67tjd1FKfH3WaXLNSXl7F')
print(client.send(GetItemValues('1')))
print(client.send(ListItemProperties()))
recommended = client.send(UserBasedRecommendation('672',5,filter="Animation" in 'genre'))
print(recommended)