from flask import Flask, render_template, request, redirect

app = Flask(__name__)

employees = []

@app.route('/')
def home():
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form['name']
    employees.append(name)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
