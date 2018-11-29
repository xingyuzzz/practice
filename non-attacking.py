
board =[[0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0]]

num = 0 #numbers of solutions

def eight_queen(arr,finish_line=0):
    # if successfully put queens in every row, then one solution is found
    if finish_line == len(arr):
        for x in range(len(board)):
            for y in range(len(board)):
                board[x][y]=0
        global num
        num+=1
        print("solutioin：")
        for i in range(8):
            for x in range(len(board)):
                for y in range(len(board)):
                    if i == x and arr[i]==y:
                        board[x][y] = '1'
        print(board)
        return
    for col in range(len(arr)):
        arr[finish_line] = col
        flag = True
        #put a queen in [finishLine,col] first and then check if it is valid later
        for line in range(finish_line):
            # if the y coordinates are the same or the two queens are places in diagonal, it is invalid
            if arr[line] == col or abs(arr[line]-col) == finish_line-line:
                flag = False
        if flag==True:
            eight_queen(arr,finish_line+1)



eight_queen([None]*8)
print("there are %r different solutions"%num)
