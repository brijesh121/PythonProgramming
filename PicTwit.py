# importing the module
import tweepy
import os
import time
 
# personal details
consumer_key ="hilwJo6SAmFwEcOEGnF32ujR8"
consumer_secret ="NH2pnLHeKcPTgNCwEOnYs2LKndyNCRRLTW4OAV2ASXasQfiGd7"
access_token ="2538904064-V86kP6jey1KFgVvkhBs87dh0Zp45g29rLkQMLjP"
access_token_secret ="yLp4ToUDsly0ztdGpv7iQ82PlduL1iWlSZloz3y7w8QIH"
 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
b=1
a=0
while a<=2:
    
    cmd="fswebcam -F 3 --fps 20 -r 800*600 /home/cs2017a112/Desktop/img.jpg"
    os.system(cmd)
    img="/home/cs2017a112/Desktop/img.jpg"
    print("Picture Taken")
    api.update_with_media(img, status="Nice one")
    print("wait for 5 second for selfie")
    time.sleep(5)
    a+=1
    b+=1
    print("Success")
