#!pip install pytelegrambotapi   instala a biblioteca do Telegram via terminal
import telebot
import os
#import InlineKeyboardButton, InlineKeyboardMarkup, Update
#from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

CHAVE_API = '5060316690:AAHT4YuNvXGUEk6c9-exoUQAxYUie1IXXpE'
bot = telebot.TeleBot(CHAVE_API)


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

@bot.message_handler(commands=["basic"])
def basic(mensagem):
    texto = """
    O plano Basic é ideal para empresas de pequeno porte e que realizam poucas reuniões
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["entreprise"])
def entreprise(mensagem):
    texto = """
    Com o plano Enterprise, é possível criar reuniões, fazer o gerenciamento das pautas e das deliberações, convocar os participantes; tudo isso em menos de três minutos."""
    bot.send_message(mensagem.chat.id, texto)
print(bot.get_me())    #traz as informações pessoais do usuário que está interagindo com o bot
@bot.message_handler(commands=["professional"])
def professional(mensagem):
    texto = """
    Já com o plano Professional, além do usuário conseguir fazer toda a gestão de suas reuniões, ele também consegue assinar as Atas e os documentos, utilizando nosso sistema de Assinatura Eletrônica.
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para mais informações acesse: https://welcome.atlasgov.com/pt")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Vamos lá, só preciso de algumas informações...")

    #########################################################
    # Captação dos dados da empresa
    #########################################################

    bot.send_message(mensagem.chat.id, f'Você é um conselheiro? {os.linesep}/1-Sim {os.linesep}/2-Não')









    print(bot.get_me())    #traz as informações pessoais do usuário que está interagindo com o bot  #id=5060316690

    bot.send_message(mensagem.chat.id, f'Você é um conselheiro? {os.linesep}/1-Sim {os.linesep}/2-Não')
    #conselheiro = int(input(f'Você é um conselheiro? {os.linesep}1-Não {os.linesep}2-Sim'))
    bot.send_message(mensagem.chat.id, f'A empresa possui governança corporativa? {os.linesep}/1-Sim {os.linesep}/2-Não')
    bot.send_message(mensagem.chat.id, f'A empresa possui Conselho Administrativo? {os.linesep}/1-Sim {os.linesep}/2-Não')
    bot.send_message(mensagem.chat.id, f'A empresa possui Conselho Fiscal? {os.linesep}/1-Sim {os.linesep}/2-Não')
    bot.send_message(mensagem.chat.id, f'A empresa possui Conselho Deliberativo? {os.linesep}/1-Sim {os.linesep}/2-Não')
    bot.send_message(mensagem.chat.id, f'A empresa possui Comitês? {os.linesep}/1-Sim {os.linesep}/2-Não')
    bot.send_message(mensagem.chat.id, f'A empresa possui Assembleias? {os.linesep}/1-Sim {os.linesep}/2-Não')
    bot.send_message(mensagem.chat.id, f'Existe algum outro tipo de Conselho dentro da empresa? {os.linesep}/1-Sim {os.linesep}/2-Não')
    bot.send_message(mensagem.chat.id, f'O Conselho da empresa reune mais de 4 vezes ao ano? {os.linesep}/1-Sim {os.linesep}/2-Não')
    bot.send_message(mensagem.chat.id, f'Os comitês fazem uso de Atas? {os.linesep}/1-Sim {os.linesep}/2-Não')
    bot.send_message(mensagem.chat.id, f'Essas Atas são publicadas? {os.linesep}/1-Sim {os.linesep}/2-Não')

    #########################################################
    # O bot fornece uma resposta
    #########################################################

    bot.send_message(mensagem.chat.id, "'Só um minuto, estou processando as informações...")

    #########################################################
    # Calculo que verifica se a empresa possui uma governança robusta
    #########################################################
    #soma = int(conselheiro) + 10 * int(governaca) + int(administracao) + int(fiscal) + int(deliberativo) + int(
        #comites) + int(assembleias) + int(outros) + int(frequencia) + int(atas) + int(publicadas)
    # print(soma)

    #########################################################
    # Bot finaliza a conversa oferecendo ou não um determinado produto para o cliente
    #########################################################
    # colocar alguns if condicionais
    if soma > 26:
        if atas == 2 and publicadas == 2:
            print('O produto que irá satisfazer as necessidades da sua empresa é o Professional')
        elif atas == 2:
            print('O produto que irá satisfazer as necessidades da sua empresa é o Enterprise')
        else:
            print('O produto que irá satisfazer as necessidades da sua empresa é Basic')

        print('Um de nossos gerentes irá entrar em contato.')
        print('Seja muito bem vindo a Atlas Governance, aqui se inicia uma grande jornada!')
    else:
        print(
            'Sinto muito mas, sua empresa ainda não possui uma governança madura suficiente para utilizar nossos produtos.')
        print('Se desejar, temos especialistas que podem ajudar a sua empresa a chegar à maturidade desejada!')

    #########################################################
    # Coletando o horário em que a pessoa conversou com o bot
    #########################################################
    data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)

def responder(mensagem):
    texto = """
    Não entendi, escolha uma das opções:
    /opcao1 Conheça nossos produtos
    /opcao2 Mais informações
    /opcao3 Encontre o melhor produto para sua empresa
    Clique em uma das opções acima!
    """
    bot.reply_to(mensagem, texto)



bot.polling()