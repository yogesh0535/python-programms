
def dob(age):
    p=2022-age
    print(f"you are {p} years old")
def fut_age(age,n):
    print(f"your age after {n} years will be {age+n}")


age=int(input("enter your year of birth\n"))
if age<2022:
    dob(age)
    years=int(input("age after how many years after your age\n"))
    fut_age(age,years)
else:
    print("you entered future date.It can't be calculated.")