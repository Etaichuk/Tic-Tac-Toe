
from board import Board

print("Hello bitches, welcome to tic tac toe! %---D~\n")


if __name__ == '__main__':

    dim_table = input("What table size do you want: rows,columns ?\n")
    p_1 = int(str.split(dim_table, ',')[0])
    p_2 = int(str.split(dim_table, ',')[1])
    board = Board(p_1,p_2)
    print(board)
    win_num = int(input('what is the winning strick?\n'))
    current_player=0
    while not (board.result(win_num) > 0 or board.full()):

        A = input(f"Shithead {current_player+1} your move:\n")
        x = int(str.split(A, ',')[0])
        y = int(str.split(A, ',')[1])
        if board.move(current_player, (x,y)):
            current_player=1-current_player
            print(board)

        # if move is legal, do this >>>>
    if board.result(win_num)>0:
        w = board.result(win_num)
        print(f'Player {w} wins!')

    else:
        print('Tie game')