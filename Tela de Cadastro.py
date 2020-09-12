import PySimpleGUI as sg
from time import sleep

class Cadastro:
    def __init__(self):
        sg.change_look_and_feel('Dark')
        #layout
        layout = [
            [sg.Text('Nome', size=(10, 0)), sg.Input(size=(15, 0), key='Nome')],
            [sg.Text('Email', size=(10, 0)), sg.Input(size=(15, 0), key='Email')],
            [sg.Text('Idade', size=(10, 0)), sg.Input(size=(15, 0), key='Idade')],
            [sg.Text('Senha', size=(10, 0)), sg.Input(size=(15, 0), key='Senha')],
            [sg.Text('Confime a senha', size=(10, 0)), sg.Input(size=(15, 0), key='Confir')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30, 15))]
        ]
        self.janela = sg.Window('Cadastro').layout(layout)
        self.button, self.values = self.janela.Read()

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            Nome = self.values['Nome']
            Email = self.values['Email']
            Idade = self.values['Idade']
            Senha = self.values['Senha']
            Confir = self.values['Confir']
            if Nome and Email and Idade and Senha and Confir != '':
                if Confir != Senha:
                    print("Analisando...")
                    sleep(2)
                    print("Senha e Confirmação não são iguais")
                    print("Insira a confirmação novamente")
                    print("-=-"*13)
                if Confir == Senha:
                    print("Analisando...")
                    sleep(2)
                    print("Salvando dados...")
                    sleep(3)
                    print("Dados Cadastrados")
                    print(f"Bem vindo, {Nome}")
            else:
                print("Existem dados não preenchidos")
            print("-=-"*13)
tela = Cadastro()
tela.Iniciar()
