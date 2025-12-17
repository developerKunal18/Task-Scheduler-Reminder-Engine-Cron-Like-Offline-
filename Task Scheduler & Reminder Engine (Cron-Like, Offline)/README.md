# 🕒 Task Scheduler & Reminder Engine 

## 💡 Overview
The **Task Scheduler & Reminder Engine** is a Python-based offline scheduler that allows you to create time-based reminders and recurring tasks without relying on OS-level cron jobs or external services.

It functions as a **mini cron system**, storing tasks locally and triggering reminders directly in the terminal.

---

## 🚀 Features

### ✔ One-Time & Recurring Tasks
- Schedule a task to run once  
- Repeat tasks at fixed intervals  

### ✔ Terminal Notifications
Receive reminders directly in the terminal when a task triggers.

### ✔ Local Persistence
Tasks are saved in a JSON file so they persist between runs.

### ✔ Offline & Cross-Platform
Works on any system with Python — no internet required.

### ✔ Simple CLI Interface
Menu-driven interface for easy task management.

---

## 🧠 Concepts & Technologies Used
- Python
- Date & time handling (`datetime`)
- Persistent storage (JSON)
- Scheduling loops
- ISO timestamp management
- CLI application design

---

## 📦 Installation

No external libraries required.

### Run the program:
```bash
python task_scheduler.py
