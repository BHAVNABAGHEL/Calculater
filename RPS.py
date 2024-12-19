import random
def rps():
    print("welcome to rock paper scissors")
    while True:
        choices= ["ROCK","PAPER","SCISSORS"]
        user_choice = input("choose Rock, paper or scissors:").upper()
        if user_choice not in choices:
            print("invalid choice")
            continue
        computer_choice=random.choice(choices)
        if user_choice==computer_choice:
            print("its a tie")
            print("computer choose :", computer_choice)
        elif(user_choice=="ROCK" and computer_choice=="SCISSORS")or (user_choice=="PAPER" and computer_choice=="ROCK") or (user_choice=="SCISSORS" and computer_choice=="ROCK"):
            print("you win")
            print("computer choose :", computer_choice)
            print("your choice",user_choice)
        else:
            print("computer wins")
            print("computer choose :", computer_choice)
            print("your choice",user_choice)
        
        play_again = input("Do you want to play more(yes/no):").lower()
        if play_again!="yes":
            print("thanks for playing")
            break
rps()
