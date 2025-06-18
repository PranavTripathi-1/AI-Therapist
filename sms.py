from twilio.rest import Client

def send_sms(to_number, body):
    account_sid = 'YOUR_TWILIO_SID'
    auth_token = 'YOUR_TWILIO_AUTH'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=body,
        from_='YOUR_TWILIO_NUMBER',
        to=to_number
    )
    return message.sid
