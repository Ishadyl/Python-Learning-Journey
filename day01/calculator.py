a = int(input("Enter the first number: "))
character = input("Enter the operator : ")
b = int(input("Enter the second number: "))

if character == '+':
    print(a+b)
elif character == '-':
    print(a-b)
elif character == '*':
    print(a*b)
elif character == '/':
    print(a/b)
else:    print("Invalid operator")