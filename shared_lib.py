#!/usr/bin/env python3

import requests
from pprint import pprint as pp


class SharedLibrary:
    def __init__(self, url=None):
        self.url = ''
        if not url:
           self.url = "https://api.chucknorris.io/jokes/random"
        print('Shared library activated')

    def get_chuck_joke_category(self, category=None):
        if not category:
            category='movie'
        self.set_url('https://api.chucknorris.io/jokes/random?category={0}'.format(category))
        print('Get joke category called in shared library')
        joke_json = self.make_request()
        return joke_json['value']

    def get_chuck_joke_id(self, random_param='a_param'):
        print('Get joke id called in shared library')
        joke_json = self.make_request()
        return joke_json['id']

    def get_url_content(self, random_param='a_param'):
        print('Get joke content called in shared library')
        joke_json = self.make_request()
        return joke_json

    def set_url(self, url):
        self.url = url

    def make_request(self, ):
        req = requests.get(self.url)
        data = req.json()
        try: 
            req.raise_for_status()
        except requests.exceptions.HTTPError as e: 
            print('HTTP Error: {0}'.format(e))

        return data