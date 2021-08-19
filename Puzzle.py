from math import*
import sys
def puzzle():
    print("You are Welcome! ")
    print()
    print("Loading....")
    print()
    answer = input(" Do you want to play a game? (yes/no): ")
    y = "yes"
    n = "no"

    if answer == y:
        print("Start Game!!!!")
        print()

    else:
        sys.exit()

    numb1 = 3
    numb2 = int(input("Enter a number: "))
    numb3 = 14
    numb4 = 1
    numb5 = 4
    if numb1 + numb2 == numb3:
        print("Nice one!")
        print("continue....")
        print()

    else:
        sys.exit("You lose! ")

    numb6 = numb1 + numb4
    numb7 = int(input("Enter a number: "))
    numb8 = numb6 * numb5

    if numb3 + numb7 == numb8:
        print("Keep it up! ")
        print()

    else:
        sys.exit("You lose! ")

    print("Level 2")
    print("Loading....")
    print()

    numb9 = int(input("Enter a number: "))
    numb10 = 12
    numb11 = 17
    numb12 = 8

    #numb5 = 4
    if numb5 * numb9 == numb10:
        print("Nice! ")
        print()

    else:
        sys.exit("You lose! ")


    numb13 = 3
    numb14 = numb13 + numb11
    numb15 = numb10 - numb12
    numb16 = int(input("Enter a number: "))

    if numb14 / numb16 == numb15:
        print("Hurray....")
        print()

    else:
        sys.exit("You lose! ")

    answer1 = input("Do you want to continue? (yes/no): " )

    if answer1 == y:
        print("Loading....")
        print()
        print("Level 3 ")
        print("Start!!! ")
        print()

    else:
        sys.exit()

    numb17 = 2
    numb18 = 5
    numb19 = 10
    numb20 = 45
    numb21 = numb18 + numb19
    numb22 = int(input("Enter a number: "))

    if numb21 * numb22 == numb20:
        print("You are almost there!!!!")
        print("continue....")
        print()

    else:
        sys.exit("You lose! ")

    numb23 = 2
    numb24 = numb23 * numb17
    numb25 = numb18 + numb24
    numb26 = int(input("Enter a number: "))

    if numb25 * numb26 == numb20:
        print("Keep it up....")
        print()

    else:
        sys.exit("You lose! ")

    numb27 = int(input("Enter a number: "))
    numb28 = numb26 - numb27
    numb29 = 6
    numb30 = numb29 / numb28
    numb31 = 5
    numb32 = 15

    if numb32 / numb31 == numb30:
        print("You are almost done, don't give up yet!!!!!!")
        print()

    else:
        sys.exit("You lose! ")

    #numb12 = 8

    numb33 = int(input("Enter a number: "))
    numb34 = numb12 + numb33
    numb35 = numb34 + numb29

    if numb35 == numb32:
        print("continue....")
        print()

    else:
        sys.exit("You lose! ")

    numb36 = int(input("Enter a number: "))

    if numb35 * numb36 == numb32:
        print()
        name = input("What is your name: ")
        print(f"Congratulation, You won {name}!!!")
        print()
            
    else:
        sys.exit("You lose! ")


print(puzzle())

again = input("Do you want to play again? (yes/no): ")
y = "yes"
n = "no"
if again == y:
    print(puzzle())
else:
    sys.exit()