# Importa o módulo tkinter para criar a interface gráfica
import tkinter as tk

# Importa a classe Gui do módulo Gui (interface gráfica)
from Gui import Gui

# Importa a classe Backend do módulo Backend (operações com banco de dados)
from Backend import Backend

# Função principal do programa
def main():
    # Inicializa o banco de dados, criando a tabela se ainda não existir
    Backend.initDB()
    
    # Cria a janela principal da aplicação (root)
    root = tk.Tk()
    
    # Cria um objeto da interface gráfica, passando a janela principal
    app = Gui(root)
    
    # Inicia o loop principal da interface gráfica (janela ficará aberta)
    root.mainloop()

# Verifica se este arquivo está sendo executado diretamente
if __name__ == "__main__":
    # Se sim, chama a função principal para iniciar o programa
    main()
