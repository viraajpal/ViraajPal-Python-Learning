import random
randNumber = random.randint(1, 100)
print(randNumber)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter Your Guess: "))
    guesses += 1
    if(userGuess==randNumber):

        print("You Guess it Right!")

    else:
        if(userGuess>randNumber):

            print("You Guessed it wronng ! Enter a smaller number!")
        else:
            print("You guessed it wrong! Enter a larger number!")

        guesses += 1

print(f"You guesses the number in {guesses} gueses")

with open("another.txt", "r") as f:
    another = int(f.read())

if(guesses<another):
    print("you have broken the hiscore record!")

with open("another.txt", "w") as f:
    f.write(str(guesses))