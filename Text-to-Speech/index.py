# Install the module
# pip install pyttsx3 
 
#Import important python modules


import pyttsx3

# Create an object for Pyttscx3 class

engine = pyttsx3.init()

# See how many voices you have in the system

for voice in engine.getProperty("voices"):
    print(voice)

# Select voice in the system
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)

# Create a functiom to convert text to speech

def Speak(Audio):
    engine.say(Audio)
    engine.runAndWait()


# Write a code to ask the user to enter text

text = input("Enter your text to convert to speech: ")

# Call the function

Speak(text)