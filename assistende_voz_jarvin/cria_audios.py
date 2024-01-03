from gtts import gTTS
from playsound import playsound


def cria_audios(audio):
    tts = gTTS(audio, lang='pt-br') # aqui transforma a escrita em audio
    tts.save('./Teste_python/assistende_voz_jarvin/audios/ola.mp3')   # aqui salva esse audio na pasta designada e nome designado


playsound('./Teste_python/assistende_voz_jarvin/audios/ola.mp3')