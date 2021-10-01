from math import*
import sys

print("You are welcome! ")
print()
quest = input("Do you want to order a package?(yes/no): ")

if quest == "yes" or "Yes":
    print("Start!!! ")

else:
    sys.exit("Logging out!! ")

ans = input('Choose between the air or freight mode of transportation: ')
air1 = 0.36
a = "air1"
freight1 = 0.25
f = "freight"

if ans not in a:
    aa = dict(freight_cost= freight1 )

else:
    aa = dict(air_cost=air1)
print(aa)
print()


c = "full_insurance1"
full_insurance1 = 50.00
d = "limited_insurance"
limited_insurance1 = 25.00
answer1 = input("Do you want full_insurance or limited_insurance: ")
if answer1 not in c:
    bb = dict(limited_cost=limited_insurance1)
else:
    bb = dict(full_cost=full_insurance1)
print(bb)
print()
answer2 = input("Do you want gift or no: ")
gift = 15.00
g = "gift"
no = 0
if answer2 not in g:
    cc = dict(no_gift_cost=no)
else:
    cc = dict(gift_cost=gift)
print(cc)
print()


answer3 = input("Do you want priority or standard_delivery: ")
priority = 100.00
p = "priority"
standard_delivery = 20.00
s = "standard_delivery"
if answer3 not in p:
    dd = dict(standard_cost=standard_delivery)
else:
    dd = dict(priority_cost=priority)
print(dd)
print()
distance = input("Enter the total distance of the delivery:  ")
print()
aa.update(bb)
cc.update(aa)
dd.update(cc)
total_score = dd.values()
ii = sum(total_score)
print(f"The total package cost is: {ii} dollars")




