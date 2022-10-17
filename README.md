# n-pieces-goal-finding

Similar to n-queens problem, here we use n-pieces threatening one another so we have to place the given pieces in a way that none of them threaten each other with obstacles on the varying chessboard

The pieces are: King, Queen, Rook, Bishop, Knight and fairy pieces like Ferz, Princess, Empress

I have implemented two approaches for this:

1. Local Search using Stochastic Hill Climbing
In this implementation, pieces are pre-populated on the board and we are supposed to remove n-k pieces so that atleast k pieces remain without threatening one another

2. Constraint Satisfaction Problem using backtracking
In this implementation, we assign the pieces given, one by one fulfilling the obstacle and threat constraints 
