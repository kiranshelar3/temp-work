# def greet(name ="starnger"):
#     g= print("namaste"+ name)
#     return g

# greet() 
# greet("krishna") 


# l = [1,8,9,4]
# for item in l:
#     if item ==9:
#         continue

#     print(item)

def percent(marks):

    p=(marks[0] + marks[1] + marks[2] + marks[3])/400
    q =p*100
    return q

marks1=[78 ,89, 50, 45]
fun1 =percent(marks1)   
print(fun1)

marks2 =[28,89,45,16]
fun2= percent(marks2)
print(fun2)


def bookticket(ticket):
    if ticket >1:
        print(f"avilable tickets are {ticket}")
        ticket = ticket-1
        print("ticket is booked")
        print(f"avilable tickets are {ticket}")

    else:
        return print("ticket is not avilable")

ticket1=5
p1=bookticket(ticket1)
p2=bookticket(ticket1)

def factorialsmpl(n):
    product =1
    for i in range(n):
        product = product * (i+1)
    return product


def fctrcrsv(n):
    if n==0 or n==1:
        return 1

    else:
        return n*fctrcrsv(n-1)    
     
f =fctrcrsv(4)
print(f)

