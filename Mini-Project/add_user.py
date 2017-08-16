from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *
client = RecombeeClient('sns', 'cqLZqZnboKlyVKS7EhhYYyM8BflGRDlizngZbljA3kp67tjd1FKfH3WaXLNSXl7F')
count = 1
users=[]
for i in range(1,673):
    request = AddUser(str(count))
    count=count+1
    users.append(request)
try:
    print('sending')
    client.send(Batch(users))
    print('sent')

except APIException as e:
    print(e)