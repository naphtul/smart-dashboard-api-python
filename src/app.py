from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from controllers.Irrigation import app as irrigation
app.register_blueprint(irrigation)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
