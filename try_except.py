'''
while(True):
    try:
        a=int(input("\nEnter an integer\n"))
    
    except Exception as e:
        print("please enter valid value\n")

    else:
        print(f"You have entered {a}\n")
    finally:
        print("\nGame Over")
'''

'''
try:
    a=int(input("enter a number\n"))
    c=1/a
except ValueError as e:
    print("enter valid value\n")

except ZeroDivisionError as e:
    print("check number should not be zero\n")

else:
    print(c)

finally:
    print("we have done it successfullly")
'''
