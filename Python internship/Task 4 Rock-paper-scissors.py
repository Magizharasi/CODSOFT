import random
print("Game: Rock-Paper-Scissors\n")
game = ["Rock","Paper","Scissors"]
for i in game:
    print(i)
    
u_po = 0
c_po = 0

def play():
    global u_po,c_po
    y = input("\nEnter your Choice:")
    user = y.lower()
    x = random.choice(game)
    comp = x.lower()
    if user == "rock":
        if comp == "scissors":
            u_po+=1
            res = "You scored a point!"
        elif comp == "rock":
            res = "It's a tie."
        elif comp == "paper":
            c_po+=1
            res = "Computer scored a point!"
    elif user == "paper":
        if comp == "rock":
            u_po+=1
            res = "You scored a point!"
        elif comp == "paper":
            res = "It's a tie."
        elif comp == "scissors":
            c_po+=1
            res = "Computer scored a point!"
    elif user == "scissors":
        if comp == "paper":
            u_po+=1
            res = "You scored a point!"
        elif comp == "scissors":
            res = "It's a tie."
        elif comp == "rock":
            c_po+=1
            res = "Computer scored a point!"
    else:
        res = "Please give a propper input."
        play()
        
    print("User's choice:",user)
    print("Computer's choice:",comp)
    print("\n",res)
    
    def pl():
        again = input("\nDo you want to play again?(Yes/No):")
        if again.lower()=="yes":
            play()
        elif again.lower()=="no":
            print("\nScore:\nUser's Points =",u_po,"\nComputer's Points =",c_po)
            if u_po>c_po:
                print("\nYou won the Game! :)")
            elif u_po==c_po:
                print("\nThe points are equal and it's a Tie.")
            else:
                print("The computer Won the game and You lose. :(")
        else:
            print("\nPlease enter a propper input.")
            pl()
    pl()
play()
        

    
        
