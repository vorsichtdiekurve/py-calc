"""
A simple one-op (sum) calculator

This application calculates the sum of two integers.
"""

from flask import Flask, request

app = Flask(__name__)


@app.route('/calculate')
def calculate():
    """Endpoint to access the calculator functionality

    This function contains the code to calculate the sum of two integers and
    return the entire operation as a string.
    """

    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)
    if op == 'sum':
        return f"{arg1} + {arg2} = {arg1 + arg2}"

    return "Invalid operation"


if __name__ == '__main__':
    app.run()
