# Task 5
# Press the 'Run File' menu button to execute
#

names=["Bob","Mary","Ismail","Nuringa"]
class player():
    clist=[]
    pNum=0

    def __init__(self,pNum):
        self.clist=[]
        self.pNum=pNum
        tempName= input("Enter player"+str(pNum)+"'s name, or hit <Enter> for default names: ")
        if len(tempName)>0:
            self.name=tempName
        else:
            import random
            if len(names)>0:
                self.name=names.pop(random.randint(0,len(names)-1))
            else:
                self.name="Player "+str(self.pNum)

    def draw(self):
        import random
        temp=random.randint(2,11)
        self.clist.append(temp)

    def getTotal(self):
        #return self.clist
        return sum(self.clist)

def overdrawn(pl):
    return pl.getTotal()>21

def whoWins(pl1,pl2):
    if overdrawn(pl1) and not(overdrawn(pl2)):
        return pl2.name
    elif (overdrawn(pl1) and (overdrawn(pl2))) or (pl1.getTotal()==pl2.getTotal()):
        return "draw"
    elif overdrawn(pl2) and not(overdrawn(pl1)):
        return pl1.name
    elif pl1.getTotal()> pl2.getTotal():
        return pl1.name
    else:
        return pl2.name
#main program
plagain='y'
while plagain=='y':
    plagain
    p1=player(1)
    p2=player(2)
    for i in range(3):
        p1.draw()
        p2.draw()

    print(p1.name,"played:",p1.clist,"vs: ", p2.name,"played:", p2.clist)
    print(p1.name,p1.getTotal(),"vs: ",p2.name,p2.getTotal())
    if whoWins(p1,p2)!="draw":
        print(whoWins(p1,p2), " won")
    else:
        print("It's a draw")
    plagain=input("Play again: type 'y'? ")
print("bye!")