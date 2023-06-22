#fabonicc series

n=int(input("Enter the last digit:\n"))
first=int(input("Enter the first number:\n"))
second=int(input("Enter the second digit:\n"))
print(first)
print(second)
third=first+second
while(third<=n):
    third=first+second
    print(third)
    first=second
    second=third
