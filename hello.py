from flask import Flask, render_template #追加
import pymysql

app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hoge"
    #return name
    db = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='flasktestdb',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
        )
    cur = db.cursor()
    sql = "select * from members"
    cur.execute(sql)
    members = cur.fetchall()

    cur.close()
    db.close()

    return render_template('hello.html', title='flask test', name=name) #変更

@app.route('/hello', methods=['POST']) #Methodを明示する必要あり
def hello():
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = "no name."
    return render_template('hello.html', title='flask test', name=name)
## おまじない
if __name__ == "__main__":
    app.run(debug=True)
