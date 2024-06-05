# Create the number to be guessed
intAns = 12345
intGuess = 1

while intGuess != 0:
    # Get input from user
    intGuess = int(input("Enter Guess or 0 to exit: "))

    # main testing sequence
    if intGuess == intAns:
        print(f"Your guess = {intGuess} is Correct")
        intGuess = 0
    elif intGuess == 0:
        break
    else:
        print(f"Your guess = {intGuess} is Wrong")
print("Goodbye")