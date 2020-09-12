import PySimpleGUI as sg

class Cadastro:
    def __init__(self):
        sg.change_look_and_feel('Dark')
        #layout
        layout = [
            [sg.Text('Nome', size=(5, 0)), sg.Input(size=(15, 0), key='Nome')],
            [sg.Text('Idade', size=(5, 0)), sg.Input(size=(15, 0), key='Idade')],
            [sg.Text('Quais provedores de E-mail são aceitos?')],
            [sg.Checkbox('Gmail', key='Gmail'), sg.Checkbox('Outlook', key='Outlook'), sg.Checkbox('Yahoo', key='Yahoo')],
            [sg.Text('Aceita cartão?')],
            [sg.Checkbox('Quero cartão', key='AceitaCartao'), sg.Checkbox('Não quero cartão', key='NaoAceitaCartao')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30, 15))]
        ]
        self.janela = sg.Window('Dados Do Usuário').layout(layout)
        self.button, self.values = self.janela.Read()

    def Iniciar(self):
            while True:
                self.button, self.values = self.janela.Read()
                nome = self.values['Nome']
                idade = self.values['Idade']
                aceita_gmail = self.values['Gmail']
                aceita_outlook = self.values['Outlook']
                aceita_yahoo = self.values['Yahoo']
                aceita_cartao = self.values['AceitaCartao']
                nao_aceita_cartao = self.values['NaoAceitaCartao']
                print(f"Nome: {nome}")
                print(f"Idade: {idade}")
                if aceita_gmail == True:
                    print("Aceita Gmail")
                if aceita_outlook == True:
                    print("Aceita Outlook")
                if aceita_yahoo == True:
                    print("Aceita Yahoo")
                if aceita_cartao == True:
                    print("Aceita Cartão")
                if nao_aceita_cartao == True:
                    print("Não aceita Cartão")
                print('-=-'*20)

tela = Cadastro()
tela.Iniciar()
