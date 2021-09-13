class calculator:

    def __init__(self, number):

        self.num = number
        
    def square(self):
        print(f"square of the number {self.num} is {self.num**2}")

    def cube(self):
        print(f"cube of the number {self.num} is {self.num **3}")

    def squareRoot(self):
        print(f"square root of the number {self.num} is {self.num **0.5}")

    @staticmethod
    def fun():
        print("*******this is a working calculator**********")        

cal=calculator(3)
cal.fun()
cal.square()
cal.cube()
cal.squareRoot()                 

# class books:
#     def bk1(self):
#         print(f"type of the book is {self.type}")

# emp = books()
# emp.type="novel"
# emp.bk1()


