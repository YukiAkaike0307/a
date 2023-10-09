from flask import Flask, render_template, request

app = Flask(__name__)
app = Flask(__name__, static_folder='./templates/images')
app = Flask(__name__, static_folder="templates", static_url_path='')

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html',  title="Form sample",  message="お名前は？")

@app.route('/open_file')
def open_file():
    return render_template('main.html')

@app.route('/', methods=['POST'])
def   form():
	field = request.form['field']
	return render_template('index.html', title="Form sample",  message="こんにちは、%s さん！" % field)


if __name__ == '__main__':
	app.debug = True
	app.run(host='localhost') 