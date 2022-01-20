#########################################################
# Este código traz a estrutura de conversa de um chatbot
# que faz a captura de informações de um cliente e verifica se ele é um possível lead qualificado
# Material confeccionado para o TCC do curso de especialização em IA da Puc Minas
# Kelly M. O. Lopes
# Campinas, set de 2021.
#########################################################


#########################################################
# Importando as bibliotecas necessárias para a construção do bot
#########################################################
# !pip install pytelegrambotapi   instala a biblioteca do Telegram via terminal

#import requests
import telebot
import ast
from telebot import types
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          RegexHandler, ConversationHandler, CallbackQueryHandler)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


#########################################################
# Informações iniciais para a construção do bot
#########################################################
CHAVE_API = '5060316690:AAHT4YuNvXGUEk6c9-exoUQAxYUie1IXXpE'
bot = telebot.TeleBot(CHAVE_API)

# Traz as informações pessoais do usuário que está interagindo com o bot  
print(bot.get_me())

# Cria um dicionário com chaves e valores que serão utilizados como entrada para os botões do bot
stringList = {"1": "👍 Sim", "2": "👎 Não"}

#########################################################
# Criação dos botões do Bot
#########################################################
# Função que trata das chaves e dos valores que vão para os botões do bot
def makeKeyboard(perguntas_1):
    markup = types.InlineKeyboardMarkup()
    # print("Passou - " + perguntas_1)

    for key, value in stringList.items():
        if value != "":
            markup.add(
                types.InlineKeyboardButton(text=value, callback_data="['value', '" + value + "', '" + key + "']"))
    return markup


# Função que inicializa as apresentações dos botões com o comando "/aqui"
@bot.message_handler(commands=['aqui'])
def handle_command_adminwindow(message):
    msg = message.text

    #################################################################
    # Captação dos dados da empresa atraves dos botões
    #################################################################
    ######################### pergunta 1 ############################
    perguntas_1 = "Você é um conselherio?"
    bot.send_message(chat_id=message.chat.id,
                     reply_markup=makeKeyboard(perguntas_1),
                     text="Você é um conselherio?",
                     parse_mode='HTML')

    ######################## pergunta 2 ############################

    bot.send_message(chat_id=message.chat.id,
                     text="A empresa possui governança corporativa?",
                     reply_markup=makeKeyboard(perguntas_1),
                     parse_mode='HTML')

    ######################## pergunta 3 ############################

    bot.send_message(chat_id=message.chat.id,
                     text="A empresa possui Conselho Administrativo?",
                     reply_markup=makeKeyboard(perguntas_1),
                     parse_mode='HTML')

    ######################## pergunta 4 ############################

    bot.send_message(chat_id=message.chat.id,
                     text="A empresa possui Conselho Fiscal?",
                     reply_markup=makeKeyboard(perguntas_1),
                     parse_mode='HTML')

    ######################## pergunta 5 ############################

    bot.send_message(chat_id=message.chat.id,
                     text="A empresa possui Conselho Deliberativo?",
                     reply_markup=makeKeyboard(perguntas_1),
                     parse_mode='HTML')

    ######################## pergunta 6 ############################

    bot.send_message(chat_id=message.chat.id,
                     text="A empresa possui Comitês?",
                     reply_markup=makeKeyboard(perguntas_1),
                     parse_mode='HTML')

    ######################## pergunta 7 ############################

    bot.send_message(chat_id=message.chat.id,
                     text="A empresa possui Assembleias?",
                     reply_markup=makeKeyboard(perguntas_1),
                     parse_mode='HTML')

    ######################## pergunta 8 ############################

    bot.send_message(chat_id=message.chat.id,
                     text="Existe algum outro tipo de Conselho dentro da empresa?",
                     reply_markup=makeKeyboard(perguntas_1),
                     parse_mode='HTML')

    ######################## pergunta 9 ############################

    bot.send_message(chat_id=message.chat.id,
                     text="O Conselho da empresa reune mais de 3 vezes ao ano? ",
                     reply_markup=makeKeyboard(perguntas_1),
                     parse_mode='HTML')

    ######################## pergunta 10 ############################

    bot.send_message(chat_id=message.chat.id,
                     text="Os comitês fazem uso de Atas? ",
                     reply_markup=makeKeyboard(perguntas_1),
                     parse_mode='HTML')

    ######################## pergunta 11 ############################

    bot.send_message(chat_id=message.chat.id,
                     text="Essas Atas são publicadas?",
                     reply_markup=makeKeyboard(perguntas_1),
                     parse_mode='HTML')


    #########################################################
    # O bot fornece uma resposta, finalizando a captação das perguntas
    #########################################################

    bot.send_message(chat_id=message.chat.id,
                     text="Pronto 😊, um de nossos gerentes irá entrar em contato com você")
    # reply_markup=makeKeyboard(perguntas_1),
    # parse_mode='HTML')
    
    bot.send_message(chat_id=message.chat.id,
                     text="Seja muito bem vindo a Atlas Governance, aqui se inicia uma grande 🚀 jornada!  ")
    # reply_markup=makeKeyboard(perguntas_1),
    # parse_mode='HTML')

    return perguntas_1

  
#########################################################
# Apresenta a resposta do botão na tela
#########################################################
# Função que expõe as informções dos cliks dos botões na tela do bot
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if (call.data.startswith("['value'")):
        print(f"call.data : {call.data} , type : {type(call.data)}")
        print(
            f"ast.literal_eval(call.data) : {ast.literal_eval(call.data)} , type : {type(ast.literal_eval(call.data))}")
        valueFromCallBack = ast.literal_eval(call.data)[1]
        keyFromCallBack = ast.literal_eval(call.data)[2]
        bot.answer_callback_query(callback_query_id=call.id,
                                  show_alert=True,
                                  text="Este botão equivale a " + keyFromCallBack)


#########################################################
# Construindo o fluxo de conversa do bot
#########################################################

# Função que trata da primeira Opção apresentada no menu do bot
@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    Nós temos os seguintes produtos:
    /basic Basic 
    /entreprise Entreprise 
    /professional Professional 
    Clique nos linkes para conhecer cada um deles.
    """
    bot.send_message(mensagem.chat.id, texto)


# Função que trata do primeiro item que está dentro da primeira Opção apresentada pelo bot
@bot.message_handler(commands=["basic"])
def basic(mensagem):
    texto = """
    O plano Basic é ideal para empresas de pequeno porte e que realizam ✍️ poucas reuniões durante o ano.
    """
    bot.send_message(mensagem.chat.id, texto)


# Função que trata do segundo item que está dentro da primeira Opção apresentada pelo bot
@bot.message_handler(commands=["entreprise"])
def entreprise(mensagem):
    texto = """
    Com o plano Enterprise, é possível criar reuniões, fazer o gerenciamento das pautas e das deliberações, convocar os participantes; tudo isso em menos de ⌚️ três minutos."""
    bot.send_message(mensagem.chat.id, texto)


# Função que trata do terceiro item que está dentro da primeira Opção apresentada pelo bot
@bot.message_handler(commands=["professional"])
def professional(mensagem):
    texto = """
    Já com o plano Professional, além do usuário conseguir fazer toda a gestão de suas reuniões, ele também consegue assinar as Atas e os documentos, utilizando nosso sistema de Assinatura Eletrônica 📝.
    """
    bot.send_message(mensagem.chat.id, texto)


# Função que trata da segunda Opção apresentada no menu do bot
@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para mais informações acesse: https://welcome.atlasgov.com/pt")


# Função que trata da terceira Opção apresentada  no menu do bot
@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Vamos lá, só preciso pegar algumas informações... ")
    bot.send_message(mensagem.chat.id, " Clique '/aqui' para iniciarmos")


    #########################################################
    # Calculo que verifica se a empresa possui uma governança robusta
    #########################################################
    # soma = int(conselheiro) + 10 * int(governaca) + int(administracao) + int(fiscal) + int(deliberativo) + int(
    # comites) + int(assembleias) + int(outros) + int(frequencia) + int(atas) + int(publicadas)
    # print(soma)

    #########################################################
    # Bot finaliza a conversa oferecendo ou não um determinado produto para o cliente
    #########################################################
    # colocar alguns if condicionais
    # if soma > 26:
    #    if atas == 2 and publicadas == 2:
    #        print('O produto que irá satisfazer as necessidades da sua empresa é o Professional')
    #    elif atas == 2:
    #        print('O produto que irá satisfazer as necessidades da sua empresa é o Enterprise')
    #    else:
    #        print('O produto que irá satisfazer as necessidades da sua empresa é Basic')

    #    print('Um de nossos gerentes irá entrar em contato.')
    #    print('Seja muito bem vindo a Atlas Governance, aqui se inicia uma grande jornada!')
    # else:
    #    print(
    #        'Sinto muito mas, sua empresa ainda não possui uma governança madura suficiente para utilizar nossos produtos.')
    #    print('Se desejar, temos especialistas que podem ajudar a sua empresa a chegar à maturidade desejada!')

    #########################################################
    # Coletando o horário em que a pessoa conversou com o bot
    #########################################################
    # data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


#########################################################
# Loop que verifica se existem novas mensagens para serem respondidas
#########################################################
def verificar(mensagem):
    return True


#########################################################
# Mensagem de saudadção do bot
# #########################################################
@bot.message_handler(func=verificar)
def responder(mensagem):
    #firstName = update.messagem.from_user.first_name
    texto =     """Oi tudo  bem 😃 ?
    Eu sou o bot da Atlas.
    Por favor,  clique em uma das seguintes opções:
    /opcao1 Conheça nossos produtos
    /opcao2 Mais informações
    /opcao3 Encontre o melhor produto para sua empresa
     """
    bot.reply_to(mensagem, texto)


bot.polling()
# while True:
#    try:
#        bot.polling(none_stop=True, interval=0, timeout=0)
#    except:
#        time.sleep(10)


# bot.polling()
