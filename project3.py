# Rock Papper Scissors 

# a=["hey this is me yoyegsh".split()]
# print(type(a))

import random

user_win=0
computer_win=0

op=["rock" ,"paper" ,"sciser"]
# print(type(op))

while True:
    user_input=input("Rock,pare,sciser or q for quit :").lower()
    if user_input=="q":
        break
    if user_input not in op:
        continue
    rangee=random.randint(0,2)

    computer=op[rangee]
    print("computer poicked",computer)

    if user_input =="rock" and computer=="sciser":
        print("you won")
        user_win=user_win+1
    
    elif user_input =="paper" and computer=="rock":
        print("you won")
        user_win=user_win+1
    
    elif user_input =="sciser" and computer=="paper":
        print("you won")
        user_win=user_win+1
    else:
        print("you lost")
        computer_win=computer_win+1
print("Thank You")




