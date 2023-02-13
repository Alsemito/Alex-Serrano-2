from flask import Flask, request

app = Flask(__name__)

@app.route('/calculator', methods=['GET'])
def calculator():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    operation = request.args.get('operation')

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        return "Error: Invalid operation. Supported operation are +, -, *, /"

    return str(result)

if __name__=='__main__':
    app.run()