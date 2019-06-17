from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACb7dce3fccd3eda8f0bdaf1612b4b3170" #"ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "9ed17649c49275a019df62027a1a8031" #"your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15104701089", 
    # My twilio number
    from_="+14159141149",
    body="Hello from Key!")

print(message.sid)