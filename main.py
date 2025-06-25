#imported functions
from show import display 
from structure import structure_of_game as sg
from structure import insert
from verify_winner import verify
import string as st

#basic user interface
for i in range(100):
    print("#",end="")
print(" ")
print("Hello , welcome to the game.")
print(" ")
print("This is two player game and both will play side by side.")
print(" ")
start = input("Press y to start the game : ").lower() 

#begning of game
if start == 'y': 
    print("Let's Begin")  
    arr = sg()
    print("game is started.Now just remember First turn is of X and secons is of O.")
    for i in range(100):
        print("#",end="")
    print(" ")
    display(arr)
    turn = 1
    while True: 
        res = verify(arr) 
        if turn >= 10: 
            print("Match is draw")
            break;
        if res == True:
            break
        if turn%2 == 0: y_turn,x_turn = True,False   
        else: y_turn,x_turn = False,True
        if(x_turn): print("X-Turn")
        else : print("O-turn") 
        pos = input("Enter the position between 1-9 : ")
        if(pos.isdigit() and int(pos) in range(1,10)):
            check = insert(int(pos),x_turn,y_turn,arr)
            if check:
                display(arr)
                turn+=1 
        else: 
            print("Invalid position.Try again")        
else: 
    print("thankyou for download...")