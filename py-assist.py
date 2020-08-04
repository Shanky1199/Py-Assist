

import pyttsx3

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices')
#print(voices[2].id) #getting details of current voice
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    speak('seeetharam is a ')