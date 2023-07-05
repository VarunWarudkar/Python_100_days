# from gtts import gTTS
# from time import sleep
# import os
# names = ["Heramb","Vrinda","Renuka","Swara","Samihan"]
# for name in names:
#     tts = gTTS(text=f'Hi; HI {name} , lots of shout out for {name}, Hip Hip Hurray', lang='en')
#     tts.save(f"good_{name}.mp3")
#     os.system(f"good_{name}.mp3")
#     sleep(2)

# import pyttsx
# e = pyttsx.init()
# e.say('Good morning.')
# e.runAndWait()
from os import name as Name
print(Name)
# Windows
import win32com.client #pip install pywin32
speaker = win32com.client.Dispatch("SAPI.SpVoice")
names = ["Heramb","Vrinda","Renuka","Swara","Samihan"]
for name in names:
    speaker.Speak(f"HI {name} , lots of shout out for {name}, Hip Hip Hurray")

# # for Mac
# from os import system
# names = ["Heramb","Vrinda","Renuka","Swara","Samihan"]
# for name in names:
#     system(f'HI {name} , lots of shout out for {name}, Hip Hip Hurray')