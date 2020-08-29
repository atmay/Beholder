import time
import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()

VK_TOKEN = os.getenv('TokenVK')
VK_URL = os.getenv('UrlVK')

TWILIO_ACCOUNT_SID = os.getenv('SidTwilio')
TWILIO_AUTH_TOKEN = os.getenv('TokenTwilio')
TWILIO_NUMBER = os.getenv('TwilioNumber')
MY_NUMBER = os.getenv('MyNumber')


def get_status(user_id):
    params = {
        'user_ids': user_id,
        'fields': 'online',
        'access_token': VK_TOKEN,
        'v': '5.92'
    }
    result = requests.post(VK_URL, params=params).json().get('response')
    status = result[0]['online']
    return status


def sms_sender(sms_text):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(to=MY_NUMBER,
                                     from_=TWILIO_NUMBER,
                                     body=sms_text)
    return message.sid


if __name__ == '__main__':
    vk_id = input('Введите id ')
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
