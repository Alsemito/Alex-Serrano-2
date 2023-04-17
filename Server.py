from flask import Flask, request

app = Flask(__name__)

@app.route("/index")
def index() -> str:
    return "Welcome to the simple calculator server"

@app.route("/+")
def addition() -> str:
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a + b
    return str(result)

@app.route("/-")
def subtraction() -> str:
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a - b
    return str(result)

@app.route("/*")
def multiplication() -> str:
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a * b
    return str(result)

@app.route("/")
def division() -> str:
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    if b == 0:
        return "Error: Division by zero"
    else:
        result = a / b
        return str(result)


if __name__=='__main__':
    app.run()