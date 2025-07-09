def divide(a,b):
    try:
        c=a/b
        return c
    except ZeroDivisionError:
        print("divided by zero error")

a=int(input("enter number for a:"))
b=int(input("enter number for b:"))
res=divide(a,b)
print(res)