import twitter
import tweepy
import json
import re
import requests
from dotenv import load_dotenv
load_dotenv()

"""

posts data to twitter 

""" 

def post_tweets():
	try:
		
		auth = tweepy.OAuthHandler(os.getenv('api_key'), os.getenv('api_secret_key'))    
		auth.set_access_token(os.getenv('access_token'), os.getenv('access_token_secret') )
		api = tweepy.API(auth)

		asked = "Testing!!!"

		api.update_status(status = asked)
	except tweepy.TweepError as e:
		print(e.args[0][0]['message'])#add a message to tell the user that posting the tweet is not possible


"""

gets trending data from twitter

"""

def top_three_trending_topics():
	
	auth = twitter.oauth.OAuth(os.getenv('access_token'), os.getenv('access_token_secret'), )

	twitter_api = twitter.Twitter(auth=auth)

	US_ID = 23424977



	
	us_trends = twitter_api.trends.place(_id=US_ID)





	def split_on_caps(str): # twitter double word trends are always camel cased
	    
	    rs = re.findall('[A-Z][^A-Z]*',str)
	    fs = ""
	    for word in rs:
	        fs += " "+word
	    
	    return fs

	to_read = []
	with_hashtag = []
	for trend in range(0,3):
		q = us_trends[0]['trends'][trend]['name']
		with_hashtag.append(q)
		if q[0] =='#':
			s = us_trends[0]['trends'][trend]['name'].split('#')[1]
			trending_subjects = split_on_caps(s)
			to_read.append(trending_subjects)
		else:
			s = us_trends[0]['trends'][trend]['name']
			trending_subjects = split_on_caps(s)
			to_read.append(trending_subjects)
			


	return to_read, with_hashtag
	

	# except:
		# return "Sorry I cannot find the trending data for now "


def top_trending_tweets():
	

	r = requests.post('https://api.twitter.com/oauth2/token',
	auth=(os.getenv('api_key'), os.getenv('api_secret_key')),
	headers={'Content-Type':
	          'application/x-www-form-urlencoded;charset=UTF-8'},
	data='grant_type=client_credentials')
	assert r.json()['token_type'] == 'bearer'
	bearer = r.json()['access_token']
	listt  = top_three_trending_topics()[1]
	print(listt)
	final =[]
	count = []
	for hashtag in listt:
		if hashtag[0] =='#':
			hashtag = hashtag.split('#')[1]
			url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23' + hashtag +'&rpp=1'
			r = (requests.get(url, headers={'Authorization': 'Bearer ' + bearer})).json()
			count.append(r['statuses'][0]['text'])
			

			
		else:
			final.append(hashtag)
			url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23' + hashtag +'&rpp=1'
			r = (requests.get(url, headers={'Authorization': 'Bearer ' + bearer})).json()
			count.append(r['statuses'][0]['text'])
	return count
		