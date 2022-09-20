import pyttsx3
friend= pyttsx3.init()
speech = input ("Type to speak:")
friend.say(speech)
friend.runAndWait()