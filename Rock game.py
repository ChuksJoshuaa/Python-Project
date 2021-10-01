import random
import sys


print("You are welcome!!!")
print()
start = input("Do you want to play game? (yes/no):")

if start == "yes" or start == "Yes":
    print("Level 1")
    print()

else:
    sys.exit()

print("Choose between Rock, Paper, Scissors? ")

count = 0
count_limit = 3

while count < count_limit:
    user = input("Choose One: ")
    cpu_choice = ["Rock", "Paper", "Scissors"]
    cpu = random.choice(cpu_choice)
    if user == cpu:
        print("Tie!!")
        count += 1
    elif user == "Scissors" or user == "scissors" and cpu == "Rock" or cpu == "rock":
       print("Cpu win!!")
       count += 1
    elif user == "Rock" or user == "rock" and cpu == "Paper"  or cpu == "paper":
        print("Cpu win!!")
        count += 1
    elif user == "Paper" or user == "paper" and cpu == "Scissors" or cpu == "scissors":
        print("Cpu win!!")
        count += 1
    elif cpu == "Scissors" or cpu == "scissors" and user == "Rock" or user == "rock":
         print("User win!!")
         count += 1
    elif cpu == "Rock" or cpu == "rock" and user == "Paper" or user  == "paper":
        print("User win!! ")
        count += 1
    elif user == "Paper" or user == "paper" and cpu == "Scissors" or cpu == "scissors":
        print("User win!!")
        count += 1
    elif cpu == "Scissors" or cpu == "scissors" and user == "Scissors" or user == "scissors":
         print("User win!!")
         count += 1
    else:
        sys.exit()

