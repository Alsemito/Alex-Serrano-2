import requests

while True:

    a = input("Enter the first value of the operation ('quit' to terminate): ")
    if a == "quit":
        break

    aux = 0
    while aux == 0:
        operation = input("Enter the operation you want to perform (+, -, *, /): ")
        if operation != "+" and operation != "-" and operation != "*" and operation != "/":
            print("Invalid operation")
        else:
            aux = 1

    b = input("Enter the second value of the operation ('quit' to terminate): ")
    if b == "quit":
        break


    url = f"http://localhost:5000/{operation}?a={a}&b={b}"
    response = requests.get(url)

    print(f"The answer to {a} {operation} {b} is: ", response.text)
