
---

# 📘 Guia Rápido — Projeto Django

Este repositório contém um projeto Django. Abaixo estão instruções básicas para configurar e gerenciar o ambiente de desenvolvimento.

---

## 🚀 Iniciando o Projeto

Após clonar o repositório, execute o comando abaixo para configurar automaticamente o ambiente:

```bash
py initiate.py
```

Esse comando realiza as seguintes etapas:

* Cria o ambiente virtual
* Instala as dependências
* Aplica as migrações iniciais

> ⚠️ Use este comando **somente uma vez**, logo após clonar o projeto.

---

## 📦 Gerenciando Dependências

### Adicionou uma nova biblioteca?

Salve as dependências atualizadas com:

```bash
pip freeze > requirements.txt
```

> ⚠️ Faça isso apenas se você instalou novas bibliotecas com `pip install`.

### Precisa atualizar seu ambiente?

Se alguém da equipe atualizou as dependências no `requirements.txt`, rode:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Comandos Django

### Iniciar o servidor

```bash
py manage.py runserver
```

### Criar novas migrações (após alterar os modelos)

```bash
py manage.py makemigrations
```

### Aplicar migrações ao banco de dados

```bash
py manage.py migrate
```

---

