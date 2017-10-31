from flask import Flask
from webhook.webhook import blueprint as bot

app = Flask(__name__)

if __name__ == '__main__':
    app.run()
