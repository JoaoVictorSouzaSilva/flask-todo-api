# 🧠 Flask To-Do API

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-%F0%9F%94%A5-lightgrey)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow)
![License](https://img.shields.io/badge/license-MIT-green)
![Last Commit](https://img.shields.io/github/last-commit/JoaoVictorSouzaSilva/flask-todo-api)

Bem-vindo ao meu primeiro projeto de backend com Flask! Essa API simples permite criar, listar, atualizar e deletar tarefas (CRUD) usando Python.

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
cd todo-api
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

## 🛠️ Futuras melhorias
- Interface Web com Flask ou React
- Autenticação de usuário
- Banco de dados SQLite ou PostgreSQL

---

## 📇 Contato

👨‍💻 João Victor de Souza Silva  
🔗 [Meu LinkedIn](https://www.linkedin.com/in/jo%C3%A3o-victor-souza-silva-9a6a2525b/)
🔗 [Meu Github](https://github.com/JoaoVictorSouzaSilva)

---
 
 ## Autor
João Victor de Souza Silva
=======
