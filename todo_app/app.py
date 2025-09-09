from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# In-memory task storage
tasks = []

# Home - list tasks
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Add task
@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

# Edit task
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    if request.method == 'POST':
        tasks[task_id] = request.form.get('task')
        return redirect(url_for('index'))
    return render_template('edit.html', task=tasks[task_id], task_id=task_id)

# Delete task
@app.route('/delete/<int:task_id>')
def delete(task_id):
    tasks.pop(task_id)
    return redirect(url_for('index'))

# AI-powered task generator (mock version here)
@app.route('/generate')
def generate():
    ai_tasks = [
        "Read one chapter of a book",
        "Do a 10-minute workout",
        "Write a gratitude journal entry",
        "Organize study notes",
        "Learn a new programming concept"
    ]
    tasks.append(random.choice(ai_tasks))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
