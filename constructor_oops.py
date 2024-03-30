class employee:
    def __init__(self,name,age):
        print("constructor is created")
        print(f"creatr name is {name} and age is {age}\n")
    
    @staticmethod    
    def static(id,salary):
        print("it is static clas")
        print(f"it has id number {id} and salary is {salary}")

    def self_fuc(self,address):
        print(f"self function is created at {address}")


yogesh=employee('yogesh',22)     # this line for constructor
yogesh.static(3,30000)              # this for static method
yogesh.self_fuc('mumbai')           # this for self function


