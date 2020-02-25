from flask import Flask

app = Flask(__name__)

@app.route("/")
def index_one():

    with app.app_context():
        string = 'connecting 1. . .'
        print(string)

    return "Hi im 1"




if __name__ == "__main__":
    app.run()