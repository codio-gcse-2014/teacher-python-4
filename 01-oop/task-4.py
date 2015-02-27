# Task 4
# Press the 'Run File' menu button to execute
# 
cur_year=2014
class r:
    name="" #fields
    hobby=""
    yob=0
    __pin=0 #hidden field, don’t show your PIN to anyone!
    def __init__(self,iname,iyob):
        self.name=iname
        self.yob=iyob

    def age(self):
        return self.name+" is "+str(cur_year-self.yob)
    def report(self):
        return self.age()+" and his hobby is "+self.hobby+"."


p1=r("Bob",1980)
print(p1.age())
p1.hobby="diving"
print(p1.report())
p1.pin=1234
print(p1.pin)
#print(p1._p1__pin)

p2=r("Jack",1970)
p=[p1,p2]
print(p[0].name)
print(p[1].name)

d={123:p1,124:p2}
print(d[123].name)
print(d[124].name)

class v(r):
    is_from=""
    def say(self):
        print("I am visiting from",self.is_from)
v1=v("Ivan",1667)
v1.name="Ivan"
v1.yob=1986
v1.hobby="kayaking"
v1.is_from="Bulgaria"
v1.say()    