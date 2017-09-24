from flask import Flask
from json import dumps


def format_pretty_json(json_output):
    return dumps(json_output, indent=4, sort_keys=True)


def format_decimal(amount):
    return '{:0.3f}'.format(amount).rstrip("0").rstrip(".")


def format_decimal_zero(amount):
    return '{:0.15f}'.format(amount).rstrip("0").rstrip(".")


# Create Flask app
app = Flask(__name__)
app.config.from_object('config')

# Define some jinja2 filters
app.jinja_env.filters['pretty_json'] = format_pretty_json
app.jinja_env.filters['decimal'] = format_decimal
app.jinja_env.filters['decimal_zero'] = format_decimal_zero

# Trim and lstrip blocks so HTML source is neat
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

from pybitcalcweb import views
