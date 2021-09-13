# class sports:
#     game = "cricket"

#     def __init__(self, name, game, value):
#         self.name=name
#         self.game=game
#         self.value=value

#     def details(self):
#         print(f"name of the player is {self.name}")  
#         print(f"game of the player is {self.game}")
#         print(f"value of the player is {self.value}")  

# rohit =sports("sunil chetri","football",150)
# rohit1 =sports("virat kohli","cricket",140)
# rohit.details()        
# rohit1.details()

class employee:
    company = "adobe"

    def __init__(self, name, prod, sal):
        self.name = name
        self.product=prod
        self.salary = sal

    def getinfo(self):
        print(f"name of the employee {self.name} and product is {self.product} sand salary {self.salary}")

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")
    

cali=employee("robin","antivirus", 10000)

cali.getinfo()
cali.getSalary("sign")
