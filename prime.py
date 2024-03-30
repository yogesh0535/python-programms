n=int(input())
prime=1
for i in range(2,n):
    if n%i==0:
        prime=0
        break

if prime==1:
    print(f"{n} number is prime")
    if n%2==0:
        print("It is even number")
    else:
        print("It is odd number")

else:
    print(f"{n} numberis not prime")
    if n%2==0:
        print("It is even number")
    else:
        print("It is odd number")