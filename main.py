from twilio.rest import Client

account_sid = 'AC9ed5c6e5ce7c778c08d35968d2ed0a07'
auth_token = 'f5415927b6a704cbf4033ff3c6639ddc'
client = Client(account_sid, auth_token)
def send_msg():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='How are you',
        to='whatsapp:+919865288018'
)

    print(message.sid)

