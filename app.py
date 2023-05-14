from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks, enumerate=enumerate)


@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    tasks.append(task)
    return redirect('/')


@app.route('/delete', methods=['POST'])
def delete():
    task_index = int(request.form['task_index'])
    del tasks[task_index]
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
