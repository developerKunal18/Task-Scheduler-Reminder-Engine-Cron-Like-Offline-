import time
import json
import os
from datetime import datetime, timedelta

DB_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DB_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks):
    name = input("Task name: ")
    seconds = int(input("Run after how many seconds?: "))
    repeat = input("Repeat? (y/n): ").lower() == "y"

    task = {
        "name": name,
        "run_at": (datetime.now() + timedelta(seconds=seconds)).isoformat(),
        "repeat": repeat,
        "interval": seconds if repeat else None
    }

    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task scheduled.\n")

def check_tasks(tasks):
    now = datetime.now()
    for task in tasks[:]:
        run_time = datetime.fromisoformat(task["run_at"])
        if now >= run_time:
            print(f"\n🔔 Reminder: {task['name']} ({now.strftime('%H:%M:%S')})")
            if task["repeat"]:
                task["run_at"] = (now + timedelta(seconds=task["interval"])).isoformat()
            else:
                tasks.remove(task)
            save_tasks(tasks)

def main():
    tasks = load_tasks()
    print("🕒 Task Scheduler \n")

    while True:
        print("1. Add task")
        print("2. Start scheduler")
        print("3. Exit")

        choice = input("\nChoose: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            print("\n⏳ Scheduler running... Press CTRL+C to stop.")
            try:
                while True:
                    check_tasks(tasks)
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\nScheduler stopped.\n")
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()
