# Info Clinicas

Sistema para Gestão de Clínicas

Aplicação disponível em https://info-clinicas-dev.herokuapp.com


## Stack
- Frontend
  - [Gentella CSS Framework](https://github.com/ColorlibHQ/gentelella)
- Backend
  - [Python 3.12](https://docs.python.org/pt-br/3/)
  - [Django 5.1](https://docs.djangoproject.com/pt-br/5.1/)
- Banco de Dados:
  - [PostgreSQL](https://www.postgresql.org/docs/current/index.html)


## Setup

Crie um virtualenv para o projeto e ative:
```bash
python3 -m venv .venv && source .venv/bin/activate
```

Como o virtualenv ativado, instale as dependências
```bash
pip3 install --upgrade pip && pip3 install -r requirements-dev.txt
```

## Rodando - Desenvolvimento

### Criar tabelas no banco de dados
```bash
python3 manage.py runserver makemigrations
python3 manage.py runserver migrate
```

### Inserindo dados de testes no banco
```bash
python3 manage.py criar_dados_de_teste
```
Isso irá criar um super usuário (`admin / admin`) e também:
- clinica de teste
- especialidades
- médicos
- pacientes
- disponibilidades
- agendamentos

### Rodando o servidor de desenvolvimento
```bash
python3 manage.py runserver
```

Acesse em: [http://localhost:8000](http://localhost:8000)

## Deploy

### Ambiente de DESENVOLVIMENTO

Deploy configurado para fazer automaticamente, conforme alterações na branch `dev`

Para fazer de forma manual rodar:
```bash
git push dev master
```

#### Disponível em
[https://info-clinicas-dev.herokuapp.com](https://info-clinicas-dev.herokuapp.com)


### Ambiente de PRODUÇÃO

Deploy configurado para fazer automaticamente, conforme alterações na branch `master`

Para fazer de forma manual rodar:
```bash
git push prod master
```

#### Disponível em
[https://info-clinicas.herokuapp.com/](https://info-clinicas.herokuapp.com/)
