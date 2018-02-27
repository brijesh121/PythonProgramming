import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "hilwJo6SAmFwEcOEGnF32ujR8",
    "consumer_secret"     : "NH2pnLHeKcPTgNCwEOnYs2LKndyNCRRLTW4OAV2ASXasQfiGd7",
    "access_token"        : "V86kP6jey1KFgVvkhBs87dh0Zp45g29rLkQMLjP",
    "access_token_secret" : "yLp4ToUDsly0ztdGpv7iQ82PlduL1iWlSZloz3y7w8QIH" 
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
