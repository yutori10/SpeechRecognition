import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile("./aftereat.wav") as source:
    audio = r.record(source)

text = r.recognize_google(audio, language = 'ja-JP')

print(text)