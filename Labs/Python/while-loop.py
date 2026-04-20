import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#Generate the number that has to be guessed
number = random.randint(1,10)

#Keep track if the guess is right
isGuessRight = False

#While the guess is not right do
while isGuessRight != True:
    #ask for the user to guess the number
    guess = input("Guess a number between 1 and 10: ")
    #compare the guess with the number generated
    if int(guess) == number:
        #if the user guessed correctly
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    #if the user did not guess correctly
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
