import pyttsx3 as tt
import webbrowser

engine = tt.init('sapi5')
volume = engine.getProperty('volume')
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
print(voices[0])
print(voices[1])
engine.setProperty('rate', 150)
engine.setProperty('volume', 2.0)
engine.setProperty('voice', voices[1].id)
engine.say('Hello World!')
engine.runAndWait()
engine.stop()



