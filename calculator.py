def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")

    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+ - * /): ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                raise ZeroDivisionError("Error: Division by zero")
            result = num1 / num2
        else:
            print("Invalid operator")
            return

        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except ZeroDivisionError as e:
        print(e)

calculator()
