# Task 5
# Press the 'Run File' menu button to execute
# 

cur_year=2014 #global variable
class r: #first class definition for residents
    name=""
    hobby=""
    yob=0
    __pin=0

    def __init__(self,iname,iyob):
        self.name=iname
        self.yob=iyob
        
    def age(self):
        return self.name+" is "+str(cur_year-self.yob)

    def report(self):
        return self.age()+" and his hobby is "+self.hobby+"."

    def what_is_your_nationality (self): #makes sense for residents
        print("I lived right here all me life.")

#once our class is defined, we instantiate a lot of objects from this #class/template and fill them with data.
    
p1=r("Bob",1980) #p1 stands for “person 1”
print(p1.age())
p1.hobby="diving" #hopefully, while not playing football ;)
print(p1.report())
p1.pin=1234
print(p1.pin)
#print(p1._p1__pin)
p1.what_is_your_nationality()

p2=r("Jack",1970) #another resident, person 2

p=[p1,p2] #starting to show the power of objects – we put both of these #people into a list, we can now access each of their attributes by #calling a list element by its [index] and then with a dot notation, we #can access their attributes.
print(p[0].name)
print(p[1].name)

d={123:p1,124:p2} #even more clever: we set up a dictionary, where the two keys #are 123 and 124, and the two values are p1 and p2. We compressed the #whole range of data about these people into one reference in a #dictionary. This is getting very close to how databases work.

print(d[123].name) #accessing dictionary elements by key
print(d[124].name)

try:  #validation/error prevention
    print(d[123].name+" is not from "+d[124].is_from)
except:
    print("Object has no such attribute or method")
    
class v(r): #our visitor class
    is_from="" #this is unique to this class
    def say(self):#this method is also different from residents
        print("I am visiting from",self.is_from)
    #polymorphism for other methods, too
    def report(self):
        return self.age()+" and, back in his country, his hobby is "+self.hobby+"."
    def what_is_your_nationality(self):
        print("I have a citizenship of",self.is_from)

   
#Instantiating an instance of our visitor class.
v1=v("Otto",1987)
v1.hobby="skating"
v1.is_from="Germany"   
v1.say()    
print(v1.report())
v1.what_is_your_nationality ()
