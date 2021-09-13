class raliway:
    # class attribute 
    company ="indian railways"
    employees = 115000

    def forp(self):
        print(f'name of the train is {self.name}')
        print(f'number of train is {self.number}')
        print(f'number of employees is {self.employees}')
       
# object instantiation    
objinst = raliway()

# isinstance attribute    
objinst.name =  "rajdhani express"
objinst.number = 579634
objinst.company ="Bhartiya raliways"
objinst.record = "1000"
objinst.employees = "2222"
print(raliway.company)
raliway.company="air force" #changing class attribute
print(raliway.company)
# printing 
objinst.forp()  # function calling

print(objinst.company)
print(raliway.company)
print(raliway.employees)
print(objinst.record)   