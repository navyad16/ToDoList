#To-Do List(CLI with File Persistence)
#Built a simple task management app using only Python
#Features include taskcreation, completion, deletion, and permanent storage using a text file.
"""TODO_FILE = "todo_tasks.txt"
# Load tasks from file
def load_tasks():
    try:
        with open(TODO_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Main to-do functionality
def todo_list():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            if not tasks:
                print("No tasks yet.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "2":
            new_task = input("Enter new task: ")
            tasks.append("[ ] " + new_task)
            save_tasks(tasks)
            print("Task added.")

        elif choice == "3":
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                idx = int(input("Enter task number to mark as done: ")) - 1
                if tasks[idx].startswith("[x]"):
                    print("Task already marked as done.")
                else:
                    tasks[idx] = tasks[idx].replace("[ ]", "[x]", 1)
                    save_tasks(tasks)
                    print("Task marked as done.")
            except (IndexError, ValueError):
                print("Invalid task number.")

        elif choice == "4":
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                idx = int(input("Enter task number to delete: ")) - 1
                removed = tasks.pop(idx)
                save_tasks(tasks)
                print(f"Deleted: {removed}")
            except (IndexError, ValueError):
                print("Invalid task number.")

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

# Run app
todo_list()
"""
###############################################  CSV    ##########################################################
#To-Do List with CSV Storage Built a CLI - based task manager in Python that supports
#adding, viewing, updating, and deleting tasks.
#Used the csv module to store tasks persistently with status tracking.
import csv
import os

CSV_FILE = "todo_tasks.csv"

# Load tasks from CSV
def load_tasks():
    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, mode="r", newline="") as file:
        reader = csv.reader(file)
        return list(reader)

# Save tasks to CSV
def save_tasks(tasks):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(tasks)

# Main To-Do List function
def todo_app():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            if not tasks:
                print("No tasks available.")
            else:
                for i, task in enumerate(tasks, 1):
                    status = "✅" if task[1] == "done" else "❌"
                    print(f"{i}. {task[0]} [{status}]")

        elif choice == '2':
            new_task = input("Enter task description: ").strip()
            if new_task:
                tasks.append([new_task, "pending"])
                save_tasks(tasks)
                print("Task added.")

        elif choice == '3':
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task[0]} [{'✅' if task[1] == 'done' else '❌'}]")
            try:
                index = int(input("Enter task number to mark as done: ")) - 1
                if 0 <= index < len(tasks):
                    tasks[index][1] = "done"
                    save_tasks(tasks)
                    print("Task marked as done.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Enter a valid number.")

        elif choice == '4':
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task[0]}")
            try:
                index = int(input("Enter task number to delete: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    save_tasks(tasks)
                    print(f"Deleted: {removed[0]}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Enter a valid number.")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the app
todo_app()

"""
###########################################  Pandas   ############################################################
# ******** To-DoList with Pandas CSV Management  ************
#Built a command - line task manager in Python using the pandas library.Implemented task CRUD operations
#with CSV persistence and clean user interaction.

import pandas as pd
import os

CSV_FILE = "todo_tasks.csv"

# Load CSV into DataFrame
def load_tasks():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else:
        return pd.DataFrame(columns=["Task", "Status"])

# Save DataFrame to CSV
def save_tasks(df):
    df.to_csv(CSV_FILE, index=False)

# Main App
def todo_app():
    df = load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            if df.empty:
                print("No tasks found.")
            else:
                for i, row in df.iterrows():
                    status = "✅" if row["Status"] == "done" else "❌"
                    print(f"{i + 1}. {row['Task']} [{status}]")

        elif choice == "2":
            task = input("Enter new task: ").strip()
            if task:
                df = pd.concat([df, pd.DataFrame([[task, "pending"]], columns=["Task", "Status"])], ignore_index=True)
                save_tasks(df)
                print("Task added.")

        elif choice == "3":
            if df.empty:
                print("No tasks to mark.")
            else:
                print(df[["Task", "Status"]].reset_index().to_string(index=False))
                try:
                    index = int(input("Enter task number to mark as done: ")) - 1
                    if 0 <= index < len(df):
                        df.at[index, "Status"] = "done"
                        save_tasks(df)
                        print("Task marked as done.")
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            if df.empty:
                print("No tasks to delete.")
            else:
                print(df[["Task", "Status"]].reset_index().to_string(index=False))
                try:
                    index = int(input("Enter task number to delete: ")) - 1
                    if 0 <= index < len(df):
                        deleted = df.iloc[index]["Task"]
                        df = df.drop(index).reset_index(drop=True)
                        save_tasks(df)
                        print(f"Deleted: {deleted}")
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "5":
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid choice. Try again.")

# Run the App
todo_app()

############################################  Statusfilter  #####################################################
#Pandas-Based To-Do List with CSV Filtering Developed a Python CLI To-Do List using the pandas library with CRUD functionality.
#Implemented dynamic filtering by task status (pending or done) and persistent CSV storage.

CSV_FILE = "todo_tasks.csv"

def load_tasks():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else:
        return pd.DataFrame(columns=["Task", "Status"])

def save_tasks(df):
    df.to_csv(CSV_FILE, index=False)

def todo_app():
    df = load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View All Tasks")
        print("2. View Tasks by Status")
        print("3. Add Task")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            if df.empty:
                print("No tasks found.")
            else:
                for i, row in df.iterrows():
                    status = "✅" if row["Status"] == "done" else "❌"
                    print(f"{i + 1}. {row['Task']} [{status}]")

        elif choice == "2":
            status_filter = input("Enter status to filter by (pending/done): ").strip().lower()
            if status_filter not in ["pending", "done"]:
                print("Invalid status. Use 'pending' or 'done'.")
            else:
                filtered = df[df["Status"] == status_filter]
                if filtered.empty:
                    print(f"No {status_filter} tasks.")
                else:
                    for i, row in filtered.iterrows():
                        print(f"{i + 1}. {row['Task']} [{'✅' if row['Status'] == 'done' else '❌'}]")

        elif choice == "3":
            task = input("Enter new task: ").strip()
            if task:
                df = pd.concat([df, pd.DataFrame([[task, "pending"]], columns=["Task", "Status"])], ignore_index=True)
                save_tasks(df)
                print("Task added.")

        elif choice == "4":
            if df.empty:
                print("No tasks to mark.")
            else:
                for i, row in df.iterrows():
                    print(f"{i + 1}. {row['Task']} [{'✅' if row['Status'] == 'done' else '❌'}]")
                try:
                    index = int(input("Enter task number to mark as done: ")) - 1
                    if 0 <= index < len(df):
                        df.at[index, "Status"] = "done"
                        save_tasks(df)
                        print("Task marked as done.")
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "5":
            if df.empty:
                print("No tasks to delete.")
            else:
                for i, row in df.iterrows():
                    print(f"{i + 1}. {row['Task']}")
                try:
                    index = int(input("Enter task number to delete: ")) - 1
                    if 0 <= index < len(df):
                        deleted = df.iloc[index]["Task"]
                        df = df.drop(index).reset_index(drop=True)
                        save_tasks(df)
                        print(f"Deleted: {deleted}")
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "6":
            print("Exiting To-Do List.")
            break

        else:
            print("Invalid choice. Try again.")

# Run the app
todo_app()

############################################### DueDateSorting ####################################################

#To-Do List App with Due Date Sorting (Python + Pandas)
#Built a command-line task manager using pandas,with full CRUD operations and persistent CSV storage.
#Implemented date handling, sorting by due date, and status-based task filtering.

import pandas as pd
import os
from datetime import datetime

CSV_FILE = "todo_tasks.csv"
DATE_FORMAT = "%Y-%m-%d"  # e.g., 2025-07-01

def load_tasks():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE, parse_dates=["Due Date"])
    else:
        return pd.DataFrame(columns=["Task", "Status", "Due Date"])

def save_tasks(df):
    df.to_csv(CSV_FILE, index=False, date_format=DATE_FORMAT)

def todo_app():
    df = load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View All Tasks")
        print("2. View Tasks by Status")
        print("3. Add Task with Due Date")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Sort Tasks by Due Date")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            if df.empty:
                print("No tasks found.")
            else:
                for i, row in df.iterrows():
                    due = row['Due Date'].strftime(DATE_FORMAT) if not pd.isna(row['Due Date']) else "No due date"
                    status = "✅" if row["Status"] == "done" else "❌"
                    print(f"{i + 1}. {row['Task']} [{status}] - Due: {due}")

        elif choice == "2":
            status_filter = input("Enter status to filter by (pending/done): ").strip().lower()
            if status_filter not in ["pending", "done"]:
                print("Invalid status. Use 'pending' or 'done'.")
            else:
                filtered = df[df["Status"] == status_filter]
                if filtered.empty:
                    print(f"No {status_filter} tasks.")
                else:
                    for i, row in filtered.iterrows():
                        due = row['Due Date'].strftime(DATE_FORMAT) if not pd.isna(row['Due Date']) else "No due date"
                        print(f"{i + 1}. {row['Task']} [{status_filter}] - Due: {due}")

        elif choice == "3":
            task = input("Enter task description: ").strip()
            due_input = input(f"Enter due date (YYYY-MM-DD) or leave blank: ").strip()
            try:
                due_date = datetime.strptime(due_input, DATE_FORMAT) if due_input else pd.NaT
                new_row = pd.DataFrame([[task, "pending", due_date]], columns=["Task", "Status", "Due Date"])
                df = pd.concat([df, new_row], ignore_index=True)
                save_tasks(df)
                print("Task added.")
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")

        elif choice == "4":
            if df.empty:
                print("No tasks to mark.")
            else:
                for i, row in df.iterrows():
                    print(f"{i + 1}. {row['Task']} [{'✅' if row['Status'] == 'done' else '❌'}]")
                try:
                    index = int(input("Enter task number to mark as done: ")) - 1
                    if 0 <= index < len(df):
                        df.at[index, "Status"] = "done"
                        save_tasks(df)
                        print("Task marked as done.")
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "5":
            if df.empty:
                print("No tasks to delete.")
            else:
                for i, row in df.iterrows():
                    print(f"{i + 1}. {row['Task']}")
                try:
                    index = int(input("Enter task number to delete: ")) - 1
                    if 0 <= index < len(df):
                        deleted = df.iloc[index]["Task"]
                        df = df.drop(index).reset_index(drop=True)
                        save_tasks(df)
                        print(f"Deleted: {deleted}")
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "6":
            if df.empty:
                print("No tasks to sort.")
            else:
                df = df.sort_values(by="Due Date", na_position='last').reset_index(drop=True)
                save_tasks(df)
                print("Tasks sorted by due date.")

        elif choice == "7":
            print("Exiting To-Do List.")
            break

        else:
            print("Invalid choice. Try again.")

# Run the app
todo_app()
"""