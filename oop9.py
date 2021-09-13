# multiple inheritance
class developer:
    company = "tcs"
    level = 0

    def upgrade(self):
        self.level= self.level +1

class employee:

    def upgrade(self):
        print("this is 2nd upgrade")
    
    company="mahindra"
    code =123

class program(employee, developer):
    name="amit"
 

k=program()
k.upgrade()
print(k.company)        


# multilevel inheritance




