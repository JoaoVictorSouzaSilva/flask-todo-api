# 🧠 Flask To-Do API

Bem-vindo ao meu primeiro projeto de backend com Flask! Essa API simples permite criar, listar, atualizar e deletar tarefas (CRUD) usando Python.

> 💬 **Meu começo como Desenvolvedor**
>
> Este projeto marca o início da minha jornada com backend em Python. Ele foi criado com o objetivo de aprender, praticar e compartilhar!

---

## 🚀 Tecnologias Usadas

- Python 🐍
- Flask 🔥
- JSON para persistência de dados

---

## 📦 Como rodar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/JoaoVictorSouzaSilva/flask-todo-api.git
cd flask-todo-api
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install flask
```

4. Execute a aplicação:
```bash
python app.py
```

A API estará disponível em: `http://127.0.0.1:5000`

---

## 🧪 Testando a API com `curl`

- Criar tarefa:
```bash
curl -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d "{\"title\": \"Nova tarefa\"}"
```

- Listar tarefas:
```bash
curl http://127.0.0.1:5000/tasks
```

- Atualizar tarefa (id 1):
```bash
curl -X PUT http://127.0.0.1:5000/tasks/1 -H "Content-Type: application/json" -d "{\"done\": true}"
```

- Deletar tarefa (id 1):
```bash
curl -X DELETE http://127.0.0.1:5000/tasks/1
```

---

## 📇 Contato

👨‍💻 João Victor Souza Silva  
🔗 [Meu LinkedIn](https://www.linkedin.com/in/jo%C3%A3o-victor-souza-silva-9a6a2525b/)

---

## 🛠️ Futuras melhorias
- Interface Web com Flask ou React
- Autenticação de usuário
- Banco de dados SQLite ou PostgreSQL
