import os
import time
a=1
b=1
while(a<5):
    os.system("fswebcam -F 5 --fps 20 -r 1200*800 /home/cs2017a112/Brijesh/a"+str(b)+".jpg")
    time.sleep(2)
    print("pic taken")
    a=a+1
    b=b+1
                    
            
