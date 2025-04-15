while True:
    user_input_num = input("Enter a number with a space in between: ")
    try:
        num1, num2 = user_input_num.split(" ")
        num1 = int(num1)
        num2 = int(num2)
        print(num1 + num2)
        break
    except ValueError:
        print("Wrong input! Maybe you forgot to add space in between those two digits.")