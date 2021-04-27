import json
from flask import  request

CONFIG_FILE = 'UserInterface/config.json'
class UserInterface:

    def __init__(self, app):
        self.routes = json.load(open(CONFIG_FILE))
        self.routes_response = {}

        for route in self.routes:
            self.routes_response[route] = open(self.routes[route],'rb').read()
            app.add_url_rule(route, 'self.response', self.response)

    def response(self):
        return self.routes_response[request.path]