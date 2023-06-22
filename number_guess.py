#to guess a number from 1 to 9 
while(True):
    import random
    guess=random.randint(1,9)
    num=int(input("\nEnter your guess from 1 to 9: \n"))
    if (num==guess):
        print("done!")

    else:
        print("miss")
