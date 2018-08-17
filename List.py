#Q1
LI1=[]
n=int(input("enter total no. of value:"))
for x in range(n):
    x=input("enter item:")
    LI1.append(x)
print (LI1)

#Q2
LI2=['google','apple','facebook','microsoft','tesla']
LI1.extend(LI2)
print(LI1)

#Q3
LI=[1,2,3,4,1,1]
print("TOTAL NUMBER OF COUNT :",LI.count(1))

#Q4)
LI=[]
n=int(input("enter total no. of value:"))
for x in range(n):
    x=int(input("enter item:"))
    LI.append(x)
LI.sort()
print("SORTED LIST:",LI)


#Q5)
A=[]
B=[]
n=int(input("enter total no. of value in list A:"))
for x in range(n):
    x=int(input("enter value:"))
    A.append(x)
n2=int(input("enter total no. of value in list B:"))
for x in range(n2):
    x=int(input("enter value:"))
    B.append(x)
A.sort()
B.sort()
print("SORTED LIST A:",A)
print("SORTED LIST B:",B)
A.extend(B)
A.sort()
C=A
print('MERGED SORTED LIST :',C)

#Q6)
LI=[]
n=int(input("enter total no. of value:"))
for x in range(n):
    x=int(input("enter numbers:"))
    LI.append(x)
even=0
odd=0
for j in LI:
    if j%2==0:
        even+=1
    else:
        odd+=1
print('Total even numbers:',even)
print('Total odd numbers:',odd)

#TUPLE: This topic hasn't been done yet.


