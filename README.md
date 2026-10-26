# Python To-Do List App

A beginner-friendly command-line To-Do List application built with Python. Add tasks, view pending tasks, mark tasks as completed, and delete tasks through a simple menu.

## Features

- **Add tasks** to your pending list.
- **View tasks**, separated into pending and completed tasks.
- **Complete tasks** by selecting their number.
- **Delete pending tasks** that you no longer need.
- **Input validation** for menu choices and task numbers.
- **Simple terminal interface** with no third-party packages required.

## Requirements

- Python **3.10 or newer** (the project uses `match-case`).
- A terminal. VS Code is optional.

## Run the app

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python3 main.py
   ```

   On Windows, you can also try:

   ```bash
   python main.py
   ```

## Menu

```text
===== TO-DO LIST =====
1. Add task
2. View tasks
3. Complete task
4. Delete task
5. Exit
```

## Concepts practiced

- Variables and user input
- Lists and list methods (`append()` and `pop()`)
- `while` and `for` loops
- `if-else` conditions
- `match-case`
- `enumerate()`
- Exception handling with `try-except`
- Basic input validation

## Current limitations

Tasks are stored in memory, so they reset when you close the program. The completed list is also temporary. Saving tasks permanently with JSON is a useful next improvement.

## Planned improvements

- Save and load tasks using JSON.
- Add task priorities and due dates.
- Allow users to restore or delete completed tasks.
- Add automated tests.

## Project structure

```text
python-todo-list/
├── main.py
├── README.md
├── .gitignore
└── LICENSE
```

## License

This project is available under the MIT License. See [`LICENSE`](LICENSE).

---

Built by Sumit as a Python practice project.
