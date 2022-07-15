# // micro web framework of python : flask
from distutils.debug import DEBUG
from flask import Flask, render_template, request
from sudokuSolver import main


app = Flask(__name__)
app.config['DEBUG'] = True

grid = [['']*9]*9

@app.route('/')
def index():
  return render_template('index.html', board=grid)

@app.route('/solve', methods=['GET','POST'])
def solver():
  board = []
  if request.method == "POST": 
    for i in range(0,9,1):
      temp = []
      for j in range(0,9,1):
        path = 'g'+ str(i)+str(j)
        if request.form[path]:
          val = request.form[path]
          temp.append(int(val))
        else:
          temp.append(0)
      board.append(temp)

  board=main(board)   

  return render_template('index.html', board= board)
if __name__ == '__main__':
  app.run()