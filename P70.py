import win32com.client as wincl
speaker = wincl.Dispatch("SAPI.SpVoice")
speaker.Speak("Hello, it works!")
l = ["Rahul","Neha","Riya","Yash"]
for i in l:
    speaker.speak(f"Shout out to {i}")