def add_task(task, tasks):
    tasks.append({"task": task, "completed": False})
    return tasks


def view_tasks(tasks):
    if not tasks:
        return "No tasks available."
    else:
        return tasks


def complete_task(task_number, tasks):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        return tasks
    else:
        return "Invalid task number."


def delete_task(task_number, tasks):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        return tasks
    else:
        return "Invalid task number."
