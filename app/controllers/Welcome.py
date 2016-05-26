"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import oauth2 as oauth
import json
import os

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)

        CONSUMER_KEY = os.environ['CONSUMER_KEY']
        CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
        ACCESS_KEY = os.environ['ACCESS_KEY']
        ACCESS_SECRET = os.environ['ACCESS_SECRET']

        consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
        access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
        global client
        client = oauth.Client(consumer, access_token)

        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):
        timeline_endpoint = "https://api.twitter.com/1.1/statuses/home_timeline.json"
        response, data = client.request(timeline_endpoint)
        tweets = json.loads(data)
        return self.load_view('index.html', tweets=tweets)
