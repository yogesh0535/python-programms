'''
lambda function or anonymous function is one line or linear function.open
it is used to define a function in one line 
'''


                    #function without lambda
'''
def add(x,y):
    return x+y

a=int(input())
b=int(input())
print(add(a,b))

'''


                    # function using lambda
'''
add=lambda x,y:x+y

a=int(input())
b=int(input())
print(add(a,b))

'''
'''
def a_first(a):
    return a[1]

a=[[2,5],[45,3],[33,643]]       
a.sort(key=a_first)                     #assending order according to last digit
print(a)
'''

#a=[[112,14],[5,7],[8,23]]
#a.sort(key=lambda x:x[0])           # assending order according to 0 index
#print(a)

'''
                        # factorial using lambda

fact=lambda a:1 if a==0 else a*fact(a-1)

a=int(input())
print(fact(a))
'''
