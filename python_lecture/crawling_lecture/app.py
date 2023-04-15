from flask import Flask, render_template
from flask import request

app = Flask(__name__)

# index
@app.route('/1')
def index1():
  return render_template('index1.html')

# index2
@app.route('/2')
def index2():
  return render_template('index2.html')

# index3
@app.route('/3')
def index3():
  return render_template('index3.html')

# index4
@app.route('/4')
def index4():
  return render_template('index4.html')

# index5
@app.route('/5')
def index5():
  return render_template('index5.html')

# index6
@app.route('/6')
def index6():
  return render_template('index6.html')

if __name__=="__main__":
  app.run(debug=True)
