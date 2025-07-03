# Importa o módulo sqlite3, que permite trabalhar com bancos de dados SQLite
import sqlite3

# Define uma classe chamada Backend para agrupar os métodos relacionados ao banco de dados
class Backend:
    
    # Método estático para inicializar o banco de dados e criar a tabela, se não existir
    @staticmethod
    def initDB():
        # Cria uma conexão com o banco de dados 'nomes.db' (será criado se não existir)
        conexao = sqlite3.connect("nomes.db")
        # Cria um cursor para executar comandos SQL
        cursor = conexao.cursor()
        # Executa um comando SQL para criar a tabela 'pessoas' se ela ainda não existir
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Campo ID autoincrementável (chave primária)
                nome TEXT NOT NULL                     -- Campo nome do tipo texto e obrigatório
            )
        """)
        # Salva as alterações feitas no banco de dados
        conexao.commit()
        # Fecha a conexão com o banco de dados
        conexao.close()

    # Método estático para salvar um nome na tabela 'pessoas'
    @staticmethod
    def salvar_nome(nome):
        # Abre uma nova conexão com o banco de dados 'nomes.db'
        conexao = sqlite3.connect("nomes.db")
        # Cria um cursor para executar comandos SQL
        cursor = conexao.cursor()
        # Executa o comando SQL para inserir o nome na tabela 'pessoas'
        cursor.execute("INSERT INTO pessoas (nome) VALUES (?)", (nome,))
        # Salva as alterações feitas no banco de dados
        conexao.commit()
        # Fecha a conexão com o banco de dados
        conexao.close()
