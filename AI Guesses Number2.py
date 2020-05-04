import random
print("Number Guessing Game")
print("Do you want to pick a random number for the computer to guess? Yes/No")
randomchoice = input()
if randomchoice.lower() == 'yes': #converts to one case, captures Yes, YES, YEs...
#if randomchoice.startswith('y'): #would accept Y.. Ye.. Yes...
    print("A random number will be selected to guess")
    number = random.randint(1,100)
    print("Your random number is", number)
else: #anything other than yes (includes "y")
    while True:
        number = int(input("Please enter a number between 1 and 100: "))
        if 1 <= number <= 100:
            break
        print('Your number was not between 1 and 100, please try again')
    print("You have selected", number)
print("The computer will now guess your number")
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
input()
