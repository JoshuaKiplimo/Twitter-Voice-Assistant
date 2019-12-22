import tweepy 
import json
import requests
import time, numpy, audiomath, speech_recognition
from gtts import gTTS
import pygame
from io import BytesIO
import os
import test2
import twitter_login
import threading
from dotenv import load_dotenv
load_dotenv()

"""
A function to call gtts AND speak to the user 

"""

def say(text):
    tts = gTTS(text=text, lang='en')
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()

class DuckTypedMicrophone( speech_recognition.AudioSource ): # parent class required purely to pass assertion in Recognizer.listen
    def __init__( self, device=None, chunkSeconds=1024/44100.0 ):
        self.recorder = None
        self.device = device
        self.chunkSeconds = chunkSeconds
    def __enter__( self ):
        self.recorder = audiomath.Recorder( audiomath.Sound( 5, nchan=1 ), loop=True, device=self.device )
        self.CHUNK = int( audiomath.SecondsToSamples( self.chunkSeconds, self.recorder.stream.fs ) )
        self.SAMPLE_RATE = int( self.recorder.stream.fs )
        self.SAMPLE_WIDTH = self.recorder.sound.bytes
        self.nSamplesRead = 0
        return self
    def __exit__( self, *blx ):
        self.recorder.Stop()
        self.recorder = None
    def read( self, nSamples ):
        targetHead = audiomath.SamplesToSeconds( self.nSamplesRead + nSamples, self.SAMPLE_RATE )
        while self.recorder.head < targetHead: time.sleep( 0.001 )
        snd = self.recorder.sound
        startSamples = self.nSamplesRead % snd.nSamples
        chunk = snd.y[ startSamples : startSamples + nSamples, : ]
        wrapped = nSamples - chunk.shape[ 0 ]
        chunk = numpy.concatenate( ( chunk, snd.y[ :wrapped, : ] ), axis=audiomath.ACROSS_SAMPLES )
        self.nSamplesRead += nSamples
        return snd.dat2str( chunk )
    @property
    def stream( self ): # property required purely to pass assertion in Recognizer.listen
        return self if self.recorder else None

if __name__ == '__main__':
    
    def ask():
        try:

            import speech_recognition as sr

            r = sr.Recognizer()
            with DuckTypedMicrophone() as source: # replaces the PyAudio-dependent class sr.Microphone()
                print('Say something to the %s...' % source.__class__.__name__)
                audio = r.listen(source)
                print('Got it.')
                print('Understood: "%s"' % r.recognize_google(audio))
                audio1 = r.recognize_google(audio)
                return audio1
        except:
            pass


"""

A function to ask if the user wants to login to twitter to check their feed 

"""

def log_in():
    say("Do you want to log in to twitter ?")
    time.sleep(3)
    say("say something")
    time.sleep(2)
    conf = ask()
    return conf

"""

A function to automate twitter login, imported from twitter_login.py 


"""

def selenium_login():
    twitter_login.twitter.login() 




def top_trending():
    say("Before I log out, here are top three trending topics right now on twitter:")
    time.sleep(2)
    for words in test2.top_three_trending_topics()[1]:
        say(words)
        time.sleep(1)
    time.sleep(2)
    if log_in() == "yes":
        say("Okay, logging you into twitter")
        selenium_login()




"""

To keep listening to the trigger word 'Hello', trigger word can be changed at any time 

"""


def LISTEN_MODE(phrase='hello'): #Trigger word to activate the sequence
    
    try: 
        transcript = ask()
        if transcript.lower() == phrase:
            return True
        else:
            return False
    except:
        pass
        


"""

Once the word matches the trigger word, the following sequence is initiated 

"""

while True:
    if LISTEN_MODE() == True:

        try:
            
            say("Hello Joshua, do you want to hear what people are talking about or you want to post a tweet?")
            time.sleep(6)
            say("say something")
            time.sleep(0.75)
            transcript = ask() 
             #to allow processing of the message
            hear = transcript.split(' ')
            time.sleep(2)
            print(hear)
            
            if 'post' in  hear or 'tweet' in hear:
                
                say("say something for me to tweet")
                time.sleep(3)
                asked = ask()
                print(asked)
                
                say("Do you want me to tweet the following words:" + asked)
                time.sleep(3)
                
                say("Say something")
                time.sleep(1)
                confirmation = ask()

                if confirmation == 'yes':
                    api.update_status(status = asked)
                    
                    say("I have tweeted: " + asked)
                    
                if log_in() == "yes":
                    selenium_login()



                else:
                    say("Good day. No tweet has been sent out")
                    time.sleep(3)
                    top_trending()




            elif 'hear' in hear or 'people' in hear:
                
                for tweet in test2.top_trending_tweets():
                    say(tweet)
                    time.sleep(11)
                say("As you can hear, the top trending topics are:")
                for word in top_three_trending_topics()[2]:
                    say(word)
                    time.sleep(3)
                say("Are you still interested in login in")
                time.sleep(5)
                say("Say something")
                yes_no = ask()
                if yes_no == "yes":
                    selenium_login()
                else:
                    say("Okay. Goodday")








                
            else:
                say("Before I log out, here are top three trending topics right now :")
                time.sleep(5)
                for words in test2.top_three_trending_topics()[0]:
                    say("hashtag" + words)
                    time.sleep(1)
                time.sleep(3)
                if log_in() == "yes":
                        selenium_login()


                
        except:
            pass




    