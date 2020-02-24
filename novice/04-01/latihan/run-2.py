from flask import Flask
from flask.views import MethodView

app = Flask(__name__)

class Animal(MethodView):

    def get(self):
        return 'Returned an animal!'

    def post(self):
        return 'Created an animal!'

    def put(self):
        return 'Modified an animal!'

    def delete(self):
        return 'Deleted an animal!'

. env