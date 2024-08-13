import random
# Snake Water Gun game just like rock paper scissors
'''
You vs Computer

 1 points for snake.
-1 points for water .
 0 points for gun.

'''
computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youDict={"s": 1,"w": -1, "g":0}
reverseDict={1: "snake", -1:"water",0: "gun"}

you = youDict[youstr]

# we have 2 player you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")


if(computer==you):
    print("It's a draw")

else:
    if(computer ==-1 and you == 1): 
        print("You win!")

    elif(computer ==-1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer ==1 and you == 0):
        print("You Win!")

    elif(computer ==0 and you == -1):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    else:
        print("Something went wrong!")