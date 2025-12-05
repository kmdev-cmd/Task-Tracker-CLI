import json
import os
import sys
import datetime

TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as f:
            json.dump([], f, indent=4)
    with open(TASKS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            with open(TASKS_FILE, "w") as f2:
                json.dump([], f2, indent=4)
            return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(description):
    tasks = load_tasks()
    new_id = 1 if not tasks else max(task["id"] for task in tasks) + 1
    now = datetime.datetime.now().isoformat()
    tasks.append({
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now,
    })
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")


def list_tasks(filter=None):
    tasks = load_tasks()
    if filter and filter.lower() == "none":
        filter = None
    for task in tasks:
        if not filter or task["status"].lower() == filter.lower():
            print(f"[{task['id']}] {task['description']} — {task['status']}")


def update_task(task_id, new_description):
    tasks = load_tasks()
    task_id = int(task_id)
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} atualizada com sucesso")
            return
    print(f"Task {task_id} não encontrada")


def delete_task(task_id):
    tasks = load_tasks()
    task_id = int(task_id)
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task {task_id} deletada com sucesso")
            return
    print(f"Task {task_id} não encontrada")


def update_status(task_id, new_status):
    allowed = ["todo", "in-progress", "done"]
    if new_status not in allowed:
        print("Status inválido. Use: todo, in-progress ou done")
        return
    tasks = load_tasks()
    task_id = int(task_id)
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = datetime.datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} alterada para {new_status}")
            return
    print(f"Task {task_id} não encontrada")


def main():
    if len(sys.argv) < 2:
        print("Uso: python task-cli.py [comando] [args]")
        sys.exit()

    command = sys.argv[1]
    args = sys.argv[2:]

    commands = {
        "add": lambda: add_task(" ".join(args)) if args else print("Uso: add <descrição>"),
        "update": lambda: update_task(args[0], " ".join(args[1:])) if len(args) >= 2 else print("Uso: update <id> <nova descrição>"),
        "delete": lambda: delete_task(args[0]) if args else print("Uso: delete <id>"),
        "list": lambda: list_tasks(args[0]) if args else list_tasks(),
        "mark-in-progress": lambda: update_status(args[0], "in-progress") if args else print("Uso: mark-in-progress <id>"),
        "mark-done": lambda: update_status(args[0], "done") if args else print("Uso: mark-done <id>")
    }

    if command in commands:
        commands[command]()
    else:
        print("Comando inválido. Comandos disponíveis: add, update, delete, list, mark-in-progress, mark-done")


if __name__ == "__main__":
    main()
