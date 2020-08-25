import time
# num1 = int(input("Enter first number: "))
# operator = str(input("Enter a operator: "))
# num2 = int(input("Enter second number: "))
# operation_to_be_done ={"+": num1+num2, "-": num1-num2, "*": num1*num2, "/": num1/num2, "%": num1%num2}
# print(operation_to_be_done.get(operator, None))
while True:
    x = int(input("Which type of input you will be giving?: Ex: \
                \n\t1. 25\n\t   +\n\t   98 \
                \n\n\t2. 25+98 \n \
Enter your input: "))
    if x == 1:
        num1 = int(input("Enter first number: "))
        operator = str(input("Enter a operator: "))
        num2 = int(input("Enter second number: "))
        operation_to_be_done ={"+": num1+num2, "-": num1-num2, "*": num1*num2, "/": num1/num2, "%": num1%num2}
        print(operation_to_be_done.get(operator, None))
    else:
        print("\n" + str(eval(input("Enter a calculation: "))))
    print()
    x = input("Do you want to try again? Type y or n: ")
    if x == "n" or x == "n":
        break
        