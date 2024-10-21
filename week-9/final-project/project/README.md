# Simple Todo List CLI Application for CS50P

#### Video Demo:  [Preview](https://youtu.be/qQKSP1EPCTQ)

#### Description:
This is a command-line interface (CLI) application built with Python and the `Click` library to help users manage a simple to-do list. The application allows users to add, view, complete, and delete tasks, storing them in a local JSON file for persistence between sessions.

The project is structured to separate the logic from the interface, making the code easy to test and maintain. Each function is designed to return values, which facilitates unit testing. 

#### Key Features:
- **Add Tasks**: Add new tasks to your to-do list.
- **View Tasks**: Display all tasks, indicating their completion status.
- **Mark Tasks as Complete**: Mark specific tasks as completed.
- **Delete Tasks**: Remove tasks from the list.

#### How to Install:
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd todo-list-cli
    ```

2. Install the required Python packages:
    ```bash
    pip install click
    ```

3. Optionally, run the tests:
    ```bash
    pytest test_project.py
    ```

#### How to Use:
The following commands are available:

- **Add a Task:**
    ```bash
    python project.py add "Your task description"
    ```

- **View Tasks:**
    ```bash
    python project.py view
    ```

- **Complete a Task:**
    ```bash
    python project.py complete <task_number>
    ```

- **Delete a Task:**
    ```bash
    python project.py delete <task_number>
    ```

#### Example:
```bash
$ python project.py add "Learn Python"
Task added: Learn Python

$ python project.py view
1. Learn Python [✗]

$ python project.py complete 1
Task 1 marked as complete!

$ python project.py view
1. Learn Python [✓]

$ python project.py delete 1
Task 1 deleted successfully!

$ python project.py view
No tasks available.
