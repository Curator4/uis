from flask import Flask
import psycopg2
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'omfaofnjuafafa23231'

#database connect
db = "dbname='minsp' user='sofus' host='localhost' password='123'"
conn = psycopg2.connect(db)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'


from .views import views
from .auth import auth
from .results import results

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(results, url_prefix='/')
