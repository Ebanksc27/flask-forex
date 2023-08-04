from flask import Flask, render_template, request, redirect, flash, url_for
from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError, DecimalFloatMismatchError

import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'defualt-secret-key')

# Initialize currency utilities 
cr = CurrencyRates()
cc = CurrencyCodes()

def get_rate(currency):
    """
    Fetches the exchange rate for the given currency. If the rate cannot be fetched,
    flashes a user-friendly error message and returns False. Otherwise, returns True.
    """
    try:
        cr.get_rate(currency, currency)
    except (RatesNotAvailableError, DecimalFloatMismatchError):
        flash('The currency code is invalid or the rate is not available.')
        return False
    return True

@app.route('/', methods=['GET', 'POST'])
def home():
     # Get a dictionary of all exchange rates relative to CAD
    currencies = cr.get_rates('CAD')
    currencies['CAD'] = 1.0  # Manually add the base currency

    if request.method == 'POST':
        from_currency = request.form.get('from_currency')
        to_currency = request.form.get('to_currency')
        amount = request.form.get('amount')

        # validate the amount
        try:
            amount = float(amount)
        except ValueError:
            flash('The amount should be a number.')
            return redirect(url_for('home'), 400)

        # validate the currencies
        if not get_rate(from_currency) or not get_rate(to_currency):
            return redirect(url_for('home'), 400)
        
        # start conversion
        result = cr.convert(from_currency, to_currency, amount)
        from_symbol = cc.get_symbol(from_currency)
        to_symbol = cc.get_symbol(to_currency)
        flash(f'{from_symbol} {amount} = {to_symbol} {result:.2f}')

    return render_template('home.html', currencies=currencies)


# if __name__ == '__main__':
    # app.run(debug=True) 

