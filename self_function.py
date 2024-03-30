class employee:
    pass
    def details(self):     #one argument passed
        return  f"Name is {self.name.title()}. Salary is {self.salary} and role is {self.role.title()}" 

yogesh=employee()
yogesh.name="yogesh"
yogesh.salary=6000
yogesh.role="coder"

print(employee.details(yogesh))
print(yogesh.details())     #these both lines are same



