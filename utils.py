import os
import json

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_divider():
    print("-" * 40)

def load_tasks(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
