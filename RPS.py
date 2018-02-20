import random
l=["Rock","Paper","Scissor"]
comp=random.choice(l)
user=input("Enter Your Choice:")
print("Computer=",comp)
if comp==user:
    print("It's a Tie")
elif comp=="Rock" and user=="Scissor":
    print("Computer Won by Rock.")
elif comp=="Rock" and user=="paper":
    print("You have Won.")
else:
    print("You have won")


    
    
