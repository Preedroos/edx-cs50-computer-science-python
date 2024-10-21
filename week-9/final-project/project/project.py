import click
import json
import os
from todo import add_task, view_tasks, complete_task, delete_task


TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as f:
                tasks = json.load(f)
                if isinstance(tasks, list):
                    return tasks
                else:
                    return []
        except json.JSONDecodeError:
            return []
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f)


@click.group()
def main():
    pass


@main.command()
@click.argument("task")
def add(task):
    tasks = load_tasks()
    updated_tasks = add_task(task, tasks)
    save_tasks(updated_tasks)
    click.echo(f"Task added: {task}")


@main.command()
def view():
    tasks = load_tasks()
    result = view_tasks(tasks)
    if isinstance(result, str):
        click.echo(result)
    else:
        for i, task in enumerate(result, 1):
            status = "✓" if task["completed"] else "✗"
            click.echo(f"{i}. {task['task']} [{status}]")


@main.command()
@click.argument("task_number", type=int)
def complete(task_number):
    tasks = load_tasks()
    result = complete_task(task_number, tasks)

    if isinstance(result, str):
        click.echo(result)
    else:
        save_tasks(result)
        click.echo(f"Task {task_number} marked as complete!")


@main.command()
@click.argument("task_number", type=int)
def delete(task_number):
    tasks = load_tasks()
    result = delete_task(task_number, tasks)

    if isinstance(result, str):
        click.echo(result)
    else:
        save_tasks(result)
        click.echo(f"Task {task_number} deleted successfully!")


if __name__ == "__main__":
    main()
