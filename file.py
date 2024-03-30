'''
f=open('text.txt','r')
data=f.read()                  # reading file
print(data)                             # printing read file
print(f.readline())         # reads one line at a time
f.close()
'''

                                # writing in file 
#f=open('text.txt','w')
#f.write("myself yogesh bhardwaj")
#f.close

'''
f=open("poem.txt","w")
f.write("twinkle twinkle little star,up above the words so high")
f.close()
f=open("poem.txt","r")
p=f.read()
print(p)
f.close()
if 'twinkle' in p:
    print("yes")
else:
    print("no")    
'''


'''
filename = 'pi_digits.txt'
with open(filename) as f:
    lines = f.readlines()
print(lines)
'''
'''
for i in range(2,11):
    print("\n")
    with open("tables.txt","w") as f:
     for j in range(1,11):
        a=(f"{i}*{j}={i*j}")
        print(a)
        f.write(a)
'''

f=open("intro.txt","r")
#text=f.read()
print(f.read())
