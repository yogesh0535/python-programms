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

    def salary(self):
        super().breathing()                      #access the upper function automatically
        print(f"my salary is {self.salary}")


p=person()
e=employee()
pr=programmer()

# pr.breathing
# pr.breath()

pr.salary()