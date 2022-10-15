import gtts
from gtts import gTTS
import speech_recognition as sr
import playsound
import time
from time import ctime
import os
import uuid

'''text=gTTS('hello how are you?')
text.save('dialoge1.mp3')'''
def listen():
    '''audio assistance'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("talk now")
        audio=r.listen(source,phrase_time_limit=5)
    data=""
    #exception handling
    try:
        data=r.recognize_google(audio,language='en-US')
        print('you said '+data)
    except sr.UnkownValueError:
        print('speak properly')
    except sr.RequestError:
        print('sarriga matladu')
    return data

#listen()
def respond(string):
    print(string)
    q=gTTS(text=string,lang='en-US')
    q.save('dialog2.mp3')
    f='dialog2%s.mp3'%str(uuid.uuid4())
    q.save(f)
    playsound.playsound(f)
    os.remove(f)

def virtual_assistant(data):
    if 'how are you' in data:
        data=True
        respond('good! how are you?')
    if 'time' in data:
        data=True
        respond(ctime())

while listening==True:
    data=listen()
    listening=virtual_assistant(data)

