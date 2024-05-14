import win32com.client as Robot

speak = Robot.Dispatch("SAPI.SpVoice")
print("Welcome to the text-to-speech Robot programmed by Abubakar Hafeez ")
speak.speak("Welcome to the text-to-speech Robot  programmed by Abubakar Hafeez")
while True:
    print("Enter what you want me to speak:  \nPress 'q' for quit the program:")
    speak.speak("Enter what you want me to speak  Press 'q' for quit the program")   
    text=input("")
    if text=="q":
        break
    speak.Speak(text)