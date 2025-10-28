import random

class Game:
    def easy(self):
        if user_choice in option:
            print(f"\nYour choice : {user_choice}")
            if user_choice=="rock":
                print("My choice : scissor\n\nYou Win")
            elif user_choice=="paper":
                print("My choice : rock\n\nYou Win")
            elif user_choice=="scissor":
                print("My choice : paper\n\nYou Win")
        else:
            print("\nInvalid Option")

    def medium(self):
        if user_choice in option and my_choice in option:
            print(f"\nYour choice : {user_choice}")
            print(f"my choice : {my_choice}")
        
            if user_choice==my_choice:
                print("\nTie!")
                
            elif user_choice=="rock":
                if my_choice=="paper":
                    print("\nYou Lose")
                else:
                    print("\nYou Win")
                    
            elif user_choice=="paper":
                if my_choice=="scissor":
                    print("\nYou Lose")
                else:
                    print("\nYou Win")
                    
            elif user_choice=="scissor":
                if my_choice=="rock":
                    print("\nYou Lose")
                else:
                    print("\nYou Win")
        else:
            print("\nInvalid Option")

    def hard(self):
        if user_choice in option:
            print(f"\nYour choice : {user_choice}")

            if user_choice=="rock":
                print("My choice : paper\n\nYou Lose")
            elif user_choice=="paper":
                print("My choice : scissor\n\nYou Lose")
            elif user_choice=="scissor":
                print("My choice : rock\n\nYou Lose")
        else:
            print("\nInvalid Option")

RPS = Game()

option = ["rock","paper","scissor"]

print("Rock Paper Scissor Game!")

user = input("\nDo you want to play (yes/no) : ").lower()

while user=="yes":
    my_choice = random.choice(option)
    
    mode = input("\nSelect Mode (easy / medium / hard) : ").lower()
    
    if mode not in ["easy","medium","hard"]:
        print("\nInvalid Mode")
    else:
        user_choice = input("Choose anyone (rock / paper / scissor) : ")
    
    if mode=="easy":
        RPS.easy()
    elif mode=="medium":
        RPS.medium()
    elif mode=="hard":
        RPS.hard()

    user = input("\nDo you want to continue (yes/no) : ")

    if user=="yes":
        pass
    elif user=="no":
        break
    
if user not in ["yes","no"]:
    print("\nInvalid Input")
else:    
    print("\nThank You")
