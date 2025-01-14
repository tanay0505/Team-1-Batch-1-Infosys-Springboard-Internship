from flask import *
from models import *
from routes import  routes_blueprint
from flask_cors import CORS
from datetime import timedelta
from flask_session import Session
from flask_bcrypt import Bcrypt




# Initialize the Flask app
app = Flask(__name__,template_folder='templates')
CORS(app,supports_credentials=True, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Configuration settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Root!1234@localhost:3306/login_role_management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ABCDEF' 
app.config['SESSION_TYPE'] = 'filesystem'  # Change this to a valid type
app.config['SESSION_PERMANENT'] = False    # Optional: Sessions expire on browser close
app.config['SESSION_FILE_DIR'] = './flask_session/'  # Directory for session files if using filesystem
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)  # Sessions last for 1 day
Session(app)


# Initialize SQLAlchemy with the app
db.init_app(app)

# Register the blueprint for routes
app.register_blueprint(routes_blueprint)

# Create the database tables and insert initial data
@app.before_request
def setup_database():
    db.create_all()
    
@app.route('/')

def home():
    return render_template('index.html') 

if __name__ == '__main__':
    app.run(debug=True)
