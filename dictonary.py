dictonary={"yogesh" : "coder",
        "computer" : "machine",
        "another" : {"mouse":"input","printer":"output"},
        "set": {1,2,3,4},
        "list":[3,4,6,'string']
    }
#dictonary["set"]={10,20,30}         #updating elements in dict

#print(dictonary['yogesh'])
#print(dictonary['another']['printer'])
#print(dictonary['another']["mouse"])
#print(dictonary['set'])

for key,value in dictonary.items():
    print(key , '::' , value)

                    #methods or functions of dictonary


#print(list(dictonary.keys()))               
#print(list(dictonary.values()))   
#print(dictonary.items())                                     
#print(dictonary.keys())
'''
updatedictonary={
    "rose":"gulab"
}
print(updatedictonary)
dictonary.update(updatedictonary)
print(dictonary)
'''