# AV-ChatGPT
 assistente virtual por comando de voz que utiliza o chatGPT para orientar respostas.

https://platform.openai.com/

acesse o link da open ai e crie uma key para poder testar o codigo.

esse projeto utiliza as bibliotecas:
    1 - speechRecognition --> utilizado para transformar a voz em texto
    2 - pyttsx3 --> utlizado para tranformar o texto em audio
    3 - datetime
    4 - openai --> para usar o chatGPT


o codigo foi separado em 3 funções principais:
    1 - inicia_pyttsx3 --> utilizado para iniciar a conversa entre voce e a maquina

    2 - chamada --> parte principal do codigo, nela usamos o chatGPT para conversa.
        obs: devido a incapacidade do chatGPT ler a hora atual, podemos utilizar a biblioteca
    datetime para coletar a hora exata. e depois devemos apenas pedir que a IA diga a hora.
        obs2: na variavel "comportamento" podemos dar um roteiro para a IA seguir. assim teremos
    uma IA totalmente personalizavel.
        obs3: usamos a bibliota pyttsx3 para tranformar a resposta do chatGPT em audio.

    3 - ativar_IA --> objetivo principal e ligar o microphone, captar a voz e tranformar em texto.

a parte real do codigo e utilizada apenas para a IA identificar quando voce dizer o nome dela para assim começar a conversa.