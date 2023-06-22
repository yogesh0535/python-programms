 # to generate list of factorial of all numbers of a list  
def fact(i):
    if i==0 or i==1:
        return i
    else:
        return i*fact(i-1)

list=[1,2,3,4,5,6,7,8,9]
for i in list:
    print(f"factorial of {i} is: {fact(i)}")
