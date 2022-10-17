import sys
from queue import PriorityQueue
 
# Helper functions to aid in your implementation. Can edit/remove
#############################################################################
######## Piece
#############################################################################
class Piece:
    def __init__(self,pos,rows,cols,board):
        self.pos=pos
        self.cols=cols
        self.rows=rows
        self.board=board
    
    #get the col (num)
    def get_c(self):
        return self.pos[1]
    
    #get the row (num)
    def get_r(self):
        return self.pos[0]
 
#finding threat area particluar to each piece  
class Rook(Piece):
    def __init__(self,pos,rows,cols,board):
        super().__init__(pos,rows,cols,board)
 
    def moves(self):
        rook_moves=[]
        r,c=self.pos
        for i in range(r-1,-1,-1):
            if self.board[i,c]==-1:
                break
            else:
                if c<self.cols and c>=0:
                    rook_moves.append((i,c))
                continue
        for j in range(r+1,self.rows):
            if self.board[j,c]==-1:
                break
            else:
                if c<self.cols and c>=0:
                    rook_moves.append((j,c))
                continue
        for k in range(c+1,self.cols):
            if self.board[r,k]==-1:
                break
            else:
                if r<self.rows and r>=0:
                    rook_moves.append((r,k))
                continue
        for l in range(c-1,-1,-1):
            if self.board[r,l]==-1:
                break
            else:
                if r<self.rows and r>=0:
                    rook_moves.append((r,l))
                continue
        return rook_moves             
 
class Bishop(Piece):
    def __init__(self,pos,rows,cols,board):
        super().__init__(pos,rows,cols,board)
  
    def moves(self):
        r,c=self.pos
        bishop_moves=[]
        diag1 = zip(range(r+1,self.rows), range(c-1,-1,-1))
        diag2 = zip(range(r+1,self.rows), range(c+1,self.cols)) 
        diag3 = zip(range(r-1,-1,-1), range(c-1,-1,-1))
        diag4 = zip(range(r-1,-1,-1), range(c+1,self.cols))
        for r1,c1 in diag1:
            if r1<self.rows and r1>=0 and c1<self.cols and c1>=0:
                if self.board[r1,c1]==-1:
                    break
                else:
                    bishop_moves.append((r1,c1))
            else:
                continue
        for r2,c2 in diag2:
            if r2<self.rows and r2>=0 and c2<self.cols and c2>=0:
                if self.board[r2,c2]==-1:
                    break
                else:
                    bishop_moves.append((r2,c2))
            else:
                continue
        for r3,c3 in diag3:
            if r3<self.rows and r3>=0 and c3<self.cols and c3>=0:
                if self.board[r3,c3]==-1:
                    break
                else:
                    bishop_moves.append((r3,c3))
            else:
                continue
        for r4,c4 in diag4:
            if r4<self.rows and r4>=0 and c4<self.cols and c4>=0:
                if self.board[r4,c4]==-1:
                    break
                else:
                    bishop_moves.append((r4,c4))
            else:
                continue
        return bishop_moves
 
class Queen(Piece):
    def __init__(self,pos,rows,cols,board):
        super().__init__(pos,rows,cols,board)
 
    def moves(self):
        queen_moves=[]
        piece1=Rook(self.pos,self.rows, self.cols,self.board)
        piece2=Bishop(self.pos, self.rows, self.cols,self.board)
        queen_moves.extend(piece1.moves())
        queen_moves.extend(piece2.moves())
        return queen_moves
    
class Knight(Piece):
    def __init__(self,pos,rows,cols,board):
        super().__init__(pos,rows,cols,board)
 
    def moves(self): #fixed 8 moves around piece
        op1=[-2,1,-1,2,2,1,-1,-2] #for row movement
        op2=[1,2,2,1,-1,-2,-2,-1] #for col movement
        knight_moves=[]
        r,c=self.pos
        for index in range(0,8):
            if r+op1[index]< self.rows and r+op1[index]>=0 and c+op2[index]<self.cols and c+op2[index]>=0:
                if self.board[r+op1[index],c+op2[index]]!=-1:
                    knight_moves.append((r+op1[index],c+op2[index]))
                else:
                    continue
            else:
                continue
        return knight_moves
 
class King(Piece):
    def __init__(self,pos,rows,cols,board):
        super().__init__(pos,rows,cols,board)
 
    def moves(self):
        king_moves=[]
        r,c=self.pos
        for i in range(-1,2):
            for j in range(-1,2):
                if r+i<self.rows and c+j<self.cols and r+i>=0 and c+j>=0:
                    if (r+i,c+j)!=(r,c) and self.board[r+i,c+j]!=-1:
                        king_moves.append((r+i,c+j))
                    else:
                        continue
                else:
                    continue
        return king_moves
 
class Ferz(Piece):
    def __init__(self,pos,rows,cols,board):
        super().__init__(pos,rows,cols,board)
 
    def moves(self):
        ops=[-1,1]
        ferz_moves=[]
        r,c=self.pos
        for i in ops:
            for j in ops:
                if r+i<self.rows and r+i>=0 and c+j<self.cols and c+j>=0:
                    if self.board[r+i,c+j]!=-1:
                        ferz_moves.append((r+i,c+j))
                    else:
                        continue
                else:
                    continue
        return ferz_moves
 
class Princess(Piece):
    def __init__(self,pos,rows,cols,board):
        super().__init__(pos,rows,cols,board)
 
    def moves(self):
        princess_moves=[]
        piece1=Bishop(self.pos,self.rows, self.cols,self.board)
        piece2=Knight(self.pos, self.rows, self.cols, self.board)
        princess_moves.extend(piece1.moves())
        princess_moves.extend(piece2.moves())
        return princess_moves
    
class Empress(Piece):
    def __init__(self,pos,rows,cols,board):
        super().__init__(pos,rows,cols,board)
 
    def moves(self):
        empress_moves=[]
        piece1=Rook(self.pos,self.rows, self.cols,self.board)
        piece2=Knight(self.pos, self.rows, self.cols,self.board)
        empress_moves.extend(piece1.moves())
        empress_moves.extend(piece2.moves())
        return empress_moves
 
############################################################################
######## Board
#############################################################################
class Board:
    def __init__(self,r,c):
        self.r=r
        self.c=c
 
    def create_board(self,grid):
        dic = {}
        for i,val in enumerate(grid):
            for j,val2 in enumerate(val):
                dic[i,j]=val2
        return dic
            
#############################################################################
######## State
#############################################################################
 
class State:
    def __init__(self,board,total_pieces,num_variables,assignments,domain):
        self.board = board 
        self.total_pieces=total_pieces #integer total num of pieces
        self.num_variables=num_variables #name: num_piece
        self.assignments=assignments #pos:name
        self.domain=domain #name:list of available position
                    
    def complete(self): #complete and consistent: ALL assigned values
        if self.total_pieces==len(self.assignments):
            return True
        else:
            return False
 
    def consistent(self,var,pos,rows,cols): #consistent: all constraints satisfied
        #Constraint: no threat position selected and no obstacle position selected
        for p,n in list(self.assignments.items()): #piece=(name,pos)
            #threats=each_threaten(rows,cols,n,p,self.board)
            threats2=each_threaten(rows,cols,var,pos,self.board)
            if pos != p :
                if p in threats2 or self.board[pos[0],pos[1]]==-1:
                    return False
        return True
 
#############################################################################
######## Implement Search Algorithm
#############################################################################
 
def search(rows, cols, grid, num_pieces): #check back on slide 22 for last troubleshooting bit
    
    board = Board(rows, cols)
    board=board.create_board(grid)
 
    num_variables=available_pieces_vars(num_pieces) #name:num
    total_pieces=sum(num_pieces) #total available num of pieces
    domain=pieces_dict(num_pieces,grid) #initial domain is same for all 
    initial_state=State(board,total_pieces,num_variables,{},domain)
 
    return backtrack(initial_state,rows,cols)
 
def available_pieces_vars(num_pieces): #dictionary to map every piece and the no. of those pieces
    board_vars={}
    p=['King','Queen','Bishop','Rook','Knight','Ferz','Princess','Empress']
    for i,j in zip(num_pieces,p):
        if i>0:
            board_vars[j]=i
        else:
            continue
    #available_pieces = [key for key, value in board_vars.items() for _ in range(value)]
    return board_vars
 
def pieces_dict(num_pieces,grid): #dictionary to map every piece and initial domain
    dict={}
    lst=list(available_pieces_vars(num_pieces).keys())
    p=['King','Queen','Bishop','Rook','Knight','Ferz','Princess','Empress']
    for i,j in zip(num_pieces,p):
        if i>0:
            dict[j]=[]
    for k in lst:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]!=-1:
                    dict[k].append((0,0,(r,c)))
                else:
                    continue
    return dict
 
def backtrack(state,rows,cols):
    if state.complete(): #final dictionary after conversion
        final={}
        for piece,type in state.assignments.items():
            final[convert_to_char(piece[1]),piece[0]]=type
        return final
 
    var=select_unassigned_variable(state)
    dom=order_domain_values(state,var,rows,cols)
    state.domain[var]=dom
    #print(dom)
    #print(var)
 
    for pos in dom:
        position=pos[2]
        if state.consistent(var,position,rows,cols) and position not in list(state.assignments.keys()):
            state.assignments[position]=var
            state.num_variables[var]-=1
            
            new_state=State(state.board,state.total_pieces,state.num_variables,state.assignments,state.domain)
 
            if forward_check(new_state,var,rows,cols): #and new_state.consistent(var,position,rows,cols):
                new_state.board[position[0],position[1]]=-2 #threatened now that it is assigned
                result = backtrack(new_state,rows,cols)
                if result:
                    return result
            state.num_variables[var]+=1
            del state.assignments[position]
    return None
 
def forward_check(state,var,rows,cols):
    return (state.total_pieces-len(state.assignments)) <= len(order_domain_values(state,var,rows,cols))
 
def select_unassigned_variable(state): #select name of variable (most constrained to least constrained)
    seq_to_explore=['Queen','Empress','Princess','Bishop','Rook','Knight','King','Ferz']
    for check in seq_to_explore:
        for piece1 in list(state.num_variables.keys()):
            if piece1==check and state.num_variables[piece1]>0:
                return piece1
            else:
                continue
 
def get_domain(state,var):
    final=[]
    for tup in state.domain[var]:
        final.append(tup[2])
    return final   
 
def order_domain_values(state,var,rows,cols): 
    #list of all possible free positions to move to, assigning to dict later
    #lst=[]
    lcv=PriorityQueue()
 
    lst=get_domain(state,var)
    
    for pos1,n1 in list(state.assignments.items()):
        t=each_threaten(rows,cols,n1,pos1,state.board)
        for ele in lst:
            if ele in t:
                lst.remove(ele)
                state.board[ele[0],ele[1]]=-2

    threaten_area(state,rows,cols)

    for (i3,j3) in lst:
        n=num_threats(state,i3,j3,var,rows,cols)
        later=0
        if var=='Queen' and (i3,j3)==(0,0): #bug when Queen at (a,0) as first choice so try again for (a,0) in Queen
            later=1
        lcv.put((n,later,(i3,j3)))
    return lcv.queue
 
def num_threats(state,r,c,var,rows,cols):
    num=len(each_threaten(rows,cols,var,(r,c),state.board))
    return num
 
def each_threaten(rows,cols,name,pos,board):
    if name=='King':
        return King(pos,rows,cols,board).moves()
    elif name=='Queen':
        return Queen(pos,rows,cols,board).moves()
    elif name=='Bishop':
        return Bishop(pos,rows,cols,board).moves()
    elif name=='Rook':
        return Rook(pos,rows,cols,board).moves()
    elif name=='Ferz':
        return Ferz(pos,rows,cols,board).moves()
    elif name=='Princess':
        return Princess(pos,rows,cols,board).moves()
    elif name=='Empress':
        return Empress(pos,rows,cols,board).moves()
    else:
        return Knight(pos,rows,cols,board).moves()
 
def threaten_area(state,rows,cols): #same as BFS instead of enemy pieces
    threat_area=[]
    for pos,name in state.assignments.items():
        if name=='Rook':
            threat_area.extend(Rook(pos,rows,cols,state.board).moves())
        elif name=='Bishop':
            threat_area.extend(Bishop(pos,rows,cols,state.board).moves())
        elif name=='Queen':
            threat_area.extend(Queen(pos,rows,cols,state.board).moves())
        elif name=='Knight':
            threat_area.extend(Knight(pos,rows,cols,state.board).moves())
        elif name=='Ferz':
            threat_area.extend(Ferz(pos,rows,cols,state.board).moves())
        elif name=='Princess':
            threat_area.extend(Princess(pos,rows,cols,state.board).moves())
        elif name=='Empress':
            threat_area.extend(Empress(pos,rows,cols,state.board).moves()) 
        else:
            threat_area.extend(King(pos,rows,cols,state.board).moves())
    for (i,j) in set(threat_area):
        state.board[i,j]=-2
 
def convert_to_char(n):
    return chr(n + 97)

#############################################################################
######## Parser function and helper functions
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
def parse(testcase):
    handle = open(testcase, "r")

    get_par = lambda x: x.split(":")[1]
    rows = int(get_par(handle.readline()))
    cols = int(get_par(handle.readline()))
    grid = [[0 for j in range(cols)] for i in range(rows)]

    num_obstacles = int(get_par(handle.readline()))
    if num_obstacles > 0:
        for ch_coord in get_par(handle.readline()).split():  # Init obstacles
            r, c = from_chess_coord(ch_coord)
            grid[r][c] = -1
    else:
        handle.readline()
    
    piece_nums = get_par(handle.readline()).split()
    num_pieces = [int(x) for x in piece_nums] #List in the order of King, Queen, Bishop, Rook, Knight

    return rows, cols, grid, num_pieces

def add_piece( comma_seperated):
    piece, ch_coord = comma_seperated.split(",")
    r, c = from_chess_coord(ch_coord)
    return [(r,c), piece]

#Returns row and col index in integers respectively
def from_chess_coord( ch_coord):
    return (int(ch_coord[1:]), ord(ch_coord[0]) - 97)

### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# To return: Goal State which is a dictionary containing a mapping of the position of the grid to the chess piece type.
# Chess Pieces (String): King, Queen, Knight, Bishop, Rook (First letter capitalized)
# Positions: Tuple. (column (String format), row (Int)). Example: ('a', 0)

# Goal State to return example: {('a', 0) : Queen, ('d', 10) : Knight, ('g', 25) : Rook}
def run_CSP():
    testcase = sys.argv[1] #Do not remove. This is your input testfile.
    rows, cols, grid, num_pieces = parse(testcase)
    goalstate = search(rows, cols, grid, num_pieces)
    return goalstate #Format to be returned

#print(parse('Public Testcases/CSP3.txt'))

#print(run_CSP())