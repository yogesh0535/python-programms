
while(True):
    b=int(input("\nenter the divisor\n"))
    a=int(input("enter the dividend\n"))
    try:
        c=a/b
    
    except ZeroDivisionError as e:
        print("infinity\n")
    
    except ValueError as e:
        print("\nplease check the values entered!")
    else:
        print(f"{a}/{b} = {c}")
    finally:
        print("We have done")

