def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")

    try:
        number1 = float(input("Enter first number: "))
        operator = input("Enter operator (+ - * /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = number1 + num2
        elif operator == "-":
            result = number1 - num2
        elif operator == "*":
            result = number1 * num2
        elif operator == "/":
            if num2 == 0:
                raise ZeroDivisionError("Error: Division by zero")
            result = number1 / num2
        else:
            print("Invalid operator")
            return

        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except ZeroDivisionError as e:
        print(e)

calculator()
