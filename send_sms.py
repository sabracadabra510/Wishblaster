import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC8c4c6bbbe9876c4a960bd59b2bcf6f4f'
auth_token = '51d8175b66f818963269de447c87cd83'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Justin's Birthday is coming up next on March 3rd!",
                     from_='+15102015515',
                     to='+15103298526'
                 )

print(message.sid)