import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environment 'APP_SECRET_KEY'
auth_token = os.environment 'APP_SECRET_KEY'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Christmas is coming up on December 25th!",
                     from_='+15102015515',
                     to='+15103298526'
                 )

print(message.sid)