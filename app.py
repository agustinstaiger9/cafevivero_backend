from flask import Flask
from routes.contacts import contacts
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='*')

db_name = ''
db_user = ''
db_password = ''
db_host = ''
db_port = ''

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
Marshmallow(app)

app.register_blueprint(contacts, url_prefix='/api/contacts')
