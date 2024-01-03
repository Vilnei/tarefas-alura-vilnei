import speech_recognition as sr


palavra_chave = "jarvin"


def trasf_audio_texto_padrao():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Aguardando Ordens ...")
            audio = mic.listen(source)
            try:
                texto_voz = mic.recognize_google(audio, language='pt-br')
                texto_voz = texto_voz.lower()
                if palavra_chave in texto_voz:
                    print(texto_voz.sprip(palavra_chave))
                    break 

            except sr.UnknownValueError:
                print("Desculpe, não entendi o que você disse")
            except sr.RequestError as e:
                print('Desculpe-me, não conseguimos reconhecer esse comando;{0}'.format(e))

# with open('nome do arquivo .json da google cloud') as credenciais_google:
#     credenciais_google = credenciais_google.read()

# def trasf_audio_texto_googlecloud():
#     mic = sr.Recognizer()
#     with sr.Microphone() as source:
#         audio = mic.listen(source)
#     try:
#         texto = mic.recognize_google(audio)
#     except sr.UnknownValueError:
#         texto = "Desculpe, não entendi o que você disse"
#     except sr.RequestError as e:
#         texto = "Desculpe, não entendi o que você disse"
#     return texto



if __name__ == '__main__':
    trasf_audio_texto_padrao()
    # print(trasf_audio_texto_googlecloud())
