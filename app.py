# // micro web framework of python : flask
from distutils.debug import DEBUG
from flask import Flask, render_template, request


n=9

def check(grid, row, col, num):
    for x in range(9):
        if grid[row][x]==num:
            return False
    for x in range(9):
        if grid[x][col]==num:
            return False
    str=row - row % 3
    stc=col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[str+i][stc+j]==num:
                return False
    return True

def solve(grid, row, col):
    if( row == n-1 and col== n):
        return True
    if col==n:
        row+=1
        col=0
    if grid[row][col]>0:
        return solve(grid, row, col+1)
    for num in range(1, n+1, 1):
        if check(grid, row, col, num):
            grid[row][col]=num
            if solve(grid, row, col+1):
                return True
        grid[row][col]=0
    return False    

def main(grid):
    solve(grid,0,0)
    return grid  



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