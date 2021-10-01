#A program that helps student to calculate their cummulative grades
#To assist student in determining their performance for the semester

from math import*
import sys


def student_grade():
     Student_name = input("Enter your name: ")
     print(f"You are welcome {Student_name}!!!")
     print()
     view = input("Do you want to input your grades? (yes/no): ")
     y = "yes"
     n = "no"

     if view == y:
          print("Loading Data.......")
          print()

     else:
          sys.exit()

     English_score = int(input("Enter grade for English: "))
     if English_score > 80:
          print("A grade! ")

     elif English_score > 70:
          print("B grade! ")

     elif English_score > 55:
          print("C grade! ")

     else:
          print("fail! ")
     Maths_score = int(input("Enter grade for Maths: "))
     if Maths_score > 80:
          print("A grade! ")

     elif Maths_score > 70:
          print("B grade! ")

     elif Maths_score > 55:
          print("C grade! ")

     else:
          print("fail! ")
     Biology_score = int(input("Enter grade for Biology: "))
     if Biology_score > 80:
          print("A grade! ")

     elif Biology_score > 70:
          print("B grade! ")

     elif Biology_score > 55:
          print("C grade! ")

     else:
          print("fail! ")
     Geography_score = int(input("Enter grade for Geography: "))
     if Geography_score > 80:
          print("A grade! ")

     elif Geography_score > 70:
          print("B grade! ")

     elif Geography_score > 55:
          print("C grade! ")

     else:
          print("fail! ")
     Physics_score = int(input("Enter grade for Physics: "))
     if Physics_score > 80:
          print("A grade! ")

     elif Physics_score > 70:
          print("B grade! ")

     elif Physics_score > 55:
          print("C grade! ")

     else:
          print("fail! ")
     Economics_score = int(input("Enter grade for Economics: "))
     if Economics_score > 80:
          print("A grade! ")

     elif Economics_score > 70:
          print("B grade! ")

     elif Economics_score > 55:
          print("C grade! ")

     else:
          print("fail! ")

     print()
     print("Loading........")
     Total_score = English_score + Maths_score +  Biology_score + Geography_score + Physics_score + Economics_score
     Commulative_score = 600
     if Student_name == Student_name:
          print(f" You scored {Total_score} / {Commulative_score}")

     else:
          print("Invalid response! ")
     print()
     print("Grade loading.......")
     if Total_score == Commulative_score:
          print("Excellent Result! ")

     elif Total_score > 450 < Commulative_score:
          print("A good result! ")

     elif Total_score > 350 < 450:
          print("An average result! ")

     else:
          print("You fail, Do better next time! ")

print(student_grade())