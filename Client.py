import requests, csv

# Create a function that maps the operator input from the user (or file) to their actual names (for the server's route)
def operation_name(operator_: str) -> str:
    operation_ = ""
    match operator_:
        case "+":
            operation_ = "addition"
        case "-":
            operation_ = "subtraction"
        case "*":
            operation_ = "multiplication"
        case "/":
            operation_ = "division"

    return operation_


# Call the root endpoint which is just a "welcome" message
welcome = requests.get("http://localhost:5000/")
print(welcome.text)


while True:

    # With this, one is able to toggle between parts of the assignment
    choice = input("Do you want to input the operation yourself or read it from the sample file ('q' to terminate)?\n"
                   "[1] Manual input\n"
                   "[2] Input from file\n")

    match choice:
        case "1":
            # Ask for the first value of the operation
            a = input("Enter the first value of the operation ('q' to terminate): ")
            if a == "q":
                break

            aux = 0
            while aux == 0:
                # Ask for the operation that the user wants to perform
                operator = input("Enter the operation you want to perform (+, -, *, /): ")
                if operator != "+" and operator != "-" and operator != "*" and operator != "/":
                    print("Invalid operation")
                else:
                    # Substitute the operator for the word to access the right url (in the server side)
                    operation = operation_name(operator)
                    aux = 1

            # Ask for the second value
            b = input("Enter the second value of the operation ('q' to terminate): ")
            if b == "q":
                break

            # Create and request the desired operation
            url = f"http://localhost:5000/{operation}?a={a}&b={b}"
            response = requests.get(url)

            print(f"\nThe answer to {a} {operator} {b} is: ", response.text + "\n")

        case "2":
            log = input("\nDo you want a log of all the operations and results? [y][n]\n")
            # Open the sample file
            with open("sample.csv", "r") as f:
                reader = csv.reader(f)
                # Iterate the entire file and print every operation
                for line in reader:
                    a = str(line[0])
                    operator = str(line[1])
                    operation = operation_name(operator)
                    b = str(line[2])

                    # Create and request the desired operation
                    url = f"http://localhost:5000/{operation}?a={a}&b={b}"
                    response = requests.get(url)

                    print(f"The answer to {a} {operator} {b} is: ", response.text)

                    # If the user wants, it can generate a log file as a .txt
                    if log == "y":
                        with open("log_file.txt", "a") as log_file:
                            log_file.write(a + operator + b + " = " + response.text + "\n")

        case "q":
            break

        case default:
            print("Enter a valid option")

