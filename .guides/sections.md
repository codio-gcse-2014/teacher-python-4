---
title: Object Oriented Programming
files: []
layout: 3-cell-tree
step: 01-oop

---
Objects are complex variables that can contain other variables, lists, both known as “attributes”, and even their own subprograms and functions (these are called methods). 

Objects shorten the amount of code needed to perform repeating tasks. An object is defined with a class statement and is “instantiated” with its first method, usually called `__init__`. Note the DOUBLE underscores before and after the name of this “constructor” method. 

Objects can be reused in many programs, so it is possible that some of the object’s attributes will have the same name as a variable in a program where it is used. 

To avoid confusion, all of the object’s attributes are preceded by the word “self.” E.g. self.value. To hide (encapsulate) the values of internal variables/attributes from the rest of the program, we can put an underscore in front of its name.

## Task 1
The simplest full class with attributes and methods:

Click to open task file : [task-1.py](open_file "01-oop/task-1.py").

Run the program by pressing the 'Run File' button in the top menu.

Which should output something along these lines:
```
2
```

## Task 2
Methods can be either subs or functions.

Modify the code so `roll()` is not a sub but a function.

Click to open task file : [task-2.py](open_file "01-oop/task-2.py").

## Task 3
What is the need for the additional complexity? We could have got the result without OOP. However, OOP “scales better” – when the number of dice increases we start saving time and code:

Objects are handy in games where there are many characters of similar type. E.g. in a fantasy game, all orcs, trolls, dragons will be written out as objects (templates of sorts) which will contain their attributes (strength, position, name) and methods (fly, fight, buy). 

Even in our simple dice game, we might have two players, so we can recycle the code we wrote for our first player and apply it to the other with just two lines of code.

Click to open task file : [task-3.py](open_file "01-oop/task-3.py").

Run the program by pressing the 'Run File' button in the top menu.

Which should output something along these lines:

```python
I lose, 2 vs 5
```
## Task 4
We have discussed using nested lists for record structures in databases. 

However, OOP allows us more sophisticated ways of dealing with records. 

For example, `my_record.validate` can be a powerful method that is written once and can be triggered for all the records in a database without additional coding.
Most of the time, however, objects store records about people and assets. 

Consider this program which stores 4 items of data data about people:
```python
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
```

Click to open task file : [task-4.py](open_file "01-oop/task-4.py").

Run the program by pressing the 'Run File' button in the top menu.

Which should output:

```python
Bob is 34
Bob is 34 and his hobby is diving.
1234
Bob
Jack
Bob
Jack
I am visiting from Bulgaria
```

**Extension:** add more people and implement user input of new people.

## Task 5
Adding functionality – we will now have two classes – one for residents, the “r” class, and another class for visitors, the “v” class. They will share some properties but will be different in others. This is known as polymorphism

Click to open task file : [task-5.py](open_file "01-oop/task-5.py").

Run the program by pressing the 'Run File' button in the top menu.

Which should output:

```python
Bob is 34
Bob is 34 and his hobby is diving.
1234
I lived right here all me life.
Bob
Jack
Bob
Jack
Object has no such attribute or method
I am visiting from Germany
Otto is 27 and, back in his country, his hobby is skating.
I have a citizenship of Germany

```
---
title: Objects as replacements for records.
files:
  - action: close
    path: "#tabs"
layout: ""
step: 02-orr

---
## Task 1

This program keeps track of hair salon appointments.


Click to open task file : [task-1.py](open_file "02-orr/task-1.py").

Run the program by pressing the 'Run File' button in the top menu.

Which should output:
```python
Jessica is expected Monday, 12pm
Sheila is expected Wednesday, 2pm
```

## Task 2
**Extension:** random appointment times for testing:


Click to open task file : [task-2.py](open_file "02-orr/task-2.py").

Run the program by pressing the 'Run File' button in the top menu.

Which should output something similar to:
```python
Jessica is expected Monday, 12pm
Sheila is expected Wednesday, 2pm
Testing random appointments generator
Tuesday, 10 am
Wednesday, 3 pm
Tuesday, 4 pm
Tuesday, 10 am
Monday, 4 pm
Monday, 11 am
Thursday, 6 pm
Wednesday, 9 am
Thursday, 12 pm
Tuesday, 1 pm
```
## Task 3

We can do further testing by generating a list of customer objects with names and appointment times randomly generated.


Click to open task file : [task-3.py](open_file "02-orr/task-3.py").

Run the program by pressing the 'Run File' button in the top menu.

Which should output something similar to:
```python
Jessica is expected Monday, 12pm
Sheila is expected Wednesday, 2pm
Testing random appointments generator
Wednesday, 6 pm
Thursday, 9 am
Tuesday, 1 pm
Thursday, 4 pm
Tuesday, 3 pm
Monday, 10 am
Tuesday, 9 am
Friday, 2 pm
Tuesday, 6 pm
Monday, 11 am
Tamurinu Monday, 4 pm
Alice Thursday, 1 pm
Amir Thursday, 11 am
Tanya Thursday, 3 pm
```
## Task 4

Double booking is an issue, let’s address this problem.
We need to generate a list of times:
```python
def dbl_book():
    appt_times=[j.appt for j in list_customers]
    return appt_times
print(dbl_book())
```

Click to open task file : [task-4.py](open_file "02-orr/task-4.py").

Run the program by pressing the 'Run File' button in the top menu.

Which would append something similar to:
```python
['Monday, 4 pm', 'Wednesday, 6 pm', 'Wednesday, 11 am', 'Monday, 5 pm']
```
## Task 5

Now, we can modify our function to iterate through the list of existing appoints (generated off the main list) and compare with “new customer’s” appointment time, reporting if double-booked and the new appointment time is already in the list.

```python
def dbl_book(new_cust):
    appt_times=[j.appt for j in list_customers]
    if new_cust.appt in appt_times:
        return new_cust.name,"double booked" 
print(dbl_book(sister))
```

Click to open task file : [task-5.py](open_file "02-orr/task-5.py").

Run the program by pressing the 'Run File' button in the top menu.
**Code error?** 
Which should output something similar to:

## Task 6

This program simulates a group of Blackjack players. It showcases the wonderful ability of object-oriented programming to “scale up” – it takes almost no additional code to implement a group of players compared with just one player. Write once, use a lot!


Click to open task file : [task-6.py](open_file "02-orr/task-6.py").

Run the program by pressing the 'Run File' button in the top menu.

Which should output something similar to:
```python
Enter player1's name, or hit <Enter> for default names: 
Enter player2's name, or hit <Enter> for default names: 
Ismail played: [9, 3, 4] vs:  Mary played: [2, 3, 3]
Ismail 16 vs:  Mary 8
Ismail  won
Play again: type 'y'? y
Enter player1's name, or hit <Enter> for default names: Jack
Enter player2's name, or hit <Enter> for default names: Martha
Jack played: [11, 6, 4] vs:  Martha played: [3, 3, 8]
Jack 21 vs:  Martha 14
Jack  won
Play again: type 'y'? n
bye!
```

