sinle inheritance
class car:
    type="sedan"

    def info(self):
        print(f"This is a {self.type} car information")

class truck(car):
    type ="hpm"

    def gettype(self):
        print(f"type of vehical {self.type}")

ecar=car()
ecar.info()
p=truck()
p.gettype()
p.info()

class doctor:
    type="orthologist"

    def fun(self):
        print(f"doctors who are knowledge about bones are {self.type}")

class doc(doctor):
    # type="neuro"

    def funcname(self):
        print(f"{self.type} doctors has a knowledge about central nervous system")
            

d=doctor()
d2=doc()
d.fun()
d2.funcname()
d2.fun()
print(d2.type)

