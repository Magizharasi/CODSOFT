print("Calculator")
def add(a,b):
    c = a+b
    return c
def sub(a,b):
    c = a-b
    return c
def mul(a,b):
    c = a*b
    return c
def div(a,b):
    c = a/b
    return c
def rem(a,b):
    c = a%b
    return c
def cal():
    list = ["1.Addition","2.Subtraction","3.Multiplication","4.Division","5.Remainder"]
    print("\nChoose the ooperation to be performed:")
    for i in list:
        print(i)
    n = int(input("\nEnter the number:"))
    if 0<n<6:
        x = int(input("\nNumber 1:"))
        y = int(input("Number 2:"))
    else:
        print("\nEnter a valid input")
        cal()
    if n==1:
        print("\nSum of",x,"and",y,"is",add(x,y))
    elif n==2:
        print("\nDifference of",x,"and",y,"is",sub(x,y))
    elif n==3:
        print("\nProduct of",x,"and",y,"is",mul(x,y))
    elif n==4:
        print("\nQuotient of",x,"and",y,"is",div(x,y))
    else:
        print("\nRemainder of",x,"and",y,"is",rem(x,y))
try:
    cal()
except ValueError:
    print("Error: Please enter only integer values!")
    
