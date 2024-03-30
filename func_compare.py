                     # greatest among three numbers
'''
def cmp(a,b,c):
    if(a>b):
        if(a>c):
            print("a")
    elif(b>c):
        if(b>a):
            print("b")
    else:
       print("c")

a=input("enter the first number:\n")
b=input("enter the second number:\n")
c=input("enter third number:\n")
cmp(a,b,c)


'''

def comp(x,y,z):
    if((x>y) and (x>z)):
        print(f"first number{x} is greater")
    elif((y>x) and (y>z)):
            print(f"second number{y} is greater")
    elif((z>x) and (z>y)):
        print(f"third number{z} is greater")
a=input()
b=input()
c=input()
comp(a,b,c)

