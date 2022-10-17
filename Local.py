import sys
import random

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
    def __init__(self, board, pieces,threats): #need to update the entire state with each move
        self.board = board #important to reinitialise
        self.pieces = pieces #list of pieces name and positions (name,pos)
        self.h_value = {} #h_value mappings
        self.threats=threats #track of total threats at each stage

    def initial_heurist(self):
        self.h_value={}
        for n1,pos1 in self.pieces: #initially assigning all h values to 0
            self.h_value[pos1]=0 #using the (name,pos) tuple as a key (_hash_ giving errors)
        return self.h_value
    
    def heurist(self,rows,cols): #comapring threat pairs   
        self.h_value=self.initial_heurist()      
        for n,pos in self.pieces:
            threats=each_threaten(rows,cols,n,pos,self.board)
            for n2,pos2 in self.pieces:
                if pos2 in threats:
                    if pos2 != pos:
                        self.h_value[pos]+=1 #assigning h value of each piece pair
                        self.h_value[pos2]+=1
                    else:
                        continue
                else:
                    continue 
        result=sum(self.h_value.values()) #value of heurist at every board state as a whole
        return -result #f(n)=-h(n)

#############################################################################
######## Implement Search Algorithm
#############################################################################
def search(rows, cols, grid, pieces, k):  
    k = int(k) #>=' not supported between instances of 'int' and 'str'
    board = Board(rows,cols)
    board=board.create_board(grid)

    all_pieces=listing_pieces(pieces,board) #putting all pieces as (name,pos) tuples
    all_pieces_threat=threaten(rows,cols,pieces,board)
    count=0 #troubleshooting for no. of loops

    while True:
        count+=1
        curr=State(board,all_pieces.copy(),all_pieces_threat.copy()) #can't add list itself, need to add copy as deleting and updating old list can cause looping infinitely
        board=curr.board #reinitialise board every time
        current=random.choice(curr.pieces) #random choice at first-go
        local_found=False #need to set in every statement to avoid infinite loop
    
        while len(curr.pieces)>=k and local_found==False:
            curr_value=curr.heurist(rows,cols)
            #print(count)
            possible_neighbors=all_neighbors(curr,current,rows,cols,board)
            chosen_neighbor=random.choice(possible_neighbors)

            if curr.heurist(rows,cols)<curr_value:
                local_found=True
                current=random_restart(curr,k) #start again as value is less than current state 

            if len(curr.pieces)<k:
                local_found=True
                current=random_restart(curr,k) #start again as less than k pieces 

            if curr.heurist(rows,cols)>=curr_value and len(curr.pieces)>=k:
                current=chosen_neighbor #continue with new current
                local_found=False

            if curr.heurist(rows,cols)==0 and len(curr.pieces)>=k: #check if total h-value is reached 0 
                res={}
                for p in curr.pieces:
                    position=p[1]
                    position=(convert_to_char(position[1]),position[0])
                    res[position]=p[0]
                return res

def all_neighbors(curr,current,rows,cols,board): #calculate max h for all remaining in pieces list
        all_neighbors=[]
        curr.pieces.remove(current) #removing current piece from list of pieces
        curr.h_value[current[1]]=0 #removing h value mapping for current as well
        curr.board[current[0],current[1]]=0 #empty space at current now
        threats2=each_threaten(rows,cols,current[0],current[1],board)
        curr.threats.remove(threats2) #not threatening the other pieces anymore
        
        maximum=max(list(curr.h_value.values()))
        for piece in curr.pieces: # all max h value neighbors added
            if piece[1] in list(curr.h_value.keys()) and curr.h_value[piece[1]]==maximum:
                all_neighbors.append(piece)
        return all_neighbors

def random_restart(state,k,limit=20):
    count=0
    if len(state.pieces)>k and count<limit: #need to arbitarily set limit so no constant looping
        selected=random.choice(state.pieces)
        count+=1 
        return selected

def listing_pieces(pieces,board):
    all_pieces=[]
    for key,val in pieces.items():
        all_pieces.append((val,key)) #(name,pos) tuples
        board[key[0],key[1]]=1 #occupied pieces assigned to 1
    return all_pieces

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

def threaten(rows,cols,pieces,board):
    threat_area=[]
    for k,v in pieces.items():
        if v=="King":
            threat_area.append(King(k,rows,cols,board).moves())
        elif v=="Queen":
            threat_area.append(Queen(k,rows,cols,board).moves())
        elif v=="Bishop":
            threat_area.append(Bishop(k,rows,cols,board).moves())
        elif v=="Rook":
            threat_area.append(Rook(k,rows,cols,board).moves())
        elif v=="Ferz":
            threat_area.append(Ferz(k,rows,cols,board).moves())
        elif v=="Princess":
            threat_area.append(Princess(k,rows,cols,board).moves())
        elif v=="Empress":
            threat_area.append(Empress(k,rows,cols,board).moves())
        else:
            threat_area.append(Knight(k,rows,cols,board).moves())
    return threat_area

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
    k = 0
    pieces = {}

    num_obstacles = int(get_par(handle.readline()))
    if num_obstacles > 0:
        for ch_coord in get_par(handle.readline()).split():  # Init obstacles
            r, c = from_chess_coord(ch_coord)
            grid[r][c] = -1
    else:
        handle.readline()
    
    k = handle.readline().split(":")[1].strip() # Read in value of k

    piece_nums = get_par(handle.readline()).split()
    num_pieces = 0
    for num in piece_nums:
        num_pieces += int(num)

    handle.readline()  # Ignore header
    for i in range(num_pieces):
        line = handle.readline()[1:-2]
        coords, piece = add_piece(line)
        pieces[coords] = piece    

    return rows, cols, grid, pieces, k

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
def run_local():
    testcase = sys.argv[1] #Do not remove. This is your input testfile.
    rows, cols, grid, pieces, k = parse(testcase)
    goalstate = search(rows, cols, grid, pieces, k)
    return goalstate #Format to be returned

#print(parse('Public Testcases/Local1.txt'))

#print(run_local())