import random  #extracting random function
c=0
while(c<100):
    a=input("Enter 'r' to roll a dice:r")
    if (a=='r'):
        r= random.randint(1,6)#printing random number from 1 to 6.
        c = c+r
        print("Dice value=")
        print(r)
        print("Count value=")
        print(c)
      
        if (c == 8):#if condtion
            c=37
            print("You have been placed to 37 by ladder")
        elif (c == 13):
            c=34
            print("You have been placed to 34 by ladder")
        elif (c == 40):
            c=68
            print("You have been placed to 68 by ladder")
        elif (c== 52):
            c=81
            print("You have been placed to 81 by ladder")
        elif (c == 76):
            c=97
            print("You have been placed to 97 by ladder")
        elif (c == 11):
            c=2
            print("You have been placed to 2 by snake bite")
        elif (c==25):
            c=4
            print("You have been placed to 4 by snake bite")
        elif (c == 38):
            c=9
            print("You have been placed to 9 by snake bite")
        elif (c== 65):
            c=46
            print("You have been placed to 46 by snake bite")
        elif (c== 89):
            c=70
            print("You have been placed to 70 by snake bite")
        elif (c== 93):
            c=64
            print("You have been placed to 64 by snake bite")
        elif c>100:
            c=c-r
        elif c==100:
            print("you won")
        
        
            

    



