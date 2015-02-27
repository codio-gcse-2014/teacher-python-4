# Task 2
# Press the 'Run File' menu button to execute
#

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

#let's generate some random customers
more_names=["Amir","Tamurinu","Alice","Tanya"]
week=["Monday","Tuesday","Wednesday","Thursday","Friday"]
import random
#gen random appt time
def r_appt():
    return week[random.randint(0,4)]+", "+ random.randint(9,18)
  
import random
#gen random appt time
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