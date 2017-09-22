from flask import Flask

# Create Flask app
app = Flask(__name__)
app.config.from_object('config')

from pybitcalcweb import views
