## Interacting With Twitter Using A Voice Assistant  

### Description

This is a python based voice assistant that utilizes Google speech synthesis on an iOS to use a voice assistant to interact with the user by `reading trending hashtags on twitter`, `top trending tweets on twitter, allowing the user to post tweets vocally and automated login to twitter`.

The voice assistant is ideally active at all times and is activated by a specific trigger word. 

If the user needs to log into twitter, the voice assistant automates it through the use of selenium and its webdrivers. 

As of this writing google speech synthesis is limited to 50 requests a day, that being the only limitation. Otherwise, audio.py can be scheduled to run during certain times of the day or every minute of the day using cron tasks that the user can set.


Due to pyAudio's installation difficulties on iOS and python3, I found a [solution]('https://stackoverflow.com/questions/55984129/attributeerror-could-not-find-pyaudio-check-installation-cant-use-speech-re') through 'ducktyping' the microphone to listen to messages
 



```


Here is a snippet:
...internally it requires only a few attributes of Microphone to be duck-typed to allow it to listen() successfully. Specifically:
source must be an instance of a speech_recognition.AudioSource subclass
source.stream must be non-None while the source is active
source.CHUNK must be the (integer) number of samples per chunk
source.SAMPLE_RATE must be the sampling rate
source.SAMPLE_WIDTH must be the number of bytes per sample
source.stream.read(numberOfSamples) must return raw single-channel audio data


```


 The project is still in its beginning stages and can be buggy, more updates are coming coming soon

### Screenshot 1 

###### Commands running on the terminal...
![screenshot1](/images/screenshot1.png)

### Screenshot 2 

#### Final post on twitter through the voice assistant
![screenshot2](/images/screenshot2.png)



