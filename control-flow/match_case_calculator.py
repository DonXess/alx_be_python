number1 = int(input("Enter the first number: \t"))
number2 = int(input("Enter the second number: \t"))
operation = input("Choose the operation (+, -, *, /): \t")
match operation :
    case "/" :
        if number2 == 0 :
            print("Cannot divide by zero")
        else :
            print("The result is ",number1/number2)
    case "+" :
        print("The result is ",number1+number2)
    case "-" :
        print("The result is ",number1-number2)
    case "*" :
        print("The result is ",number1*number2)