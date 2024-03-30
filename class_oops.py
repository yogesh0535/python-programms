
class employee:
    leaves=4


yogesh=employee()
bhupesh=employee()
print(employee.leaves)
yogesh.role="guide"
bhupesh.role="ASSISTANT"

yogesh.salary=6000
bhupesh.salary=45000
yogesh.leaves=3
employee.leaves=5
bhupesh.leaves=6
print(yogesh.__dict__)

print(bhupesh.__dict__)
print(employee.leaves)
print(yogesh.leaves)
print(bhupesh.leaves)
print(employee.__dict__)



'''

class student:
    pass
std1=student()
std2=student()
std1.name="Yogesh"
std1.roll_number=2101605
std2.name="Bhupesh"
std2.roll_number=2101603
std1.subjects=["PYTHON language","scycology"]
std2.subjects=["maths","biology"]
print(std1.name)
print(std1.roll_number,std1.subjects)
print(std2.name)
print(std2.roll_number,std2.subjects)
print(std1.__dict__)
print(std2.__dict__)


'''