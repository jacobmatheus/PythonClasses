print("Welcome to the calculator, insert the operation desired: + - * /")
operation = input("->")
nun1 = int(input("Type in the first number: "))
nun2 = int(input("Type in the second number: "))

if operation == "+":
    print(nun1, "+", nun2, "=", nun1+nun2)
elif operation == "-":
    print(nun1, "-", nun2, "=", nun1-nun2)