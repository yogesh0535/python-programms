'''
print("enter the number of rows of stars")
a=int(input())
for i in range(a):
    for n in range(i):
        print('*', end='')
    if i > 0:
        print()
'''
                                    

                                 #stars in reverse order
print("enter the number of rows of stars")
a=int(input())
for i in range(a):
    print("*" * (a-i))