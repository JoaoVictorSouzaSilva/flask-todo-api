from flask import Flask, jsonify, request
import json

app = Flask(__name__)
DATA_FILE = 'tasks.json'

def load_tasks():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(load_tasks())

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "title": data.get('title', 'Sem título'),
        "done": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = request.json.get('done', task['done'])
            save_tasks(tasks)
            return jsonify(task)
    return jsonify({'error': 'Tarefa não encontrada'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    return jsonify({'message': 'Tarefa removida'}), 200

if __name__ == '__main__':
    app.run(debug=True)
