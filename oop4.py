class hospital:

    name ="lilawati"
    
    def fun1(self):
        
        return print(f"name of the hospital is {self.name} and doctor is {self.doctor}")

ronit = hospital()
ronit.doctor='padhale'
ronit.fun1()


class hotel:
    hname="expressIn"
    def fun2(self):
        return print(f"name of the best hotel is {self.hname} and chairman is {self.chairman}")

r1=hotel()
# r1.hname="gateway"
r1.chairman= "mr.Nayar"
r1.fun2()

class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good day")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")


amy = Employee()
amy.salary = 100000
amy.getSalary("Done") # Employee.getSalary(harry)
amy.greet() # Employee.greet()
amy.time()

