from gtts import gTTS

text = "Olá, como está?"

language = 'pt-br'

obj = gTTS(text = text, lang = language, slow = False)

obj.save("voz.mp3")

