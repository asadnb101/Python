#build  a calculator
operator = input("Enter an operator  ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if operator == "+":
    ans = num1 + num2
    print("The ans is" ,ans)
    
elif operator == "-":
    ans = num1 + num2
    print("The ans is" ,ans)
 
elif operator == "*":
        ans = num1 * num2
        print("The ans is" ,ans)
    
elif operator == "/":
    ans = num1 / num2
    print("The ans is" ,ans)       
    
else:
    print("invalid operator")
