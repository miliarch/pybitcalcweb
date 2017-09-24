from flask import render_template, redirect, url_for, request, flash
from pybitcalcweb import app
from . import bitcalc


@app.route('/')
def site_root():
    return redirect(url_for('calculator'))


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    user_input = {
        'amount': request.args.get('amount'),
        'prefix': request.args.get('prefix'),
        'type': request.args.get('type'),
        'base': request.args.get('base')
    }

    arg_count = 0

    for key in user_input:
        arg_count += 1 if user_input[key] else 0

    all_required_args = False if arg_count < 4 else True

    if all_required_args:
        return calculate(user_input)
    else:
        return render_template('calculator.html')


def calculate(user_input):
    sanitized_input = bitcalc.sanitize_input(user_input)

    if len(sanitized_input['errors']) > 0:
        for error in sanitized_input['errors']:
            flash(error)
        return redirect(url_for('calculator'))

    bit_value = bitcalc.convert_amount_to_bits(
        sanitized_input['amount'],
        sanitized_input['prefix'],
        sanitized_input['type'],
        sanitized_input['base'])

    conversion_table = bitcalc.generate_conversion_table(
        bit_value,
        sanitized_input['base'])

    return render_template(
        'calculator.html',
        sanitized_input=sanitized_input,
        conversion_table=conversion_table)
