# Task Tracker CLI

Gerenciador de tarefas via linha de comando (CLI) em Python. Permite adicionar, atualizar, deletar, marcar status e listar tarefas salvas em JSON.

## Como usar

```bash
# Adicionar
python task-cli.py add "Comprar leite"

# Atualizar
python task-cli.py update 1 "Comprar leite e pão"

# Deletar
python task-cli.py delete 1

# Marcar status
python task-cli.py mark-in-progress 2
python task-cli.py mark-done 2

# Listar
python task-cli.py list
python task-cli.py list done
python task-cli.py list todo
python task-cli.py list in-progress
