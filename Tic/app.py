import numpy as np
from flask import Flask,render_template,url_for,request


app=Flask(__name__)

game_board=np.array([['','',''],['','',''],['','','']])
print(game_board)
winner=0
k=0
count=0
msg=''
@app.route("/restart/", methods=['POST'])
def restart():
       game_board=np.array([['','',''],['','',''],['','','']])
       print(game_board)
       winner=0
       k=0
       count=0
       return render_template('index.html',game=game_board,player="X",msg=msg)


def set_board(player,row,col):
    if(game_board[row][col]==''):
        game_board[row][col]=player
    else:
        r,c=map(int,input("Try again").split())
        set_board(player,r,c)


def check_row_win():
    global winner
    if(game_board[0][0]==game_board[0][1]==game_board[0][2] and game_board[0][0]!=''):
        winner=game_board[0][0]
        print("1")
        return 1
    elif(game_board[1][0]==game_board[1][1]==game_board[1][2] and game_board[1][0]!=''):
        winner=game_board[1][0]
        print("2")
        return 1
    elif(game_board[2][0]==game_board[2][1]==game_board[2][2] and game_board[2][0]!=''):
        winner=game_board[2][0]
        print("3")
        return 1
    
def check_col_win():
    global winner
    if(game_board[0][0]==game_board[1][0]==game_board[2][0] and game_board[0][0]!=''):
        winner=game_board[0][0]
        print("4")
        return 1
    elif(game_board[0][1]==game_board[1][1]==game_board[2][1] and game_board[0][1]!=''):
        winner=game_board[0][1]
        print("5")
        return 1
    elif(game_board[0][2]==game_board[1][2]==game_board[2][2] and game_board[0][2]!=''):
        winner=game_board[0][2]
        print("6")
        return 1
    
def check_diag_win():
    global winner
    if(game_board[0][0]==game_board[1][1]==game_board[2][2] and game_board[0][0]!=''):
        winner=game_board[0][0]
        print("7")
        return 1
    elif(game_board[0][2]==game_board[1][1]==game_board[2][0] and game_board[0][2]!=''):
        winner=game_board[0][2]
        print("8")
        return 1

def check():
    if(check_row_win()==1 or check_col_win()==1 or check_diag_win()==1):
        print("Winner is",winner)
        return 1

@app.route('/',methods=['POST','GET'])
def index():
    players=['X','O']
    global k
    global count
    msg=""
    if request.method=="POST":
       r,c=map(int,request.form['1'].split(','))
       print(r,c)
       count=count+1
       player=players[k]
       set_board(player,r,c)
       if(k==0):
          k=1
       else:
          k=0
       if(check()==1):
          msg="Win"
       if(count==9 and msg==''):
          msg="Draw"
       return render_template('index.html',game=game_board,player=player,win=winner,msg=msg)
    
    else:
        return render_template('index.html',game=game_board,player="X",msg=msg)
    
    

if __name__== "__main__":
    app.run(debug=True)