'''
n=int(input())
sum=0
for i in range(1,n+1):
    print(i)
    sum=sum+i

print("the sum is " + str(sum))    
'''
'''
def sum(n):
    if(n==0):
        return 0
    #add=0
    #for i in range(1,n+1):
    else:
      return (n+sum(n-1))  

num=int(input())
s=sum(num)
print("the sum is "+str(s))
'''

                    # factorial without recursion
'''
def fact(a):
    factorial=1
    i=1
    while(i<=a):
        factorial=factorial*i
        i+=1
    return (factorial)

num=int(input())
r=fact(num)
print(r)
'''

                                # factorialusing recursion
def fact(a):
    if (a==0 or a==1):
        return(a)
    else:
        return (a*fact(a-1))

num=int(input())                    
r=fact(num)
print(f"factorial of {num} is {r}")