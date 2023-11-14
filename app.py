from flask import Flask, render_template, request


app = Flask(__name__)
app = Flask(__name__, static_folder='./templates/images')
app = Flask(__name__, static_folder="templates", static_url_path='')

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html',  title="Form sample",  message="お名前は？")

@app.route('/', methods=['POST'])
def   form():
	field = request.form['field']
	return render_template('index.html', title="Form sample",  message="こんにちは、%s さん！" % field)

@app.route('/result', methods=['POST'])
def result_post():
	# POST送信の処理
	field1 = request.form['email']
	field2 = request.form['password']
	return render_template('result.html', message = "ログイン成功!")

@app.route('/akaunto', methods=['POST'])
def akaunto_post():
	# POST送信の処理
	field1 = request.form['name']
	field2 = request.form['text']
	field3 = request.form['email']
	field4 = request.form['password']
	return render_template('result_first.html', message = "会員登録完了!!")

if __name__ == '__main__':
	app.debug = True
	app.run(host='localhost') 