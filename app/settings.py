import os

# facebook config
FB_VERIFY_TOKEN = "banange"
FB_ACCESS_TOKEN = "EAAcLyLNtP4YBAAUaQRrEdYx3TuZAZC9fTcbmHv0OUZBp4nI7PeZCEvtgdu5k4lFns0gUD3TVZBufekwie6SDdKxewAWaW6b04s05EYcdfUvhEGBYOAeIsbkdQCI3ebAi3DzmXoqDCZASEGJib5s6kukLV4bk6Nj5ViTUnjIDOqPwZDZD"

# configuration for the database url.
DATABASE_URL = os.getenv('DATABASE_URL',
                         'postgres://sinshsojtiexeq:edc5c508a2bc4c375d450a395a86851801ba59a1a3700c8f9fad0a945389eaff@ec2-50-16-228-232.compute-1.amazonaws.com:5432/d1n5ejp83fah5t')
APP_SECRET_KEY = os.getenv('SECRET_KEY',
                           'this-really-needs-to-be-changed')
