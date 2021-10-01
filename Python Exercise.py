#A simple pdfreader

import pyttsx3
import PyPDF2

book = open("Text.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(7)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()

#using audiobook for wikipedia

import pyttsx3
import wikipedia

person = "Enter a name:"
info = wikipedia.summary(person, 5)
print(info)
speaker = pyttsx3.init()
speaker.say(info)
speaker.runAndWait()


#find location using ipaddress:
import pygeoip

Location = pygeoip.GeoIP("GeoLiteCity.dat")
res = Location.record_by_addr("197.210.44.144")
for key, val in res.items():
    print("%s : %s" % (key, val))


#Guess a number using random:
import random
import pyttsx3
print("You are welcome Mr chuks")
random_numb = int(input("Enter a random number from 1 to 5: "))
A = random.randint(1, 5)
if A == random_numb:
    speaker = pyttsx3.init()
    speaker.say("You win")
    speaker.runAndWait()
else:
   speaker = pyttsx3.init()
   speaker.say("you lose")
   speaker.runAndWait()

#finding sum/product
numb1 = int(input("Enter your first integer: "))
numb2 = int(input("Enter your second integer: "))
product = numb1 * numb2
sum = numb1 + numb2

if product >= 1000:
    print(sum)

else:
    print(product)

#even word indention
name = "pynative"

A  = name[0:8:2]

for i in A:
    print(i)

#divisable by 5

numb1 = [2, 5, 9, 10, 15, 20, 50, 30]
for num in numb1:
    if (num % 5 == 0):
        print(num)



#Everything about calendar

import datetime
import pytz
import DateTime

today = datetime.date.today()
print(today)

tdelta = datetime.timedelta(days=15)

A = today + tdelta
print(A)
print(today.day)
print(today.weekday())

datetime_today = datetime.datetime.now(pytz.UTC)
print(datetime_today)

datetime_pacific = datetime_today.astimezone(pytz.timezone("Africa/lagos"))
print(datetime_pacific)

#for tz in pytz.all_timezones:
    #print(tz)


datetime_thing = datetime_pacific.strftime("%B %d, %y")
print(datetime_thing)

datetime_ping = datetime.datetime.strptime('June 10, 2021', '%B %d, %Y')
print(datetime_ping)

#pyramid question

space = 5

for i in range(1,10,2):
    space = space-1

    print(" "*space+"*"*i)

#2 pyramid question

def pattern(n):
    k = 2 * n - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print(" *", end=" ")
        print("\r")

pattern(10)

#inverse pyramid
def pattern(n):
    k = 2 * n - 2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")

        k = k + 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print("\r")

pattern(10)


#star pyramid

for i in range(5):
    for j in range(5):
        if i + j == 2 or i - j == 2 or i + j == 6 or j - i  == 2:
            print("*", end="")
        else:
            print(end=" ")
    print()


#number pyramid
def pattern(n):
    x = 0
    for i in range(0,n):
        x += 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("\r")

pattern(10)

from math import*
numb1 = int(input("Enter x: "))
numb2 = int(input("Enter y: "))
numb3 = int(input("Enter z: "))

a = sqrt((numb1 ** 2) + (numb2 ** 2) + (numb3 ** 3))
b = numb2 ** (1/numb1)
c = numb1 ** (1/numb2)
d = numb3 ** (1/numb3)
e = b - c + d
f = e / a
g = f ** (1/3)


print(g)


from functools import reduce

#map function to add a list function by iteslf
def new(a):
    return a + a
x = map(new,[1, 2, 4, 3, 5, 6, 7, 8])

print(list(x))

#map function to add a list function by x + 4
def new():
    x = map(lambda x: x + 4, [3, 4, 5, 6, 7])
    return list(x)

print(new())

#to filter the list function that is greater than 5
def new():
    x = filter(lambda x: x>=5, [4, 5, 6, 7, 8, 6,10, 11])
    return list(x)

print(new())

#to reduce a list fucntion to add and give it initial result
#Note you do not need to put the list(x) when returning the fucntion

def new():
    x = reduce(lambda x,y: x+y, [3, 4, 5, 6, 7, 8, 9])
    return x
print(new())

#to use both the map and filter function together

def new():
    x = map(lambda x: x * 4, filter(lambda x: x<=3, [3, 2, 4, 5, 1]))
    return list(x)

print(new())


#factorial of a number (n!)

def new(num):
    if num == 1:
        return num
    else:
        return num * new(num - 1)

print(new(9))


#fabonnaci series
from timeit import default_timer as timer
start = timer()
a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
n = int(input("Enter the number of element: "))

print(a, b, end=" ")

while n - 2:
    c = a+b
    a = b
    b = c
    print(c, end=" ")
    n = n - 1
stop = timer()

#armstrong number

num = int(input("Enter a number: "))
s = 0
temp = num

while temp > 0 :
     c = temp % 10
     s += c ** 3
     temp //= 10

if num == s:
     print("armstrong number! ")

else:
     print("Not armstrong number! ")


numb1 = input("Enter a first digit: ")
numb2 = input("Enter a second digit: ")
numb3 = input("Enter a third digit: ")

a = numb1 + numb2 + numb3
#print(a)

b = int(numb1) ** 3
c = int(numb2) ** 3
d = int(numb3) ** 3

r = b + c + d
#print(r)

if int(a) == r:
   print("Armstrong number! ")

else:
    print("Not armstrong number! ")

 #lear year

numb1 = int(input("Enter a year: "))

if numb1 % 400 == 0:
    print("Leap year! ")

elif numb1 % 100 == 0:
    print("not a leap year! ")

elif numb1 % 4 == 0:
    print("Leap year! ")


else:
    print("Not a leap year")



#Using the counter function to find how many times a number occur

from collections import Counter

g = ["Jake", "Teni", "Jake", "Teni", "Jake", "chima", "john", "john"]
my_counter = Counter(g)
List1 = my_counter.most_common(1)[0][1]

#using named tuple to indicate the x and y value
# always include something in the namedtuple
from collections import namedtuple

list1 = namedtuple("point", "x,y")
pt = list1(1, 3)

#using default to form a set
# defaultdict also function as the Ordereddict
from collections import defaultdict

default = defaultdict()

default["a"] = 4
default["b"] = 10
default["c"] = 6
default["d"] = 5
default["e"] = 1

print(default)

# to use the depue function
from collections import deque

list1 = {1, 2, 3, 4, 5, 6}
list2 = deque(list1)
list2.popleft()
list2.appendleft()

# itertools product, permutations, combinations, combination_wth_replacement, accumulate

from itertools import product

a = [1, 2, 8]
b = [3, 4, 6]
c = [5]

prod = product(a, b, c)
e = list(prod)
print(e)


#----------------------
from itertools import accumulate
import operator
a = [1, 2, 3, 4, 5, 6]
print(a)
acu = accumulate(a, func=operator.sub)
print(list(acu))
#...................................
from itertools import groupby
def smaller_than_3(x):
    return x > 3

a = [1, 2, 3, 4, 5, 0]

group = groupby(a, smaller_than_3)

for key, value in group:
    print(key, list(value))

#..............................
# to create infinity
from itertools import count, cycle, repeat

for i in count(100, 1000):
    print(i)
    if i == 10000:
        break


#..............................
# Title is Sum.py
class Valuetoomuch(Exception):
    pass

#from Sum import Valuetoomuch

class Valuetoosmall(Valuetoomuch):
    pass

def value(x):
    if x > 400:
       raise Valuetoomuch

    elif x < 200:
        raise Valuetoosmall

    else:
        return False

try:
    value(int(input("Enter a number: ")))

except Valuetoosmall as e:
    print(e, "value too small fool")

except Valuetoomuch as e:
      print(e, "value too high fool")


#...........TO log in files

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s,: %(levelname)s,: %(message)s")

file_handler = logging.FileHandler("school.log")
logger.addHandler(file_handler)
file_handler.setFormatter(formatter)

#basic logging file
logging.basicConfig(filename="school.log", level=logging.INFO, format="%(asctime)s,: %(levelname)s,: %(message)s")


name = input("Enter your school: ")
school = "Jocarine"

if name == school:
    logging.info("True")

else:
    logging.info("False")

if len(school) > len(name):
    logging.info("Yes")

else:
    logging.info("No")

#>>>>>>>>>>>>>>>>>>>>>>>ADVANCED LOGGING

class ValueError(Exception):
    pass
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s,: %(levelname)s,: %(message)s")

file_handler = logging.FileHandler("school.log")
# you can use the file_handler. setlevel(logging.ERROR) to indicate if there is error in the program
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
#now we use the stream handler to indicate the solution to the console down below
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


name = input("Enter your school: ")
school = "Jocarine"

if name == school:
    logger.info("True")

else:
    logger.info("False")


if len(school) > len(name):
    logger.info("Yes")

else:
    logger.info("No")

def new(x):
    if x > 20:
        return x

    else:
        logger.exception(ValueError)
try:
    new(11)

except ValueError:
    logger.exception("Value is too small")


# how to import html file in python

import webbrowser
# i named the project to be "main.html"
f = open("main.html", "r+")
message = """<html>
<body>
   <div>
   <p>n = 1000000</p>
   <p>numb1 = 10</p>
   <p>numb2 = 3</p>
   <hr>
   </div>
   <div>
      <p>numb = list(range(1, n)) </p>
         <p>print(numb)</p>   
         <hr>
   </div>
   <div>
    <p> for i in range(1, n, numb1): </p>
       <strong>print(i)</strong>
       <hr>
   </div>
   <div>
     <p> for i in range(1, n, numb2): </p>
        <p><i>print(i)</i></p>
        <hr>
   </div>
   <div>
      <p> a = 2 </p>
      <p> b = 1000000 </p>
      <p>for i in range(a, b+1):</p>
            <p> if i > 1: </p>
               <p>for j in range(2, i):</p>
                    <p>if i % j == 0:</p>   
                            <p>break</p>    
             <p> else: </p>
                <p><u>print(i)<u></p>
   </div>
</body>


</html>"""


f.write(message)
f.close()

webbrowser.open_new_tab("main.html")














