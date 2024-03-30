'''
with open('text.txt','r') as f:
    a=f.read()
    print(a)
with open('text.txt','a') as f:
        a=f.write("he is a good boy\n")
'''
with open("text.txt","rt") as f:
    a=f.readline()
    a1=f.read(5)
    print(a)
    print(a1)
