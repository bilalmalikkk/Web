from flask import Flask, render_template
from flask_restful import Api
from database import db
from resources import routes
import json  # Add this line to import the json module

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost:27017/User'
}

# Define your JSONEncoder subclass
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        # Implement your custom serialization here
        # Return a serializable representation of the object
        pass

# Use your custom JSONEncoder for the app
app.json_encoder = CustomJSONEncoder
api = Api(app)
db.initialize_db(app)
routes.initialize_routes(api)


@app.route('/')
def register():
    return render_template("register.html")

@app.route('/login')
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)
