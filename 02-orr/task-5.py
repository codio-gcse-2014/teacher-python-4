# Task 5
# Press the 'Run File' menu button to execute
# 
# 
import datetime
class customer:
    name=""
    appt=""
Jess=customer()
Jess.name="Jessica"
Jess.appt="Monday, 12pm"
print(Jess.name+" is expected "+Jess.appt)
#ext 1
that_office_girl=customer()
that_office_girl .name="Sheila"
that_office_girl .appt="Wednesday, 2pm"
print( that_office_girl.name+" is expected "+ that_office_girl .appt)

#ext 2
#let's generate some random customers
more_names=["Amir","Tamurinu","Alice","Tanya"]
week=["Monday","Tuesday","Wednesday","Thursday","Friday"]
#w= datetime.date.strftime('%A')
#print(w)
import random
#gen random appt time
def r_name():
    return more_names.pop(random.randint(0,len(more_names)-1))
def r_appt():
    r_day=week[random.randint(0,4)]
    r_time=random.randint(9,18)
    if r_time<12:
        return r_day+", "+ str(r_time) + " am"
    else:
        if r_time==12:
            return r_day+", "+ str(r_time) + " pm"
        else:
            return r_day+", "+ str(r_time-12) + " pm"
        
print("Testing random appointments generator")
for i in range(0,10):
    print(r_appt())

#random customer object
list_customers=[]
for i in range(0,4):
    temp=customer()
    temp.name=r_name()
    temp.appt=r_appt()
    list_customers.append(temp)

for j in list_customers:
    print (j.name,j.appt)
    
#Double Booking  - Code error?   
def dbl_book(new_cust):
    appt_times=[j.appt for j in list_customers]
    if new_cust.appt in appt_times:
        return new_cust.name,"double booked" 
print(dbl_book(new_cust))

