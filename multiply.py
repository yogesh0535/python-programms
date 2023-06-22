# multiply all items in list
list=[]
for value in range(5):
    a=int(input())
    list.append(a)
mul=1
for i in list:
    mul=mul*i
print(mul)
