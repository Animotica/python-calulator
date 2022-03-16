from os import system
def clear():
    try:
        system("cls")
    except:
        system("clear")
def aftercal(message):
    message = ''
    print("If you want to calculate another calculation enter 'y' if not enter 'n'.")
    yn = input()
    if yn.lower() == "y":
        print("To '*', '/', '+', '-' enter'1'")
        print("To 'x^y' enter '2'")
        print("To get the square root enter '3'")
        cal_option = input()
        if cal_option == '1':
            clear()
            calculat(message)
        elif cal_option == '2':
            clear()
            calculat_2(message)
        elif cal_option == '3':
            clear()
            calculat_3(message)
        else:
            print("Invalid Input")
            aftercal(message)
    elif yn.lower() == "n":
        quit()
    else:
        print("Invalid Input. Enter Again.")
        aftercal(message)
def calculat(message):
    clear()
    print(message)
    number1 = input("First number: ")
    number2 = input("Second number: ")
    for x in number1 and number2:
        if x not in digits:
            message = "An error has occured: <<'input wasn't a valid number!'>>'"
        else: pass
    output = float(number1) + float(number2)
    print(f"{str(number1)} + {str(number2)} = {str(output)}")
    output = float(number1) - float(number2)
    print(f"{str(number1)} - {str(number2)} = {str(output)}")
    output = float(number1) * float(number2)
    print(f"{str(number1)} * {str(number2)} = {str(output)}")
    output = float(number1) / float(number2)
    print(f"{str(number1)} / {str(number2)} = {str(output)}"), aftercal(message)
def calculat_2(message):
    clear()
    print(message)
    num = input("Enter x^y: ")
    num = num.split('^')
    for x in num:
        if x in '-':
            message = "An error has occured: <<input wasn't a number or '^'!>>", clear()
            calculat_2(message)
        else: pass
    num1 = int(num[0])
    num2 = int(num[1])
    num_calc = num1**num2
    print(f"{str(num[0])} ^ {str(num[1])} = {str(num_calc)}"), aftercal(message)
def calculat_3(message):
    user = input("Enter a number: ")
    user = user.replace(' ', '')
    for x in user:
        if x in '-' or not digits:
            clear()
            print("Input was negative or a letter PLEASE enter a positive number"), calculat_3(message)
        else: pass
    try: 
        sq = float(user)**(1/2)
        print(f"The square root of {str(user)} = {str(sq)}")
        sq = float(user)**(1/3)
        print(f"The cube root of {str(user)} = {str(sq)}"), aftercal(message)
    except:
        clear()
        print("An error has occured... Please try again"), calculat_3(message)          
def start(message):
    print("To '*', '/', '+', '-' enter'1'")
    print("To 'x^y' (no decimal numbers) enter '2'")
    print("To get the square and cube root enter '3'")
    cal_option = input()
    if cal_option == '1':
        clear()
        calculat(message)
    elif cal_option == '2':
        clear()
        calculat_2(message)
    elif cal_option == '3':
        clear()
        calculat_3(message)
    else:
        print(f"That wasn't an option: {cal_option}")
        start(message)       
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
message = ''
clear()
start(message)
