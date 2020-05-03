print("Number Guessing Game")
print("Do you want to pick a random number for the computer to guess? Yes/No")
randomchoice = input()
if randomchoice.lower() == 'yes': #converts to one case, captures Yes, YES, YEs...
    print("A random number will be selected to guess")
    import random
    number = random.randint(1,100)
    print("Your random number is", number)
else: #anything other than yes
    print("Please select a number")
    number = input()
    print("You have entered", number)
print("The computer will now guess your number")
import random
aiguess = random.randint(1,100)
number = int(number)
guesses = 0
lowguess = 1
highguess = 100
while aiguess != number:
    guesses = guesses + 1
    print("Guess number #",guesses, "is", aiguess)
    if aiguess < number:
        print("The guess ",aiguess, "was too low")
        print("Try again ")
        lowguess = aiguess + 1
        aiguess = random.randint(lowguess,highguess)
    elif aiguess > number:
        print("The guess ",aiguess, "was too high")
        print("Try again ")
        highguess = aiguess - 1
        aiguess = random.randint(lowguess,highguess)
print("The computer guessed the correct number with",aiguess)
print("It took the computer", guesses+1, "guesses to find your number")