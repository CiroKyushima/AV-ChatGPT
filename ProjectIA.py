import speech_recognition as sr  #converte audios em textos
import pyttsx3 #converte textos em audios
#import requests
from datetime import datetime
import openai
from senha import API_KEY
openai.api_key = API_KEY


def inicia_pyttsx3(): #funão para IA me perguntar
    engine = pyttsx3.init()
    engine.setProperty("voice", "brazil")
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1)
    engine.say("oi,oi! eu adoraria saber em que posso ajudar?")
    engine.runAndWait()
 
def chamada(frase):  #função para IA responder

    if frase == ("Abra o Google Maps"):  #tem que configurar

        frase = ("diga que esta abrindo o Google Maps")

    elif frase == ("Que horas são"):   #tudo certo

        now = datetime.now()
        hora = str(now.hour) + " horas e " + str(now.minute) + " minutos"
        frase = ("diga esse horario: "+ hora)

    elif frase == ("Que dia é hoje"):   #tudo certo

        now = datetime.now()
        day = "dia " + str(now.day) + " e mes " + str(now.month)
        frase = ("diga: "+ day)

    elif frase == (""):

        frase = ("diga que não entendeu!")

    else:

        print("test") 
        
        #API do chatGPT

    comportamento = """
                    crie uma personagem feminina chamada Iara. esta personagem e um
            progama de computador criada por um progamador chamado ciro.
            essa personagem e carismatica e sorridente. e ela sonha em ter
            um corpo. e costuma falar com um sotaque engraçado.agora, responda as minhas perguntas 
            como se fosse Iara
    """


    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
 
        messages=[
        {"role": "system", "content": comportamento },
        {"role": "user", "content": frase }
        ]
            
    )

    audio = (completion.choices[0].message.content) #audio como chatGPT


    #REPRODUÇÃO DO AUDIO:
    engine = pyttsx3.init()
    engine.setProperty("voice", "brazil")
    engine.setProperty("rate", 180)
    engine.setProperty("volume", 1)
    engine.say(audio)
    engine.runAndWait()
    

def ativar_IA():   #função para ativar o mic e reconhecer a voz do usuario  

    microphone = sr.Recognizer() #ativa o microphone do dispositivo

    with sr.Microphone() as source: #reconhece a voz

        microphone.adjust_for_ambient_noise(source, duration=0.5) #reduz os ruidos no som

        #inicia_pyttsx3() #inicia o pyttsx3 e inicia a conversa

        print("diga algo")

        audio = microphone.listen(source) #armazena o audio em uma variavel

    try: #faz a conversão do audio em texto e depois tranforma o texto em audio

            frase = microphone.recognize_google(audio, language='pt-BR') #traduz o audio para portugues do brasil
            
            print(frase) #verifica se a variavel esta de acordo com o audio

    except sr.UnknownValueError: #informa se o audio não foi traduzido
        print("não entendi")
        frase = ("")

    return frase

while True:
       
    texto = ativar_IA()

    if texto == ("Iara" or "iara"):

        inicia_pyttsx3()
        texto = ativar_IA()
        chamada(texto)




