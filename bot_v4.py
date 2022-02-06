#########################################################
# Este código traz a estrutura de conversa de um chatbot
# que faz a captura de informações de um cliente e verifica se ele é um possível lead qualificado.
# Material confeccionado para o TCC do curso de Especialização em IA da Puc Minas
#
# Kelly M. O. Lopes
# Campinas, 06 janeiro de 2022.
#########################################################
# Importando bilbliocas
import requests
import json
#import time
import pandas as pd

# Variaveis auxiliares
aux = []
aux2 = []

# Classe que instância o Bot com a API do Telegram
class TelegramBot:
    def __init__(self):
        token = '5060316690:AAHT4YuNvXGUEk6c9-exoUQAxYUie1IXXpE'
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    # Função que pega as mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)


    # Função que capta as perguntas que são inputadas pelo usuário
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        print('mensagem do cliente:' + str(mensagem)) # visualizar as respostas do usuário


        # Salvando o conjunto de dados do usuário
        aux.append(mensagem)
        dataset = pd.DataFrame(aux).T
        dataset.to_csv(r'C:\Users\kelly\PycharmProjects\pythonProject1\dataset_v4.csv', sep=',', index=False, encoding='utf-8')



        # Mensagem inicial do Bot
        if eh_primeira_mensagem == True or mensagem.lower() in ('oi', 'olá','o', 'bom dia','boa tarde','boa noite'):
            return f'''Oi tudo  bem 😃 ?
            Eu sou o bot da Atlas.
            Por favor,  digite uma das opções:
            1-Conheça nossos produtos
            2-Mais informações
            3-Encontre o melhor produto para sua empresa'''

        # Condição que trata da primeira lista de opções oferecida pelo Bot
        if mensagem == '1':
            return f'''Nós temos os seguintes produtos:
            4-Basic 
            5-Entreprise 
            6-Professional 
            Digite um dos valores.'''

        # Condição que trata do primeiro iten oferecido pelo lista de opções do Bot
        if mensagem == '4':
            return f''' O plano Basic é ideal para empresas de pequeno porte e que realizam ✍️ poucas reuniões durante o ano.'''

        # Condição que trata do segundo iten oferecido pelo lista de opções do Bot
        if mensagem == '5':
            return f'''Com o plano Enterprise, é possível criar reuniões, fazer o gerenciamento das pautas e das deliberações, convocar os participantes; tudo isso em menos de 🕜  três minutos.'''

        # Condição que trata do terceiro iten oferecido pelo lista de opções do Bot
        if mensagem == '6':
            return f'''Já com o plano Professional, além do usuário conseguir fazer toda a gestão de suas reuniões, ele também consegue assinar as Atas e os documentos, utilizando nosso sistema de Assinatura Eletrônica 📝.'''


        # Condição que trata da segunda opção da lista de oferecida pelo Bot
        elif mensagem == '2':
            return f'''Para mais informações acesse: https://welcome.atlasgov.com/pt'''


        # Condição que trata da terceira opção da lista de oferecida pelo Bot
        # Juntamente com as perguntas de validação da empresa
        if mensagem == '3':
            return f'''Digite o nome da empresa.'''
        elif ('a' or 'b' or 'c' or 'e' or 'd') in mensagem.lower():
            return f'''Digite o número de telefone com o DDD.'''
        elif len(mensagem) > 6:
            return f'''A empresa faz uso de Assinatura Eletronica? Digite "7"-Sim ou "8"-Não'''
        elif (mensagem =='7' or mensagem =='8'):
            return f'''A empresa possui Comitês? Digite "9"-Sim ou "10"-Não'''
        elif mensagem =='9':
            return f'''O melhor produto 😃 para a sua empresa é o Plano Professional. Seja muito bem vindo a Atlas Governance, um de nossos gerentes irá entrar em contato com você 😉.'''
        elif mensagem == '10':
            return f'''A empresa possui Assembleias? Digite "11"-Sim ou "12"-Não'''
        elif mensagem == '11':
            return f'''O melhor produto 😃 para a sua empresa é o Plano Enterprise. Seja muito bem vindo a Atlas Governance, um de nossos gerentes irá entrar em contato com você 😉.'''
        elif mensagem == '12':
            return f'''A empresa faz uso de Atas? Digite "13"-Sim ou "14"-Não'''
        elif mensagem == '13':
            return f'''O melhor produto 😃 para a sua empresa é o Plano Basic. Seja muito bem vindo a Atlas Governance, um de nossos gerentes irá entrar em contato com você 😉.'''
        elif mensagem == '14':
            return f'''Desculpe 😥, mas a  sua empresa ainda não possui estrutura para utilizar nossos produtos. Entre em nosso site 🤗, podemos te ajudar estruturando o seu conselho.'''
        else:
            return f'''Por favor, digite uma das opções!'''



    # Bot responde as perguntas do usuário
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)
        print('Bot:' + str(resposta)) # visualizar as respostas do Bot

        # Salvando o resultado da qualificação do lead
        aux2.append(resposta)
        dataset2 = pd.DataFrame(aux2)
        dataset2.columns = ['Resultado da Qualificaçã']
        dataset2.to_csv(r'C:\Users\kelly\PycharmProjects\pythonProject1\dataset2_v4.csv', sep=',', index=False, encoding='utf-8')


# Inicializando o Bot
bot = TelegramBot()
bot.Iniciar()



