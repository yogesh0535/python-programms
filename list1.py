#fav_language = 'C '
#second_most_fav = ' python '
#third_most_fav = ' go'
#print(len(fav_language.rstrip()))
#print(second_most_fav.strip())
#print(third_most_fav.lstrip())

import webbrowser


a=[2,423,43,32]
b=[6,7,8,9]
#a.exted(b)         # adding a and b
#a.insert(2,100)      # adding 100 at 2nd index
#a.pop(3)                # delet element from given index
#a.pop()                # delet element from last
#a.reverse()            # for revrsing sequence
#a.sort(reverse=True)     #descending  order

#print(a.clear())            # deleting all elements
#del a[2]                # delet elemnt at 2 index

'''                       
print(a)
c= a[::]                #copying 1 list to 2nd 
d= list(a)
del c[1]
del d[0]
print(c)
print(d)
print(a)
'''
                                #finding even odd from list
'''
list=[13,46,78,93,89,90,00,535]
even=[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(odd)            
print(even)
'''
                                # SQUARING of list
'''
list=[9,3,8,0,5,3,5]
print(list)
square=[]
for i in list:
    square.append(i*i)

print(square)
'''

'''
path='/usr/bin/firefox'
firefox=webbrowser.get(path)
webbrowser.open('https://www.google.com')

#path = '/usr/bin/firefox'
#firefox = webbrowser.get(path)
#firefox.open('https://www.google.com')
'''

                        # sets complete details 
'''
b = {3,4,5,6}
a = {1,2,3,4, 'c',1.11}
s2 = a & b                  # for intersection
#s2 = a.intersection(b)
print(s2)

s4 = a | b                  # for union
s4 = a.union(b)
print(s4)

s5 = a - b 
print(s5)

c = {1,2}
d = {1,2,3,4}
#print(c < d) 
#print(c > d) 

if (d.issubset(c)):             # identifying subset
    print("yes")
else:
    print("no")

s = {1,2,2,3,4}
s.add(1000)                 # adding value in set
print(s)
s.remove(2)              # removing value from set 
print(s)
#s.discard(7)                #  removing of given element 
#print(s)
'''

'''
a = 100

def func():
    # global a
    a = 10
    print(a)

func()
print(a)
'''

#
#def get_age(age=18):
#    return age 
#
#age = get_age(35)
#print(age)

#def show_me_my_age(get_age, age):
#    print(get_age)
#    print(age)
#    return get_age(age)
#show_me_my_age('get_age', 100)
'''
def return_tuple(n):
    print(n)
    return 5,6
print(return_tuple(10))
'''