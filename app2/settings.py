import os

# facebook config
FB_VERIFY_TOKEN = "banange"
FB_ACCESS_TOKEN = "EAAcLyLNtP4YBAAUaQRrEdYx3TuZAZC9fTcbmHv0OUZBp4nI7PeZCEvtgdu5k4lFns0gUD3TVZBufekwie6SDdKxewAWaW6b04s05EYcdfUvhEGBYOAeIsbkdQCI3ebAi3DzmXoqDCZASEGJib5s6kukLV4bk6Nj5ViTUnjIDOqPwZDZD"

# configuration for the database url.
DATABASE_URL = os.getenv('DATABASE_URL',
                         'postgres://jus_machungwa@localhost/bot_db')
APP_SECRET_KEY = os.getenv('SECRET_KEY',
                           'this-really-needs-to-be-changed')
