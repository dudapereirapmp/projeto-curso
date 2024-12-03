from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)
TASKS_FILE = "tasks.json"

# Carregar tarefas
def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Salvar tarefas
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET', 'POST'])
def manage_tasks():
    if request.method == 'GET':
        return jsonify(load_tasks())
    elif request.method == 'POST':
        tasks = load_tasks()
        new_task = request.json
        tasks.append(new_task)
        save_tasks(tasks)
        return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
