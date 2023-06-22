#average of a set of integers
count=int(input("Enter the number of integers: \n"))
sum=0
i=0
while(i<count):
    num=int(input(f"Enter the {i+1} integer : "))
    sum=sum+num
    i=i+1
avg=sum/count
print(f"averge of numbers is : {avg}")
