import csv
from datetime import datetime
import os

class CollegeToDoList:
    def __init__(self):
        self.tasks = []
        self.predefined_tasks = {'Book Reading': False, 'Workout': False}
        self.daily_skills = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task):
        if task in self.predefined_tasks:
            self.predefined_tasks[task] = True

    def add_daily_skill(self, skill):
        self.daily_skills.append(skill)

    def export_to_csv(self):
        downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
        filename = os.path.join(downloads_folder, 'todo_list.csv')
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Task', 'Completed'])
            for task in self.tasks:
                writer.writerow([datetime.now().strftime('%Y-%m-%d'), task, 'Yes'])
            for task, completed in self.predefined_tasks.items():
                writer.writerow([datetime.now().strftime('%Y-%m-%d'), task, 'Yes' if completed else 'No'])
            if self.daily_skills:
                writer.writerow([])
                writer.writerow(['Skills Learned'])
                for skill in self.daily_skills:
                    writer.writerow([skill])
        print(f"Your to-do list has been saved to {filename}")

if __name__ == "__main__":
    todo_list = CollegeToDoList()

    while True:
        task = input("Enter a task you completed today (or type 'done' to finish): ")
        if task.lower() == 'done':
            break
        todo_list.add_task(task)

    for task in todo_list.predefined_tasks.keys():
        complete = input(f"Did you complete {task}? (yes/no): ").lower()
        if complete == 'yes':
            todo_list.complete_task(task)

    while True:
        skill = input("Did you learn any new skills today? (or type 'done' to finish): ")
        if skill.lower() == 'done':
            break
        todo_list.add_daily_skill(skill)

    todo_list.export_to_csv()
