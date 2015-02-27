# Task 1
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