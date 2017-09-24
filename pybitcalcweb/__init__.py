from flask import Flask
from json import dumps


def format_pretty_json(json_output):
    return dumps(json_output, indent=4, sort_keys=True)


'''def format_decimal(amount):
    return '{:0.3f}'.format(amount).rstrip("0").rstrip(".")'''

def format_decimal(amount):
    amt_whole = int(amount)
    amt_whole_len = len(str(amt_whole))

    if amount < 1:
        amt_str = '{:0.15f}'.format(amount).rstrip("0").rstrip(".")
    elif amt_whole_len < 4:
        amt_str = '{:0.3f}'.format(amount).rstrip("0").rstrip(".")
    elif amt_whole_len < 6:
        amt_str = '{:0.2f}'.format(amount).rstrip("0").rstrip(".")
    elif amt_whole_len < 9:
        amt_str = '{:0.1f}'.format(amount).rstrip("0").rstrip(".")
    else:
        amt_str = '{}'.format(amt_whole)

    return amt_str


# Create Flask app
app = Flask(__name__)
app.config.from_object('config')

# Define some jinja2 filters
app.jinja_env.filters['pretty_json'] = format_pretty_json
app.jinja_env.filters['decimal'] = format_decimal

# Trim and lstrip blocks so HTML source is neat
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

from pybitcalcweb import views
