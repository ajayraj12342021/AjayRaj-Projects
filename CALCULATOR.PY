try:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))

    print("What kind of operation you want to perform? \nPress + for addition \nPress - for subtraction \nPress * for  multiplication \nPress / for division:")

    operation=input("Enter Operation:")

    match operation:
        case"+":
            print(f"The result is {num1+num2}")
        case "-":  
            print(f"The result is {num1-num2}")
        case "*":
            print(f"The result is {num1*num2}")
        case "/":
            try:
                print(f"The result is {num1/num2}")
            except ZeroDivisionError:
                print("Division by zero is not possible")
        case _:
            print(f"There was an error")

except Exception as e:
    print("Enter a valid value of a and b")              
    
