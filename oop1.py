class raliway:
    # class attribute 
    company ="indian railways"  
    def forp(self):
        print(f'name of the train is {self.name}')
        print(f'number of train is {self.number}')
       
# object instantiation    
objinst = raliway()

objinst.name =  "rajdhani express"
objinst.number = 579634
# isinstance attribute    
objinst.company ="Bhartiya raliways"

print(objinst.company)
print(raliway.company)
objinst.forp()
