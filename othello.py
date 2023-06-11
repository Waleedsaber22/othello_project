from tkinter import *
from tkinter import ttk
import time
import pygame
import copy
from threading import Timer
from datetime import datetime
import os
pygame.mixer.init()
root = Tk()
root.configure()
root.title("Othello")
game_type=""
active_black=1
board_size=8
minimax_depth=4
restart=0
directions = [(1,1),(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]
min_eval_coins = float("-inf")
max_eval_coins = float("inf")
waiting=False
dir_path = os.path.dirname(os.path.realpath(__file__))
regions=[[80,1,10,10,10,10,1,80],
             [1,2,4,4,4,4,2,1],
             [10,4,7,6,6,7,4,10],
             [10,4,6,7,7,6,4,10],
             [10,4,6,7,7,6,4,10],
             [10,4,7,6,6,7,4,10],
             [1,2,4,4,4,4,2,1],
             [80,1,10,10,10,10,1,80]]

######################################################### game design ############################################################

#+++++++++++++++++++++++++ create pages container ++++++++++++++++
container_fr = Frame(root)
start_fr_cont = Frame(container_fr)
menu_fr_cont = Frame(container_fr)
gameover_fr_cont = Frame(container_fr)
play_fr_cont = Frame(container_fr,padx=10,pady=10,bg="green")
start_fr = Frame(start_fr_cont)
menu_fr = Frame(menu_fr_cont)
play_fr = Frame(play_fr_cont)
gameover_fr = Frame(gameover_fr_cont,bg="blue")
container_fr.pack(expand=True)
start_fr_cont.grid(row = 0, column = 0, sticky ="nsew")
menu_fr_cont.grid(row = 0, column = 0, sticky ="nsew")
play_fr_cont.grid(row = 0, column = 0, sticky ="nsew")
gameover_fr_cont.grid(row = 0, column = 0, sticky ="nsew")
frames={"start":start_fr_cont,"menu":menu_fr_cont,"play":play_fr_cont}
frames["start"].tkraise()
start_fr.pack(expand=True)
menu_fr.pack(expand=True)
gameover_fr.pack(expand=True,padx=20,pady=20)
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

#++++++++++++++++++++++++++ create start page ++++++++++++++++++++
start_lb=Label(start_fr,text="Play Othello Now",foreground="blue",font=("Verdana", 35,"bold"),pady=30)
start_lb.pack()
start_bt = Button(start_fr,text="START")
start_bt.pack()
def handle_start() :
    frames["menu"].tkraise()
start_bt.config(command=handle_start)
start_bt.configure(font=("Arial",30,"bold"),padx=80,pady=10,bg="blue",foreground="white")

#++++++++++++++++++++++++++ create menu page ++++++++++++++++++++++
menu_mode_fr=Frame(menu_fr)
menu_mode_fr.pack(side="left")
menu_level_fr=Frame(menu_fr,bg="orange")
menu_level_fr.pack_forget()
menu2_level_cont=Frame(menu_fr,bg="orange")
menu2_level_fr=Frame(menu2_level_cont,bg="orange")
home_bt = Button(menu_mode_fr,text="HOME")
p_bt = Button(menu_mode_fr,text="Player VS Player")
pc_bt = Button(menu_mode_fr,text="Player VS Computer")
c_bt = Button(menu_mode_fr,text="Computer VS Computer")
cp_bt = Button(menu_mode_fr,text="Computer VS Player")
# player_name1=Entry(menu_level_fr)
# player_name2=Entry(menu_level_fr)
black_level=StringVar(value="easy")
white_level=StringVar(value="easy")
Label(menu_level_fr,text="Computer Levels",padx=10,pady=10,bg="orange",font=("Arial",25,"bold")).pack()
Label(menu_level_fr,text="Computer 1",padx=10,pady=10,bg="orange",font=("Arial",25,"bold")).pack()
b_veasy=Radiobutton(menu_level_fr,text="Beginner",variable=black_level,value="veasy")
b_easy=Radiobutton(menu_level_fr,text="Amateur",variable=black_level,value="easy")
b_med=Radiobutton(menu_level_fr,text="Intermediate",variable=black_level,value="med")
b_hard=Radiobutton(menu_level_fr,text="Professional",variable=black_level,value="hard")
b_vhard=Radiobutton(menu_level_fr,text="Master",variable=black_level,value="vhard")
Label(menu2_level_fr,text="Computer 2",padx=10,pady=10,bg="orange",font=("Arial",25,"bold")).pack()
b2_veasy=Radiobutton(menu2_level_fr,text="Beginner",variable=white_level,value="veasy")
b2_easy=Radiobutton(menu2_level_fr,text="Amateur",variable=white_level,value="easy")
b2_med=Radiobutton(menu2_level_fr,text="Intermediate",variable=white_level,value="med")
b2_hard=Radiobutton(menu2_level_fr,text="Professional",variable=white_level,value="hard")
b2_vhard=Radiobutton(menu2_level_fr,text="Master",variable=white_level,value="vhard")
st_level_bt = Button(menu_level_fr,text="Start")
home_bt.pack(pady=10)
p_bt.pack(pady=10)
pc_bt.pack(pady=10)
cp_bt.pack(pady=10)
c_bt.pack(pady=10)
b_veasy.pack(pady=10)
b_easy.pack(pady=10)
b_med.pack(pady=10)
b_hard.pack(pady=10)
b_vhard.pack(pady=10)
menu2_level_cont.pack_forget()
menu2_level_fr.pack()
b2_veasy.pack(pady=10)
b2_easy.pack(pady=10)
b2_med.pack(pady=10)
b2_hard.pack(pady=10)
b2_vhard.pack(pady=10)
st_level_bt.pack(pady=10)
def go_start() :
    frames["start"].tkraise()
home_bt.config(command=go_start)
p_bt.config(command=lambda: go_play("p"))
pc_bt.config(command=lambda: go_play("pc"))
cp_bt.config(command=lambda: go_play("cp"))
c_bt.config(command=lambda: go_play("c"))
home_bt.configure(font=("Arial",30,"bold"),padx=80,pady=10,bg="orange",foreground="white")
p_bt.configure(font=("Arial",25,"bold"),padx=50,pady=10,bg="blue",foreground="white")
pc_bt.configure(font=("Arial",25,"bold"),padx=50,pady=10,bg="indigo",foreground="white")
cp_bt.configure(font=("Arial",25,"bold"),padx=50,pady=10,bg="slateblue",foreground="white")
def go_play_level():
    if game_type != "pc":
        st_ai_bt.pack(side="left",anchor="w")
    else:
        st_ai_bt.pack_forget()
    player_lb.configure(text= f"{player_name(active_black,game_type)} playing now ...",foreground="black" if active_black  else "white" )
    frames["play"].tkraise()
st_level_bt.configure(font=("Arial",25,"bold"),padx=50,pady=10,bg="blue",foreground="white",command=go_play_level)
c_bt.configure(font=("Arial",25,"bold"),padx=50,pady=10,bg="purple",foreground="white")
b_easy.configure(font=("Arial",25,"bold"),padx=50,pady=10)
b_hard.configure(font=("Arial",25,"bold"),padx=50,pady=10)
b_med.configure(font=("Arial",25,"bold"),padx=50,pady=10)
b_veasy.configure(font=("Arial",25,"bold"),padx=50,pady=10)
b_vhard.configure(font=("Arial",25,"bold"),padx=50,pady=10)
b2_easy.configure(font=("Arial",25,"bold"),padx=50,pady=10)
b2_hard.configure(font=("Arial",25,"bold"),padx=50,pady=10)
b2_med.configure(font=("Arial",25,"bold"),padx=50,pady=10)
b2_veasy.configure(font=("Arial",25,"bold"),padx=50,pady=10)
b2_vhard.configure(font=("Arial",25,"bold"),padx=50,pady=10)

#+++++++++++++++++++++ create gameover page ++++++++++++++++++
def close_page() :
    gameover_fr_cont.grid(sticky="nsew")
    play_fr_cont.grid(sticky="nsew")
    play_fr_cont.tkraise()
cls_bt = Button(gameover_fr,text="X",font=("Arial",20,"bold"),pady=15,padx=15,command=close_page,bg="blue")
cls_bt.pack(anchor="e")
gameover_lbl = Label(gameover_fr,text="Game over",font=("Arial",30,"bold"),pady=30,padx=30,foreground="black",bg="blue")
gameover_lbl.pack()
winner_lbl = Label(gameover_fr,font=("Arial",30,"bold"),pady=30,padx=30,foreground="black",bg="blue")
winner_lbl.pack()
#++++++++++++++++++++ create play page +++++++++++++++++++

        #1 +++++ create action container
action_cont = Frame(play_fr_cont,bg="green")
action_cont.pack(expand=True)
score_cont = Frame(action_cont)
score_cont.pack(side="right",ipadx=20,padx=20,pady=10)
rst_bt=Button(action_cont,text="Restart")
st_bt=Button(action_cont,text="Start New Game")
rst_bt.configure(font=("Arial",20,"bold"),padx=30,pady=10,bg="blue",foreground="white")
st_bt.configure(font=("Arial",20,"bold"),padx=30,pady=10,bg="orange",foreground="white")
rst_bt.pack(side="left",anchor="w")
st_bt.pack(side="left",anchor="w")
st_ai_bt=Button(action_cont,text="Start AI",)
def start_ai():
    st_ai_bt.configure(state=["disabled"],bg="white")
    ai=Timer(0,AI_move)
    ai.start()
st_ai_bt.configure(font=("Arial",20,"bold"),padx=30,pady=10,bg="brown",foreground="white",command=start_ai)
st_ai_bt.pack(side="left",anchor="w")
        #2 +++++ create score banner
scoretitle_lb=Label(score_cont,text="⚫ Player Vs ⚪ Player",pady=10,font=("Arial",20,"bold"))
score_lb=Label(score_cont,text="⚫ 2  ⚪ 2",font=("Arial",20,"bold"))
scoretitle_lb.pack()
score_lb.pack()
player_lb=Label(play_fr_cont,text="⚫ Player A playing now ....",font=("Arial",20,"bold"),foreground="black",bg="green")
player_lb.pack()
def go_play(type) :
    global game_type
    global waiting
    game_type=type
    init_board()
    if game_type == "p" or game_type == "pc":
        waiting=False
    else: waiting=True
    if game_type != "p":
        menu_level_fr.pack(side="left",ipadx=20,padx=20)
        if game_type=="c":menu2_level_cont.pack(side="right")
        else:menu2_level_cont.pack_forget()
    else:
        st_ai_bt.place(x=-6000)
        player_lb.configure(text= f"{player_name(active_black,game_type)} playing now ...",foreground="black" if active_black  else "white" )
        frames["play"].tkraise()
    scoretitle_lb.configure(text= (
            "⚫ Player A Vs ⚪ Player B") if type == "p" else "⚫ Computer A Vs ⚪ Player A" if type == "cp"
            else "⚫ Player A Vs ⚪ Computer A" if type == "pc" else "⚫ Computer A Vs ⚪ Computer B" if type=="c" else "")
play_fr.pack(expand=True,pady=10)

        #3 +++++ create board
board = [[Button(play_fr,bg="gray",padx=20,pady=20) for col in range(board_size)] for row in range(board_size)]
coins = [["gray" for col in range(board_size)] for row in range(board_size)]
player_name=lambda active_black,game_type:  ("⚫ Computer A" if active_black
        else "⚪ Computer B") if game_type=="c" else ("⚫ Player A" if active_black
        else "⚪ Player B") if game_type=="p" else ("⚫ Player A" if active_black
        else "⚪ Computer A") if game_type[0]=="p" else ("⚫ Computer A" if active_black
        else "⚪ Player A")


## handling reset and init part
def init_board():
    for row in range(board_size):
        for col in range(board_size):
            board[row][col].grid(row=row,column=col,padx=5,pady=5)
            if (row == 3 and (col==3 or col==4))  or (row==4 and (col==3 or col==4)):
                board[row][col].configure(state=["disabled"],bg="black" if row !=col else "white" )
                board[row][col].configure(state=["disabled"],bg="black" if row !=col else "white" )
                coins[row][col]="black" if row !=col else "white"
            else:
                coins[row][col]="gray"
                board[row][col].config(state=["normal"],command=lambda row=row,col=col: handle_move(row,col),bg="gray")
    if game_type =="p" or game_type =="pc":
        for (row,col) in possible_moves(coins,active_black):
            board[row][col].configure(bg="blue")
def restart_ai():
    global restart
    restart=0
    st_ai_bt.configure(state=["normal"],bg="brown")
def reset_game():
    global active_black
    global waiting
    global restart
    active_black=1
    init_board()
    if game_type == "c" or game_type == "cp":
        restart=1
        waiting=True
        time.sleep(2.5)
        restart_ai()
    else: waiting=False
    score_lb.configure(text=f"⚫ 2  ⚪ 2")
    player_lb.configure(text= f"{player_name(active_black,game_type)} playing now ...",foreground="black" if active_black else "white")
    init_board()

def new_game():
    reset_game()
    menu_level_fr.place_forget()
    menu2_level_cont.place_forget()
    frames["menu"].tkraise()

rst_bt.configure(command=reset_game)
st_bt.configure(command=new_game)


############################################## game algorithms ###################################################
#+++++++ check if there's captured coins for specific move at any direction
def check_captured(coins,r,c,iy,ix,is_black,is_move,index):
    my_color = "black" if is_black else "white"
    target_color = "black" if not is_black else "white"
    change_coins=[]
    y=r
    x=c
    while True:
        if y < 0 or y > board_size -1 or x < 0 or x > board_size - 1: return []
        x=x+ix
        y=y+iy
        if y < 0 or y > board_size -1 or x < 0 or x > board_size - 1: return []
        coin = coins[y][x]
        if  coin == target_color :
          change_coins.append((y,x) if is_move or index else coin)
        else : break
    if coins[y][x] != my_color : return []
    return change_coins

#+++++++ check if it's valid move only if there's captured coins
def valid_moves(coins,r,c,is_black,is_move=False,index=False):
    all_captures=[]
    if not(coins[r][c]=="black" or coins[r][c]=="white"):
        for iy,ix in directions:
            all_captures= all_captures + check_captured(coins,r,c,iy,ix,is_black,is_move,index)
    if is_move:
        coins[r][c]="black" if is_black else "white"
        for row,col in all_captures:
             coins[row][col]="black" if is_black else "white"
    return coins if is_move else all_captures
  
#+++++++ get all possible move for a game state 
def possible_moves(coins,is_black,order_value=False):
    all_moves=[]
    count=0
    for row in range(board_size):
        for col in range(board_size):
            if(valid_moves(coins,row,col,is_black)):
                if order_value:
                    score=0
                    if count < 3:
                        new_coins = valid_moves(copy.deepcopy(coins),row,col,is_black,True)
                        score=eval_func(new_coins,is_black)
                    all_moves.append(((row,col),score))
                else:
                    all_moves.append((row,col))
                count = count + 1
    if order_value:
        all_moves=sorted(all_moves, key = lambda ele: ele[1], reverse = (order_value == "desc"))
        all_moves=[ele[0] for ele in all_moves]
    return all_moves


#++++++++++++++++++ calculate evaluation function based on all heurstics mentioned
def eval_func(coins,is_black):
    my_color = "black" if is_black else "white"
    target_color = "black" if not is_black else "white"
    ##################### using heurstics ##################

    #+++++++++++ mobility heurstic (potential mobility)
    pv1=potential_moves(coins,is_black)
    pv2=potential_moves(coins,not is_black)
    my_moves=len(pv1)
    your_moves=len(pv2)
    cost=0

    #++++++++++++ static cost matrix taking into consideration high corner value
    #++++++++++++and changing the cells adjacent to the same color corner accordingly
    static_cost=[
        [80,1,10,10,10,10,1,80],
        [1,2,4,4,4,4,2,1],
        [10,4,7,6,6,7,4,10],
        [10,4,6,7,7,6,4,10],
        [10,4,6,7,7,6,4,10],
        [10,4,7,6,6,7,4,10],
        [1,2,4,4,4,4,2,1],
        [80,1,10,10,10,10,1,80]
        ]
    for row in range(board_size):
        for col in range(board_size):
            actual_color=coins[row][col]
            if  actual_color == my_color or actual_color == target_color:
                if regions[row][col]==80 and actual_color == my_color:
                    r = 1 if (row==0) else row-1
                    c = 1 if (col==0) else col-1
                    if coins[r][col]==my_color:
                        static_cost[r][col]=80
                    if coins[row][c]==my_color:
                        static_cost[row][c]=80
                cost= cost +  (static_cost[row][col] if actual_color == my_color else -static_cost[row][col])
    cost=cost+((my_moves-your_moves)/ (my_moves+your_moves if (my_moves+your_moves) else 1))*abs(cost)*0.5
    return cost

#++++++++ count coins for two players for a game state
def count_coins(coins):
    black_coins=0
    white_coins=0
    for row in range(board_size):
        for col in range(board_size):
            if coins[row][col]=="black":black_coins=black_coins+1
            if coins[row][col]=="white":white_coins=white_coins+1
    return (black_coins,white_coins)

#+++++++++++ check if it's last move (leaf node)
def end_move(coins, is_black):
    for row in range(board_size):
        for col in range(board_size):
            if valid_moves(coins, row, col, is_black):
                return False
    return True

#################### heuristics and evaulation function part ###############

#++++++++++++++++ mobility heuristic using potential moves (for efficient computation)
def potential_moves(coins,is_black):
    all_moves=[]
    target_color = "white" if is_black else "black"
    for row in range(board_size):
        for col in range(board_size):
            if(coins[row][col]==target_color):
                    for (r,c) in directions:
                        r1=row+r
                        c1=col+c
                        r2=row-r
                        c2=col-c
                        if(r1 >= 0 and r1 < board_size and c1  > 0 and c1 < board_size
                           and r2 >= 0 and r2 < board_size and c2  > 0 and c2 < board_size):
                            if coins[r1][c1]=="gray" and coins[r2][c2]!="gray":
                                all_moves.append((r1,c1))
    return list(set(all_moves))
#+++++++++++++++++++++ minimax algoritm

def min_max(coins, is_black, depth, maximizer,player=False):

    if depth == 0 or end_move(coins,is_black) or restart:

        return eval_func(coins, player)

    pv = possible_moves(coins,is_black)

    best_score = min_eval_coins if maximizer else max_eval_coins

    for (row,col) in pv:

            new_coins = valid_moves(copy.deepcopy(coins), row ,col, is_black,True)

            score = min_max(new_coins,not is_black, depth - 1, not maximizer,player)

            best_score =  max(best_score, score) if maximizer else min(best_score, score)

    if not pv: return min_max(new_coins,not is_black, depth - 1, not maximizer,player)

    return best_score

#++++++++++++++++++++++ minimax algoritm with alpha_beta pruning
def alpha_beta(coins, is_black, depth, maximizer,alpha,beta,player=False,id_alg=0,now=0):
    # handle iterative deepening time violate
    if id_alg:
        if (datetime.timestamp(datetime.now())-now) > 5:
            return None
    if depth == 0 or end_move(coins, is_black) or restart:
        return eval_func(coins, player)
    pv = possible_moves(coins,is_black)
    best_score = min_eval_coins if maximizer else max_eval_coins
    for (row,col) in pv:
        if valid_moves(coins, row, col, is_black):
            new_coins = valid_moves(copy.deepcopy(coins), row, col, is_black,True)
            score = alpha_beta(new_coins,not is_black, depth - 1,not maximizer, alpha, beta, player,id_alg,now)
            if score is not None:
                best_score = max(score,best_score) if maximizer else min(score,best_score)
                if maximizer :alpha = max(alpha, best_score)
                else: beta = min(beta, best_score)
                # pruning (cut-off)
                if alpha >= beta:
                    break
            else: return None
    if not pv:
        if score is not None:
            return alpha_beta(new_coins,not is_black, depth - 1,not maximizer, alpha, beta, player,id_alg,now)
        else: return None
    return best_score

#++++++++++++++++++++++ apply all possible moves for a game state in ai algorithm then get scores
def best_move(alg=0,depth=4):
    max_score = min_eval_coins
    new_col = -1; new_row = -1
    idepth=1
    now=datetime.timestamp(datetime.now())
    for row,col in possible_moves(coins,active_black):
            if valid_moves(coins, row, col, active_black) and not restart:
                new_coins = valid_moves(copy.deepcopy(coins), row, col, active_black,True)
                score=0
                if alg==0:
                    #minimax algorithm
                    score = min_max(new_coins,not active_black, depth, False,active_black)
                elif alg==1:
                    #minimax algorithm with alpha_beta pruning
                    score = alpha_beta(new_coins,not active_black, depth, False,min_eval_coins,max_eval_coins,active_black)
                elif alg==2:
                    #iterative deepning minimax algorithm with alpha_beta pruning
                    while idepth <= depth and ((datetime.timestamp(datetime.now())-now) <= 5):
                        val=alpha_beta(new_coins,not active_black,idepth, False,min_eval_coins,max_eval_coins,active_black,True,now)
                        idepth = idepth + 1
                        if val is not None:
                            score=val
                if score > max_score:
                    max_score = score
                    new_col = col; new_row = row
    return (new_row, new_col)
  
############## apply actual move in board from any player
#++++++++++ AI player make move
def AI_move():
    global waiting
    waiting=True
    level=(black_level.get() if active_black else white_level.get()) if game_type=="c" else black_level.get()
    # estimate of best move
    (row,col)=best_move(0 if level == "easy" or level == "veasy" else 2 if level=="med" else 1,0 if level=="veasy" else 1  if level == "easy" 
                        else 3 if level=="med" else 4 if level=="hard" else 5)
    waiting=False
    apply_move(row,col)
    return
#++++++++++ player make move
def apply_move(row,col,cpass=False):
    global active_black
    global waiting
    if not waiting and not restart:
        my_color="black" if active_black else "white"
        trans_coins = valid_moves(coins,row,col,active_black,False,True)
        if (trans_coins or cpass):
            if row != -1:
                waiting=True
                
                pygame.mixer.music.load(os.path.join(dir_path,"accept.mp3"))
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    for i in [0,1,0,1]:
                        if not restart:
                            board[row][col].configure(bg= "blue" if i else "orange")
                            time.sleep(0.2)
                        else: return
                coins[row][col]=my_color
                board[row][col].configure(state=["disabled"],bg=my_color,activebackground="gray")
                target_color="black" if not active_black else "white"
                for (row,col) in trans_coins:
                    if coins[row][col]==target_color:
                        board[row][col].configure(state=["disabled"],bg=my_color)
                        coins[row][col] = my_color
                for row in range(8):
                    for col in range(8):
                        if board[row][col]["bg"]=="blue":
                            board[row][col].configure(bg="gray")

                active_black=not active_black
                if game_type =="p" or (game_type =="pc" and active_black) or (game_type =="cp" and not active_black):
                    for (row,col) in possible_moves(coins,active_black):
                        board[row][col].configure(bg="blue")
        # +++++++++++++++++++++++++++++++ players turns +++++++++++++++++++++++
                player_lb.configure(text= f"{player_name(active_black,game_type)} playing now ...",foreground="black" if active_black  else "white")
                (black_count,white_count)=count_coins(coins)
        # +++++++++++++++++++++++++++++++ players scores  +++++++++++++++++++++
                score_lb.configure(text=f"⚫ {black_count}  ⚪ {white_count}")
                waiting=False
                if (not active_black and game_type == "pc") or (active_black and game_type=="cp") or game_type == "c":
                    AI_move()
                    return

        elif row!=-1:
            pygame.mixer.music.load(os.path.join(dir_path,"reject.wav"))
            pygame.mixer.music.play()
            board[row][col].configure(activebackground="red")
        black_moves = possible_moves(coins,True)
        white_moves = possible_moves(coins,False)
        # +++++++++++++++++++++++++++++++  game over  +++++++++++++++++++++
        if not black_moves and not white_moves:
            (b,w)=count_coins(coins)
            lb="Draw between Players" if b==w else f"{player_name(b>w,game_type)} Winner"
            winner_lbl.configure(text=f"{lb}",foreground="black" if b>w  else "white")
            gameover_fr_cont.grid(sticky="")
            gameover_fr_cont.tkraise()
            player_lb.configure(text= f"All players play their moves")
            active_black=1
        # +++++++++++++++++++++++++++++++  skip black turn  +++++++++++++++++++++
        elif active_black and not black_moves:
            active_black=not active_black
            player_lb.configure(text= f"{player_name(active_black,game_type)} playing now ...",foreground="black" if active_black  else "white")
            if game_type=="c" or game_type=="pc":
                AI_move()
            else:
                for row in range(8):
                    for col in range(8):
                        if board[row][col]["bg"]=="blue":
                            board[row][col].configure(bg="gray")
                if game_type =="p" or (game_type =="pc" and active_black) or (game_type =="cp" and not active_black):
                    for (row,col) in possible_moves(coins,active_black):
                        board[row][col].configure(bg="blue")
            return
        # +++++++++++++++++++++++++++++++  skip white turn  +++++++++++++++++++++
        elif not active_black and not white_moves:
            active_black=not active_black
            player_lb.configure(text= f"{player_name(active_black,game_type)} playing now ...",foreground="black" if active_black  else "white")
            if game_type=="c" or game_type=="cp":
                AI_move()
            else:
                for row in range(8):
                    for col in range(8):
                        if board[row][col]["bg"]=="blue":
                            board[row][col].configure(bg="gray")
                if game_type =="p" or (game_type =="pc" and active_black) or (game_type =="cp" and not active_black):
                    for (row,col) in possible_moves(coins,active_black):
                        board[row][col].configure(bg="blue")
            return
def handle_move(row,col,cpass=False):
    Timer(0,apply_move,(row,col,cpass)).start()
    


################################################ start game ##############################################
init_board()
root.mainloop()
