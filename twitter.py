import tweepy 
f=open('password/password.txt','r')
passwords=f.read().split('\n')

consumer_key=str(passwords[0])
consumer_secret=str(passwords[1])
access_token=str(passwords[2])
access_token_secret=str(passwords[3])
print(consumer_key+"\n"+consumer_secret)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#tweets = api.search('#12monthsofcode')
#for tweet in tweets:
#    try:
#        api.retweet(tweet.id)
#    except:
#        print("Already Retweeted   ")

message= "Sometext"
mentions=["shivam","rawat"]
mention=""

for i in mentions:
    mention=mention+" @"+i
print(message+mention)
api.update_status(str(message)+" "+str(mention))
