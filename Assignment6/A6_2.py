print("3 digit number") if int(input("num="))/100>=1 else print("naah mate")
#or 99<n<100
#7
x=int(input("num="))
if x>0:
    print("positive")
elif x<0:
    print("negative") 
 
else:
    print("zero")


#8
#quadratic equation= ax**2+bx+c
#enter coefficients x**2,x and constant
a,b,c=int(input()),int(input()),int(input())
d=b**2-4*a*c
if d>0:
    print("real and distinct roots")
elif d==0:
    print("real and equal roots")
else:
    print("imaginary roots")
