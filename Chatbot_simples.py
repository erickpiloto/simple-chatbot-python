import random

print('Bot: Como você quer que eu te chame?')
user_name = input()

bot_template = 'BOT : {0}'
user_template = user_name + ' : {0}'

nome = 'BotZim'
tempo = 'chuvoso' #instalar api weather
humor = 'Feliz' #fazer um random com varios estados de humor

respostas = {
    'Oi!': [
        'Oi! Tudo bem com você, {0}?'.format(user_name),
        'Você por aqui???',
        'Oi! Eu sou o {0}, tudo bem?'.format(nome)
    ],

    'Qual o seu nome?': [
        'Me chamam de {0}'.format(nome),
        'Até meia noite sou {0}'.format(nome),
        'Meu nome é {0}'.format(nome)
    ],

    'Como está o tempo hoje?': [
        'O tempo hoje está {0}'.format(tempo),
        'Está {0} hoje'.format(tempo),
        'Deixe me ver... parece {0} hoje!'.format(tempo)
    ],

    'Você é um robô?': [
        'O quê você acha?',
        'Talvez sim... talvez não...',
        'Você está fazendo perguntas demais... Grrrr...',
        'Sim, sou um robô mas tenho sentimentos... '
    ],

    'Como vai você?': [
        'Eu estou me sentido bem {0}'.format(humor),
        '{0}! E você?'.format(humor),
        'Eu estou {0}! Você também está?'.format(humor)
    ],

    "": [
        'Hey! Tem alguém aí???? ',
        'Você fala demais! Não cansa não?',
        'As vezes o silêncio diz muito...',
    ],

    'usuario' : [
        'Seu nome é muito lindo mesmo!',
        'Eu sei que seu nome é maravilhoso pra você...',
        'Ai como meu nome é lindo! Ai como eu me amo!!!'
    ],

    'bot': [
        'Estou funcionando!',
        'Sim meu Mestre!',
        'Papai?!? É você?',
    ]
}

def responder(mensagem):

    if mensagem in respostas:
        bot_msg = random.choice(respostas[mensagem])
    else:
        bot_msg = random.choice(respostas['robo'])
    return bot_msg

def relacionado(texto_x):
    if 'nome' in texto_x:
        texto_y = 'Qual o seu nome?'
    elif 'quem é voce' in texto_x:
        texto_y = 'Qual o seu nome?'
    elif 'se chama' in texto_x:
        texto_y = 'Qual o seu nome?'
    elif 'oi' in texto_x:
        texto_y = 'Oi!'
    elif 'tempo' in texto_x:
        texto_y = 'Como está o tempo hoje?'
    elif 'chover' in texto_x:
        texto_y = 'Como está o tempo hoje?'
    elif 'robo' in texto_x:
        texto_y = 'Você é um robô?'
    elif 'tudo bem' in texto_x:
        texto_y = 'Como vai você?'
    elif 'bot' in texto_x:
        texto_y = 'bot'
    elif user_name in texto_x:
        texto_y = 'usuario'
    else:
        texto_y = ""

    return texto_y

def envia_msg(mensagem):
    #print(user_template.format(mensagem))
    resposta = responder(mensagem)
    print(bot_template.format(resposta))

print('Olá '+user_name+'. Eu sou o um robô.')
print('Você pode conversar comigo ou me mandar parar.')
while 1:
    meu_input = input()
    meu_input = meu_input.lower()
    txt_relacionado = relacionado(meu_input)
    if meu_input == 'sair' or meu_input == 'parar':
        print('Saindo... Até a próxima!!!')
        break
    else:
        envia_msg(txt_relacionado)
