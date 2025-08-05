print("a simple calculator")
print("1.addition")
print("2.subtraction")
print("3.multiply")
print("4.divide")
n=input("enter ur choice:")
a=float(input("enter 1st number:"))
b=float(input("enter 2nd number:"))
if n=="1":
    print("addition=",(a+b))
elif n=="2":
    print("subtraction=",(a-b))
elif n=="3":
    print("multiplication=",(a*b))
elif n=="4":
    if b!=0:
        print("division=",(a/b))
    else:
        print("can't divided by 0")
else:
    print("invalid choice")
