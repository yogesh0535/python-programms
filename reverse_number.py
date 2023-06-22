#display number in reverse order
num=int(input("enter the number: "))
new=0
#6534
while(num!=0):
    r=num%10
    new=new*10+r
    num=num//10
print(new)
