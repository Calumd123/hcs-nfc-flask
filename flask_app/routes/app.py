import os
import sys
from dotenv import load_dotenv
from twilio.rest import Client
import uuid
from dotenv import load_dotenv
from flask import Flask, Blueprint
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant

app = Blueprint('app', __name__)
load_dotenv()


@app.route('/token', methods=['POST'])
def token():
    token = AccessToken(os.environ['TWILIO_ACCOUNT_SID'],
                        os.environ['TWILIO_API_KEY_SID'],
                        os.environ['TWILIO_API_KEY_SECRET'],
                        grants=[SyncGrant(os.environ['TWILIO_SYNC_SERVICE_SID'])],
                        identity=uuid.uuid4().hex)
    return {'token': token.to_jwt().decode()}

@app.route('/nfc', methods=['POST'])
def pushNFC():

    json_data = request.get_json(force=True)
    text = json_data['text']
    client = Client()

    sync_service = client.sync.services(os.environ.get('TWILIO_SYNC_SERVICE_SID'))
    todo_list = sync_service.sync_lists('todoList')
    todo_list.sync_list_items.create({'todo': text})
    return {}
