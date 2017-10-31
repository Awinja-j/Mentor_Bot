from flask import Blueprint, request, jsonify, Response, abort
import requests, sys, json
from manage import app
from webhook import process_bot_query

blueprint = Blueprint('bot', __name__)

FB_VERIFY_TOKEN = 'banange'
FB_ACCESS_TOKEN = "EAAcLyLNtP4YBAAUaQRrEdYx3TuZAZC9fTcbmHv0OUZBp4nI7PeZCEvtgdu5k4lFns0gUD3TVZBufekwie6SDdKxewAWaW6b04s05EYcdfUvhEGBYOAeIsbkdQCI3ebAi3DzmXoqDCZASEGJib5s6kukLV4bk6Nj5ViTUnjIDOqPwZDZD"

@blueprint.route('/webhook', methods=['GET'], strict_slashes=False)
def handle_verification():
    #webhook verification
    print "Handling Verification."
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == FB_VERIFY_TOKEN:
            return "Invalid verification token", 403
        return requests.args['hub.challenge']
    return "Verification successful!", 200

@blueprint.route('/webhook', methods=['POST'], strict_slashes=False)
def handle_messages():
    print "Handling Messages"
    payload = request.get_data()
    for sender, message in messaging_events(payload):
        print "Incoming from %s: %s" % (sender, message)
        send_message(FB_ACCESS_TOKEN, sender, message)
    return "ok", 200

def messaging_events(payload):
    """Generate tuples of (sender_id, message_text) from the
    provided payload.
    """
    data = json.loads(payload)
    messaging_events = data["entry"][0]["messaging"]
    for event in messaging_events:
        if "message" in event and "text" in event["message"]:
            # query = ''.join((nested_lookup('text', data)))
            yield event["sender"]["id"], process_bot_query(query)

def send_message(token, recipient, text):
    """Send the message text to recipient with id recipient.
    """
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
    params={"access_token": token},
    data=json.dumps({
        "recipient": {"id": recipient},
        "message": {"text": text}
        }),
    headers={'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        print r.text