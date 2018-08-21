#Take an input year from user and decide whether it is a leap year or not.
year = int(input("Please Enter the Year Number you wish: "))
 
if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
    print("%d is a Leap Year" %year)
else:
    print("%d is Not the Leap Year" %year)

#Take length and breadth input from user and check whether the dimensions are of square or rectangle.
x=int(input("enter the length "))
y=int(input("enter the breadth"))
if(x==y):
        print("square")
else:
    print("rectangle")

#Take the input age of 3 people and determine oldest and youngest among them.
    
a=int(input("enter any number"))
b=int(input("enter any number"))
c=int(input("enter any number"))
if(a>b)and(a>c):
    print("oldest is",a)
elif((b>a)and(b>c)):
        print("oldest is",b)
elif(c>a)and(c>a):
        print("oldest is",c)
        
if((a<b)and(a<c)):
 print("youngest is",a)
        
elif((b<a)and(b<c)):
        print("youngest is",b)
elif(c<a)and(c<b):
        print("youngest is",c)

#Q4
age=int(input("Enter age"))
sex=input("Enter sex")
m=input("Enter marital status")
if(sex=='F'):
    print("Work in Urban Areas")
else:
    if(age>=20 and age<=40):
        print("Can work anywhere")
    elif(age>=40 and age<=60):
        print("Work in urban areas")
    else:
        print("Error")
#Q5
q=int(input("Enter quantity"))
c=100*q
if(c>1000):
    c=c-(c*0.1)
    print("Total cost is =",c)
else:
    print("Total cost is =",c)

#LOOPS

#Question 1
li=[]
for i in range(10):
    a=int(input("Enter a number"))
    li.append(a)
print(li)

#Question 2

while True:
    print("*")

    
#Question 3
    
a=[]
b=[]
num=int(input("enter number of elements"))
for i in range(num):
    c=int(input("enter number"))
    a.append(c)
for j in a:
    v=j*j
    b.append(v)
print(b)

#Question 4

li1=[]
li2=[]
li3=[]
li4=[]
a=int(input("Enter total number of inputs"))
for i in range(a):
    b=input("Enter elements of list")
    li1.append(b)
for i in li1:
    if(i.isdigit()):
        li2.append(i)
    elif(i.isalpha()):
        li3.append(i)
    else:
        li4.append(i)
print(li2)
print(li3)
print(li4)

#Question 5

p=[]
for i in range(1,101):
    if(i>1):
        flag=False
        for j in range(2,i):
            if(i%j==0):
                flag=True
        if not flag:
            p.append(i)
print(p)

#Question 6

for i in range(5):
    for j in range(i):
        print("*",end='')
    print()


#Question 7


li8=[]
n=int(input("Enter number of elements of list"))
for i in range(n):
    a=int(input("Enter element"))
    li8.append(a)
num=int(input("Enter the number you want to delete from list"))
x=li8.count(num)
for i in range(x):
    y=li8.index(num)
    del(li8[y])
print(li8)


