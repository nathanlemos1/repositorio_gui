# 📘 Explicação do Funcionamento do Código: Cadastro de Nomes com Tkinter + SQLite

Este projeto é uma aplicação simples que permite cadastrar nomes por meio de uma interface gráfica feita com **Tkinter**, armazenando esses dados em um banco local **SQLite**. A aplicação é dividida em três arquivos principais: `Backend.py`, `Gui.py` e `main.py`.

---

## 🧠 Como o projeto funciona?

### 1️⃣ Backend.py - Banco de Dados

Este arquivo contém uma classe chamada `Backend`, responsável por tudo que envolve o banco de dados.

- **Criação do Banco e Tabela:**  
  Ao iniciar, ele cria um banco de dados chamado `nomes.db`, e dentro dele, uma tabela chamada `pessoas`, com duas colunas: `id` (chave primária) e `nome` (campo obrigatório).

- **Inserção de Dados:**  
  O método `salvar_nome` é usado para inserir nomes digitados pelo usuário dentro da tabela `pessoas`.

---

### 2️⃣ Gui.py - Interface Gráfica

Este arquivo define a interface visual da aplicação usando a biblioteca Tkinter.

- **Componentes da Janela:**
  - Um rótulo que orienta o usuário a digitar o nome.
  - Um campo de entrada onde o nome é digitado.
  - Um botão "Salvar" que envia o nome para o banco.
  - Um rótulo de mensagem que exibe avisos de sucesso ou erro.

- **Validação:**
  Antes de salvar, o programa verifica se o campo de entrada está vazio. Se estiver, mostra uma mensagem de erro. Se estiver preenchido, chama o `Backend` para salvar o nome e limpa o campo após o envio.

---

### 3️⃣ main.py - Execução da Aplicação

Este é o arquivo principal que deve ser executado.

- Inicializa o banco de dados, garantindo que a tabela esteja pronta.
- Cria a janela principal da interface.
- Inicia a aplicação gráfica com um loop que mantém a janela aberta até o usuário fechá-la.

---

## 🔁 Fluxo de Uso da Aplicação

1. O usuário executa o programa (`main.py`).
2. A interface gráfica aparece com um campo para digitar nomes.
3. O usuário digita um nome e clica em **Salvar**.
4. O sistema verifica se o campo está preenchido:
   - Se sim, o nome é salvo no banco de dados.
   - Se não, uma mensagem de erro aparece.
5. Uma mensagem informa que o nome foi salvo com sucesso e o campo é limpo.

---

## ✅ Funcionalidades Implementadas

- Criação automática do banco e tabela se não existirem.
- Interface gráfica amigável com campo de entrada e botão.
- Validação do campo de entrada para evitar nomes em branco.
- Inserção de dados no banco de forma segura.
- Exibição de mensagens de feedback ao usuário (sucesso ou erro).

---

## 📦 O que é gerado?

- Um banco de dados local chamado `nomes.db`
- Uma tabela chamada `pessoas`
- Uma interface gráfica simples e funcional para entrada de dados

---

**Explicação criada por Nathan Lemos ✨**
