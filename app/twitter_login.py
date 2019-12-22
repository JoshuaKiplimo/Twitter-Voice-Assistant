from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time
import random
from dotenv import load_dotenv
load_dotenv()



class TwitterBot:

	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.bot = webdriver.Chrome(executable_path = "/Users/emmanuelgyekyeatta-penkra/Documents/Tweet My Voice/chromedriver 2")#instance of the bot

	def login(self):
		
			
		BOT = self.bot
		BOT.get("https://twitter.com/login")
		time.sleep(10) #pause as the page loads
		email = BOT.find_element_by_name("session[username_or_email]")
		password = BOT.find_element_by_name("session[password]")
		email.clear()
		password.clear()
		email.send_keys(self.username)
		password.send_keys(self.password)
		password.send_keys(Keys.RETURN)
		time.sleep(3)
		


twitter = TwitterBot(os.getenv('username'), os.getenv('password'))
twitter.login()
