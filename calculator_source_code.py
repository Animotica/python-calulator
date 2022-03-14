from os import system

def clear():
    try:
        system("cls")
    except:
        system("clear")
    pass

def aftercal():
    print("If you want to calculate another calculation enter 'y' if not enter 'n'.")
    yn = input()
    if yn.lower() == "y":
        print("To '*', '/', '+', '-' enter'1'")
        print("To '^2' enter '2'")
        cal_option = input()
        if cal_option == '1':
            calculat()
        elif cal_option == '2':
            calculat_2()
        else:
            print("Invalid Input")
            aftercal()
    elif yn.lower() == "n":
        exit()
    else:
        print("Invalid Input. Enter Again.")
        aftercal()

def calculat():
    clear()
    number1 = input("First number: ")
    number2 = input("Second number: ")
    number1 = int(number1)
    number2 = int(number2)
    output = number1 + number2 
    output = str(output)
    number1 = str(number1)
    number2 = str(number2)
    print(number1 +" + " + number2 + " = " + output)
    number1 = int(number1)
    number2 = int(number2)
    output = number1 - number2 
    output = str(output)
    number1 = str(number1)
    number2 = str(number2)
    print(number1 +" - " + number2 + " = " + output)
    number1 = int(number1)
    number2 = int(number2)
    output = number1 * number2 
    output = str(output)
    number1 = str(number1)
    number2 = str(number2)
    print(number1 +" * " + number2 + " = " + output)
    number1 = int(number1)
    number2 = int(number2)
    output = number1 / number2
    output = str(output)
    number1 = str(number1)
    number2 = str(number2) 
    print(number1 +" / " + number2 + " = " + output), aftercal()

def calculat_2():
    clear()
    num = input("Enter the number: ")
    num_calc = int(num) * int(num)
    print(f"{num}^2 = {num_calc}")
    num_calc = int(num) * int(num) * int(num)
    print(f"{num}^3 = {num_calc}")
    num_calc = int(num) * int(num) * int(num)* int(num)
    print(f"{num}^4 = {num_calc}")
    aftercal()

def start():
    print("If you want to '*', ':', '+', '-' enter '1'")
    print("If you want to '^2', '^3', '^4' something enter '2'")
    choice = input()
    if choice == '1':
        calculat()
    elif choice == '2':
        calculat_2()
    else:
        print(f"That wasn't an option: {choice}")
        start()

clear()
start()