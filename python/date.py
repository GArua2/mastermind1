        ##Importing Date module
import datetime
import time
from datetime import date

today=date.today()
print("Date:",today)
print("Day:",datetime.date.today().strftime("%a"))

day=time.strftime("%a")
week = set(["Mon","Tue","Wed","Thur","Fri"])
Sat = set(["Sat"])
Sun = set(["Sun"])

if day in week:
    print("Fare: 300")
elif day in Sat :
    print("Fare: 120")

elif day in Sun:
    print("Fare: 90")