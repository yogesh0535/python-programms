                 # use of for loop in one line 

 
'''
#dictionary compherension

#d={i:f"item{i}" for i in range(1,1000)}
#print(d)
#d1={i:f"item{i}" for i in range(1,101) if i%5==0}
#print(d1)

d1={i:f"item{i}" for i in range(1,21) if i%5==0}
d2={value:key for key ,value in d1.items()}
print(d1)
print("\n")
print(d2)
'''

            # compherension using set
'''
# below is set 
dresses={i for i in ["dresses1","dresses2","dresses1","dresses2"]}
# below is list 
dresses1=[i for i in ["dresses1","dresses2","dresses1","dresses2"]]
print(dresses)
print(dresses1)
'''

          # compherension using generators


#odd1=[i for i in range(50) if i%2!=0]      #list compherension
#print(odd1)

odd=(i for i in range(50) if i%2!=0)        #generaor
print(odd)
print(odd.__next__())
print(odd.__next__())
print(odd.__next__())

#for item in odd:
#  print(item)
