from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound

from app1 import app as app1
from app2 import app as app2
from app3 import app as app3

app = Flask(__name__)

app.wsgi_app = DispatcherMiddleware(NotFound(), {
    '/app1': app1,
    '/app2': app2,
    '/app3': app3
})


if __name__ == "__main__":
    app.run()