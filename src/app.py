from flask import Flask
from flask_cors import CORS

from controllers.Irrigation import app as irrigation
from controllers.Garage import app as garage

app: Flask = Flask(__name__)
CORS(app)
app.register_blueprint(irrigation)
app.register_blueprint(garage)


if __name__ == '__main__':
    app.run()
