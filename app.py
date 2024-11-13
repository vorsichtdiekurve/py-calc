"""
A simple one-op (sum) calculator

This application calculates the sum of two integers.
"""

from flask import Flask, request
from calculator import Calculator

app = Flask(__name__)


@app.route('/calculate')
def calculate():
    """Endpoint to access the calculator functionality

    This function contains the code to calculate the sum of two integers and
    return the entire operation as a string.
    """

    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=float)
    arg2 = request.args.get('arg2', type=float)

    if op == 'sum':
        return f"{arg1} + {arg2} = {Calculator(arg1, arg2).sum()}"

    if op == 'subtract':
        return f"{arg1} - {arg2} = {Calculator(arg1, arg2).subtract()}"

    if op == 'multiply':
        return f"{arg1} * {arg2} = {Calculator(arg1, arg2).multiply()}"

    if op == 'divide':
        if arg2 != 0:
            return f"{arg1} / {arg2} = {Calculator(arg1, arg2).divide()}"

        return "Division by zero is not allowed"

    return "Invalid operation"


if __name__ == '__main__':
    app.run()
