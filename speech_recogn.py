import speech_recognition as sr

def speech_tr():
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Birşeyler Söyle!")
                audio = r.listen(source)

        text = r.recognize_google(audio, language="tr-TR")
        return text

#print (speech_tr())