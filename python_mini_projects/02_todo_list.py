# ============================================================
# MINI PROJECT 2 — To-Do List (saves to a file)
# Uses: lists, functions, loops, file handling, conditionals
# ============================================================

import os

FILENAME = "todo_list.txt"


def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as f:
        lines = f.readlines()
        return [line.strip() for line in lines] # return as list


def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def show_tasks(tasks):      # Will take list form load_tasks fxn
    if not tasks:
        print("No tasks yet!")
        return
    print("\n--- Your To-Do List ---")
    for i, task in enumerate(tasks, 1):
        print(f"  {i}. {task}")
    print(f"  Total: {len(tasks)} task(s)")


def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)
    print(f"  ✓ Added: '{task}'")


def remove_task(tasks, number):
    if 1 <= number <= len(tasks):
        removed = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f"  ✓ Removed: '{removed}'")
    else:
        print("  Invalid task number.")


# --- Demo run ---
tasks = load_tasks()

add_task(tasks, "Study Calculus Chapter 9")
add_task(tasks, "Practice Python loops")
add_task(tasks, "Review Linear Algebra notes")
add_task(tasks, "Pray Fajr and read Quran")

show_tasks(tasks)

print("\nRemoving task #2...")
remove_task(tasks, 2)

show_tasks(tasks)

print(f"\nTasks saved to '{FILENAME}'")
