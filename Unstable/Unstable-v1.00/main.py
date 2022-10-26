#interact with terminal to add and divide




print("Choose the desired mathematical equation, press the letter on your keyboard that matches the options below")
print("Press A to add two numbers")
print("Press S to subtract two numbers")
print("Press M to multiply two numbers")
print("Press D to divide two numbers")
print("### EXTREMELY IMPORTANT: LETTERS MUST BE IN CAPITALIZED TO WORK, A FIX FOR THIS WILL BE IMPLEMENTED LATER ###")

while True:

#input to the caculator
    mathoperation = input(str("Please select the operation: "))
    if mathoperation == str("A", "S", "M", "D"):
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))

        if mathoperation == "A":
            print(number1, "+", number2, "=", number1 + number2)

        elif mathoperation == "S":
            print(number1, "-", number2, "=", number1 - number2)
         
        elif mathoperation == "M":
            print(number1, "*", number2, "=", number1 * number2)
    
        elif mathoperation == "D":
            print(number1, "/", number2, "=", number1 / number2)

        else:
            print("Error: Invalid letter selected, the letter that was selected was not one of the options.")
            break
