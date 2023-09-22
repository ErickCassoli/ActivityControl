
# ActivityControl API

Api para controle de atividades atraves de alunos, sendo ela realizando CRUD para as 3 entidades disponiveis atraves de endpoints.

Tarefa Realizada por: Erick Moreira Cassoli de Souza
## Indice

- [Funcionalidades](#funcionalidades)
- [Setup](#setup)
- [Uso](#uso)
- [Documentação da API](#documentação-da-api)

## Funcionalidades

- Criar, Listar, Atualizar, Deletar Alunos
- Criar, Listar, Atualizar, Deletar Disciplinas
- Criar, Listar, Atualizar, Deletar Tarefas
- Listar Tarefas por Aluno


## Setup

Execute o arquivo Setup.bat atraves do terminal usando:
```
.\Setup.ps1
```
Caso de algum erro use primeiro esse comando:
```
Set-ExecutionPolicy Bypass -Scope Process
```

e execute o Setup.ps1 novamente.

Ele criara a .env e intalara os requirements automaticamente.

Caso ele não execute os comandos vc pode tentar fazer isso manualmente utilizando 
```
python -m venv .env

.\.env\Scripts\activate

pip install -r requirements.txt
```
## Uso
Para iniciar a api utilize:

```
python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```
após isso você pode fazer requisições atraves do postman ou da url em questão
a url padrão da api é localhost ou ```http://127.0.0.1:8000/```.

Apos isso voce pode importar as Colections da pasta "postmanCollections" para o seu proprio postman para testar.

## Documentação da API

### Retorna todos os alunos

```http
GET /api/alunos/
```

### Retorna um aluno específico

```http
GET /api/alunos/${id}/
```

| Parâmetro | Tipo   | Descrição             |
| --------- | ------ | -------------------- |
| `id`      | `int`  | **Obrigatório**. ID do aluno desejado |

### Adiciona um aluno

```http
POST /api/alunos/
```

Envie um JSON contendo os detalhes do aluno a ser adicionado.

### Atualiza um aluno

```http
PUT /api/alunos/${id}/
```

| Parâmetro | Tipo   | Descrição             |
| --------- | ------ | -------------------- |
| `id`      | `int`  | **Obrigatório**. ID do aluno a ser atualizado |

Envie um JSON contendo os detalhes atualizados do aluno.

### Remove um aluno

```http
DELETE /api/alunos/${id}/
```

| Parâmetro | Tipo   | Descrição             |
| --------- | ------ | -------------------- |
| `id`      | `int`  | **Obrigatório**. ID do aluno a ser removido |

### Retorna as tarefas de um aluno específico

```http
GET /api/alunos/${id}/tarefas/
```

| Parâmetro | Tipo   | Descrição             |
| --------- | ------ | -------------------- |
| `id`      | `int`  | **Obrigatório**. ID do aluno desejado |

### Retorna todas as disciplinas

```http
GET /api/disciplinas/
```

### Retorna uma disciplina específica

```http
GET /api/disciplinas/${id}/
```

| Parâmetro | Tipo   | Descrição             |
| --------- | ------ | -------------------- |
| `id`      | `int`  | **Obrigatório**. ID da disciplina desejada |

### Adiciona uma disciplina

```http
POST /api/disciplinas/
```

Envie um JSON contendo os detalhes da disciplina a ser adicionada.

### Atualiza uma disciplina

```http
PUT /api/disciplinas/${id}/
```

| Parâmetro | Tipo   | Descrição             |
| --------- | ------ | -------------------- |
| `id`      | `int`  | **Obrigatório**. ID da disciplina a ser atualizada |

Envie um JSON contendo os detalhes atualizados da disciplina.

### Remove uma disciplina

```http
DELETE /api/disciplinas/${id}/
```

| Parâmetro | Tipo   | Descrição             |
| --------- | ------ | -------------------- |
| `id`      | `int`  | **Obrigatório**. ID da disciplina a ser removida |

### Retorna todas as tarefas

```http
GET /api/tarefas/
```

### Retorna uma tarefa específica

```http
GET /api/tarefas/${id}/
```

| Parâmetro | Tipo   | Descrição             |
| --------- | ------ | -------------------- |
| `id`      | `int`  | **Obrigatório**. ID da tarefa desejada |

### Adiciona uma tarefa

```http
POST /api/tarefas/
```

Envie um JSON contendo os detalhes da tarefa a ser adicionada.

### Atualiza uma tarefa

```http
PUT /api/tarefas/${id}/
```

| Parâmetro | Tipo   | Descrição             |
| --------- | ------ | -------------------- |
| `id`      | `int`  | **Obrigatório**. ID da tarefa a ser atualizada |

Envie um JSON contendo os detalhes atualizados da tarefa.

### Remove uma tarefa

```http
DELETE /api/tarefas/${id}/
```

| Parâmetro | Tipo   | Descrição             |
| --------- | ------ | -------------------- |
| `id`      | `int`  | **Obrigatório**. ID da tarefa a ser removida |
