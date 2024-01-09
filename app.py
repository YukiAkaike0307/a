from flask import Flask, render_template, request, redirect, url_for, session
import MySQLdb
import secrets

app = Flask(__name__, static_folder="templates", static_url_path='')
app.secret_key = secrets.token_hex(24)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title="Form sample", message="お名前は？")

# ログイン画面
@app.route('/rogin', methods=['GET', 'POST'])
def rogin():
    db = MySQLdb.connect(host="localhost", user="root", password="Yuki0307", db="account")
    cursor = db.cursor()
    error_message = None

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # プレースホルダーを使用してSQLインジェクション対策
        cursor.execute("SELECT * FROM account_list WHERE email=%s AND password=%s", (email, password))
        user = cursor.fetchone()

        if user:
            # ユーザーが存在すればセッションにユーザーIDを保存
            session['user_id'] = user[0]
            return redirect(url_for('home'))
        else:
            error_message = 'メールアドレスかパスワードが間違っています'

    return render_template('rogin.html', error_message=error_message)

@app.route('/akaunto', methods=['POST', 'GET'])
def result():
    db = MySQLdb.connect(host="localhost", user="root", password="Yuki0307", db="account")
    cursor = db.cursor()
    if request.method == 'POST':
        name = request.form['name']
        text = request.form['text']
        email = request.form['email']
        password = request.form['password']

        # プレースホルダーを使用してSQLインジェクション対策
        cursor.execute("INSERT INTO account_list (name, text, email, password) VALUES (%s, %s, %s, %s)", (name, text, email, password))
        db.commit()

        # アカウント作成後にログイン画面にリダイレクト
        return redirect(url_for('rogin'))

    return render_template('akaunto.html')

# ホーム画面
@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('index.html')  # ログインしていればホーム画面を表示
    else:
        return redirect(url_for('rogin'))  # ログインしていなければログイン画面にリダイレクト
    
@app.route('/tokusetu')
def tokusetu():
    db = MySQLdb.connect(host="localhost", user="root", password="Yuki0307", db="japan_series")
    cursor = db.cursor()
    # データベースからデータを取得
    cursor.execute("SELECT * FROM japan_series_list")
    results = cursor.fetchall()
    # HTMLテンプレートにデータを渡して表示
    return render_template('tokusetu.html', results=results)

@app.route('/openapi', methods=['GET'])
def openapi():
    return render_template('openapi.html')

if __name__ == '__main__':
    app.debug = True
    app.run(port='5000')
