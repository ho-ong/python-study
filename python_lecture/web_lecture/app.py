# app.py (Backend)
from flask import Flask, render_template
from flask import request

import pymysql

# DB 연동
db_conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '1234',
    db = 'test',
    charset = 'utf8'
)

print(db_conn)

# Flask 객체 인스턴스 생성
app = Flask(__name__)

# @ : decoration
# GET
@app.route('/') # 접속하는 url
def index():
    temp = request.args.get('uid')
    temp1 = request.args.get('cid')
    print(temp, temp1)
    return render_template('index.html')

# GET
@app.route('/test')
def testget():
    return render_template('posttest.html')

# POST
@app.route('/test', methods=['POST'])
def testpost():
    value = request.form['input']
    print(value)
    return render_template('posttest.html')

# MySQL
# GET
@app.route('/sqltest')
def sqltest():
    # 커서 객체 생성
    cursor = db_conn.cursor()
    query = "select * from player"
    cursor.execute(query)
    result = []

    for i in cursor:
        temp = {'player_id':i[0], 'player_name':i[1]}
        result.append(temp)

    return render_template('sqltest.html', result_table = result)

# GET
@app.route('/detail')
def detailtest():
    temp = request.args.get('id')
    temp1 = request.args.get('name')
    cursor = db_conn.cursor()

    # sql 쿼리에서 작은따옴표 쿼리문에 넣으니까 넣어줘야 한다.
    query = "select * from player where player_id = {} and player_name like '{}'".format(temp, temp1)
    cursor.execute(query)
    result = []

    for i in cursor:
        temp = {'player_id':i[0], 'player_name':i[1], 'team_name':i[2], 'height':i[-2], 'weight':i[-1]}
        result.append(temp)

    return render_template('detail.html', result_table = result)

if __name__=="__main__":
    app.run(debug=True)
    # host 등을 직접 지정하고 싶다면
    # app.run(host="127.0.0.1", port="5000", debug="True")
