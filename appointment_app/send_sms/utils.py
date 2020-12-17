from twilio.rest import Client
from django.conf import settings

account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN


def send_message(to_number, from_number, body_message):
    client = Client(account_sid, auth_token)
    from_number = "+12515773239"

    message = client.messages.create(
        to="+{}".format(to_number), from_=from_number, body=body_message
    )

    return message.sid
