# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def adding():
    """Adds a and b parameters"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)

# in URL add?a=10&b=20 gives you 30

@app.route("/sub")
def subtracting():
    """Subtracts a and b parameters"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)

# sub?a=10&b=20 gives you -10

@app.route("/mult")
def multiplying():
    """Multiplies a and b parameters"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)

# mult?a=10&b=20 gives you 200

@app.route("/div")
def dividing():
    """Divides a and b parameters"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)

# div?a=10&b=20 gives you 0.5