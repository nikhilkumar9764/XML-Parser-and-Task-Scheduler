import warnings
from WebServices.Controller import Controller
import json

warnings.filterwarnings('ignore', message='Unverified HTTPS request')

CONFIG_FILE = 'WebServices/Config/Route.json'

class WebServices:


    def __init__(self, app):

        self.controller = Controller.getInstance()
        self.addRoutes(app)

    def addRoutes(self, app):
        self.routes = json.load(open(CONFIG_FILE))
        print('Add Routes')
        print(self.routes)

        for route in self.routes:
            app.add_url_rule(route, str(self.routes[route]), eval(self.routes[route][1]),methods=[self.routes[route][0]])










