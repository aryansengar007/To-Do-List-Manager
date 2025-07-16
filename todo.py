import json
from utils import load_tasks, save_tasks

class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {"title": self.title, "completed": self.completed}

    @staticmethod
    def from_dict(data):
        return Task(data['title'], data['completed'])

class ToDoList:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        task_data = load_tasks(self.filename)
        return [Task.from_dict(t) for t in task_data]

    def save_tasks(self):
        save_tasks(self.filename, [t.to_dict() for t in self.tasks])

    def add_task(self, title):
        self.tasks.append(Task(title))
        self.save_tasks()
        print(f"✅ Task '{title}' added.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"🗑️ Task '{removed.title}' removed.")
        else:
            print("⚠️ Invalid task number.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()
            print(f"✅ Task '{self.tasks[index].title}' marked as completed.")
        else:
            print("⚠️ Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks to show.")
            return
        print("\n📋 Your Tasks:")
        for idx, task in enumerate(self.tasks, start=1):
            status = "✅" if task.completed else "⏳"
            print(f"{idx}. {task.title} [{status}]")
