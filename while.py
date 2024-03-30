'''
languages=['c','c++','java','python']
i=0
#while(i<4):
while(i<len(languages)):
    print(languages[i])
    i=i+1    
'''

print("enter the number whose table required")
n=int(input())
print("the table of "+ str(n) +" is given below")
i=1
while(i<11):
    print(n*i)
    i=i+1