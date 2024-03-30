sub1=int(input())
sub2=int(input())
sub3=int(input())
if(sub1 or sub2 or sub3)<33:
    print("you are fail due to less marks in one sunject")
elif((sub1+sub2+sub3)/3)<40:
    print("you are fail due to less percentage")
else:
    print("Congratulation! You have passed")    
