num1=int(input("Enter number 1 "))
operator=input("Enter the operation you wanna perform (+,-,*,/,%) :")
num2=int(input("Enter second number "))


if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)    
elif operator=="%":
    print(num1%num2)
else:
    print("Invalid")    