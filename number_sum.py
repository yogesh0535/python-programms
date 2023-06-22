
#sum of digits of number
num=int(input("enter the integer: "))
sum=0
while(num!=0):
    rem=num%10
    sum=sum+rem
    num=num//10
print(f"sum of digits of number is : {sum}")
