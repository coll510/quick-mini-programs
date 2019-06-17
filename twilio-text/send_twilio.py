# Use the Twilio API to send a text

from twilio.rest import Client
import os

# Your Account SID from twilio.com/console
account_sid =  os.environ.get("TWILIO_SID") #ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = os.environ.get("TWILIO_TOKEN") #"your_auth_token"

# Create an instance/object of the Twilio class Client
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15104701089", 
    from_="+14159141149",
    body="Hello from Key!")

print(message.sid)