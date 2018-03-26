from flask import Flask,render_template

from src.common.database import Database
from src.models.person.person import Person
import src.config as config
app = Flask(__name__)
app.config.from_object(config)
app.secret_key = "123"

from src.models.person.views import person_blueprint
app.register_blueprint(person_blueprint,url_prefix='/persons')

from src.models.api.api import api_blueprint
app.register_blueprint(api_blueprint, url_prefix = '/api')

@app.before_first_request
def database_inititalize():
    Database.initialize()


@app.route('/')
def home():
    persons = Person.get_all_user()
    return render_template('view-record.html', persons=persons)
