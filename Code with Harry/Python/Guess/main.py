import random
randNumber = random.randint(1,100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter Your Guess :"))
    if(userGuess == randNumber):
        print("You guessed it right !")
    elif(userGuess < randNumber):
        print("You guess is low : Aim Higher")
        guesses+=1
    else:
        print("You guess is high : Aim Lower")
        guesses+=1
        
print(f"You gueesd in {guesses} guesses")

with open("highscore.txt", "r") as f:
    highscore = int(f.read())
    
if guesses<highscore:
    print("You just broke the high score !")
    with open("highscore.txt" , "w") as f:
        f.write(str(guesses))
 
   
