from flask import Flask, render_template, url_for

app = Flask(__name__)

data = [
    {'id': 1, 'title': 'Artículo 1', 'content': 'Contenido del artículo 1'},
    {'id': 2, 'title': 'Artículo 2', 'content': 'Contenido del artículo 2'},
    {'id': 3, 'title': 'Artículo 3', 'content': 'Contenido del artículo 3'}
]

@app.route('/')
def home():
    return render_template('index.html', data=data)

@app.route('/view_data')
def view_data():
    return render_template('view_data.html', data=data)

@app.route('/detail/<int:item_id>')
def detail(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    return render_template('detail.html', item=item)

if __name__ == '__main__':
    app.run(debug=True)

