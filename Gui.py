# Importa o módulo tkinter, usado para criar interfaces gráficas em Python
import tkinter as tk

# Importa a classe Backend do módulo Backend (onde está o código do banco de dados)
from Backend import Backend

# Define uma classe chamada Gui para criar a interface gráfica
class Gui:
    # Método inicializador da classe, chamado ao criar o objeto da interface
    def __init__(self, master):
        # Armazena a janela principal (root) passada como argumento
        self.master = master
        # Define o título da janela
        self.master.title("Cadastro de Nomes")
        # Define o tamanho da janela (largura x altura)
        self.master.geometry("600x350")

        # Cria um rótulo (label) com o texto "Digite seu nome:" e adiciona à janela
        self.label = tk.Label(master, text="Digite seu nome:")
        self.label.pack(pady=5)  # Adiciona uma margem vertical de 5 pixels

        # Cria um campo de entrada de texto e adiciona à janela
        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)

        # Cria um botão com o texto "Salvar" e associa a função salvar_nome ao clique
        self.botao = tk.Button(master, text="Salvar", command=self.salvar_nome)
        self.botao.pack(pady=10)

        # Cria um rótulo vazio para mostrar mensagens ao usuário (ex: sucesso ou erro)
        self.mensagem = tk.Label(master, text="", fg="green")  # Cor padrão: verde
        self.mensagem.pack()

    # Função que será chamada ao clicar no botão "Salvar"
    def salvar_nome(self):
        # Pega o texto digitado no campo de entrada
        nome = self.entry.get()
        # Verifica se o nome não está em branco ou só com espaços
        if nome.strip():
            # Chama o método do Backend para salvar o nome no banco de dados
            Backend.salvar_nome(nome)
            # Exibe mensagem de sucesso
            self.mensagem.config(text="Nome salvo com sucesso!", fg="green")
            # Limpa o campo de entrada após salvar
            self.entry.delete(0, tk.END)
        else:
            # Se o campo estiver vazio, exibe uma mensagem de erro em vermelho
            self.mensagem.config(text="Por favor, digite um nome.", fg="red")
