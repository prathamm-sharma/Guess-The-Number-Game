import random

number = random.randint(1, 100 )

while True:
    userchoice = input("Guess the number or Quit : ")
    if(userchoice == "Quit"):
        break

    userchoice= int(userchoice)
    if(userchoice == number):
        print("You have guess successfully : Correct Guess!!")
        break
    elif(userchoice < number):
        print("Your number was too small. Take a bigger guess...")
    else:
        print("Your number was too big. Take a smaller guess...")


print("-------GAME OVER---------")     