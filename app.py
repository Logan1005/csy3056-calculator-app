

# File: app.py
# Purpose: Web-based frontend for the calculator using Flask
# Dependencies: Flask, calculator module

from flask import Flask, render_template, request, jsonify
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("calculator.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    result = None
    error = None

    if request.method == 'POST':
        try:
            a = float(request.form.get("a"))
            b = float(request.form.get("b"))
            op = request.form.get("operation")

            if op == "add":
                result = add(a, b)
            elif op == "subtract":
                result = subtract(a, b)
            elif op == "multiply":
                result = multiply(a, b)
            elif op == "divide":
                result = divide(a, b)
            else:
                error = "Invalid operation"
        except ValueError:
            error = "Please enter valid numbers"
        except Exception as e:
            error = str(e)

    return render_template("calculator.html", result=result, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

