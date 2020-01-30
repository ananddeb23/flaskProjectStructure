from flask import jsonify, Blueprint, request
from pprint import pprint
import json
from app import db
from app.module_one.models import Todo

mod_one = Blueprint('module_1', __name__, url_prefix='/module-1')

@mod_one.route('/', methods=['POST', 'GET'])
def index():
  if request.method == 'POST':
    task_content = request.form['task']
    new_task = Todo(content=task_content)

    try:
      db.session.add(new_task)
      db.session.commit()
      return 'Success'
    except:
      return 'There was an issue adding your task'

  else:
    tasks = Todo.query.order_by(Todo.date_created).all()
    # print('TASKS', tasks)
    # pprint.pprint(tasks)
    # resp_body = {
    #   "tasks" : tasks
    # }
    # d = dict(tasks.tasks())
    # resp = jsonify(resp_body)
    return json.dumps(tasks)
    # return 'sd'

@mod_one.route('/delete/<int:id>')
def delete(id):
  task_to_delete = Todo.query.get_or_404(id)

  try:
    db.session.delete(task_to_delete)
    db.session.commit()
    return 'Success'
  except:
    return 'There was a problem deleting that task'

@mod_one.route('/update/<int:id>', methods=['PUT'])
def update(id):
  task = Todo.query.get_or_404(id)
  task.content = request.args.get('task')
  try:
    db.session.commit()
    return 'Success'
  except:
    return 'There was an issue updating the task'
