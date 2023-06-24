first=float(input("Enter the first number to perform the operation"))
second=float(input("Enter the second number to perform the operation"))
operation=str(input("Enter the operation(+,-,*,/,%)"))
if operation == "+":
    output=first+second
elif operation == "-":
    output=first-second
elif operation == "*":
    output=first*second
elif operation == "/":
    output =first/second
elif operation == "%":
    output=first%second
else:
    output=str("please enter a valid operation")
print(output)
 