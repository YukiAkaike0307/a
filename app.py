from flask import Flask, render_template, request, jsonify


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

app.route('/jyunni', methods=['GET'])
def get_jyunni():
    jyunni_data = {
        'p_jyunni': '1位　オリックス・バファローズ 、2位　千葉ロッテマリーンズ、3位　福岡ソフトバンクホークス、4位　楽天ゴールデンイーグルス、5位　埼玉西武ライオンズ、6位　北海道日本ハムファイターズ',
        's_jyunni': '1位　阪神タイガース 、2位　広島東洋カープ、3位　横浜DeNAベイスターズ、4位　読売ジャイアンツ、5位　東京ヤクルトスワローズ、6位　中日ドラゴンズ',
    }
    return jsonify(jyunni_data), 200

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