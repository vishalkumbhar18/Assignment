#1
n=5
if n>0:
    print("positive")
else:
    print("non-positive")
print()
#2
m=5
if n%5==0:
    print("divisable by 5")
else:
    print("not divisable by 5")
print()
#or 
print("divisable") if m%5==0 else ("naah mate")
print()
#3%
print("even") if int(input("number="))%2==0 else ("odd") 
print()
#4
a,b=int(input()),int(input())  
print(b) if b>a else (a)
print() 
#5
c,d=input(),input()
print(c,d) if c<d else (d,c)
print()