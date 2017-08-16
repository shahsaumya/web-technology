from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *
client = RecombeeClient('sns', 'cqLZqZnboKlyVKS7EhhYYyM8BflGRDlizngZbljA3kp67tjd1FKfH3WaXLNSXl7F')
count = 1
users=[]
for i in range(1,672):
    client =