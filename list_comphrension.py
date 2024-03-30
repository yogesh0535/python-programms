 #list compherension

ls=[i for i in range(1,20) if i%2==0]  
ls1=[i for i in range(1,50) if i%3==0]  
print(ls)
print(ls1)

a=[]
for i in range(1,21):
    a.append(i)

b=[i for i in a if i%2==0]
print(a)
print(b)