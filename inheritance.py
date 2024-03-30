'''# this is single inheritance

class employee:
    company='google'

    def showdetails(self):
        print("this is an employee\n")
    
class programmer(employee):
    language='python'

    def lang(self):
        print(f"the language is {self.language}\n")

e=employee()
e.showdetails()
p=programmer()
p.showdetails()
print(p.company)
'''


'''
# mutiple inheritance

class employee:
    company="visa"
    code=10

class freelancer:
    company="fiver"
    level=100

    def upgrade(self):
        self.level=self.level+1

class programmer(employee,freelancer):
    name='archit'

p=programmer()
print(p.level)

'''

# multilevel inheritance
class person:
    country='india'

    def breath(self):
        print("i am breadthing. ")

class employee(person):
    company='infosis'

    def breathing(self):
        print("i am employee so i am breadthing.")

class programmer(employee):
    country='wipro'



p=person()
e=employee()
pr=programmer()

pr.breathing()
pr.breath()