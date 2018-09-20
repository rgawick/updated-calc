from calculator import addition, subtraction, multipication, division

while True:
    try:
        first = int(input("First Number: "))
        operand = input("Would you like to +, -, * or / ? ")
        second = int(input("Second Number: "))

        if operand == "+":
            addition(first, second)
            break
        elif operand == "-":
            subtraction(first, second)
            break
        elif operand == "*":
            multipication(first, second)
            break
        elif operand == "/":
            division(first, second)
            break
        else:
            print("Please enter a valid operand.")
    except ValueError:
        print("Please enter numbers only!")

quit = input("To quit the program, please press q then hit enter.").lower()
if quit == "q":
    import sys
    sys.exit(0)
