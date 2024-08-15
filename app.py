from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for to-do items
todos = []

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html', todos=todos)

# Route to add a new to-do item
@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        todos.append(todo)
    return redirect(url_for('index'))

# Route to delete a to-do item
@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    if 0 <= todo_id < len(todos):
        del todos[todo_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
