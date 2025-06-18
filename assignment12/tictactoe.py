#Task 6: More on Classes

#Declare a class called TictactoeException. This should inherit from the Exception class
class TictactoeException(Exception):
    #Add an __init__ method that stores an instance variable called message
    def __init__(self, message):
        self.message = message
        #Then call the __init__ method of the superclass
        super().__init__(message)

#Declare also a class called Board
class Board:
    #Board class should have a class variable called valid_moves
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    #Have an __init__ function that only has the self argument
    def __init__(self):
        #Create a list of lists, 3x3, all git containing " " as a value.
        #This is stored in the variable self.board_array.
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        #Create instance variables self.turn, which is initialized to "X"
        self.turn = "X"

    #Add a __str__() method. This converts the board into a displayable string
    def __str__(self):
        #The rows to be displayed are separated by newlines ("\n") and you also want some "|" amd "-" characters
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)

    #Add a move() method
    #Two arguments, self and move_string
    def move(self, move_string):
        #The following strings are valid in TicTacToe: "upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", and "lower right"
        #Checks for that by referencing valid_moves in the Board class
        if move_string not in Board.valid_moves:
            #When a string is passed, the move() method will check if it is one of these, and if not it will raise a TictactoeException with the message "That's not a valid move"
            raise TictactoeException("That's not a valid move.")

        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3

        #Then the move() method will check to see if the space is taken
        if self.board_array[row][column] != " ":
            #If so, it will raise an exception with the message "That spot is taken."
            raise TictactoeException("That spot is taken.")

        self.board_array[row][column] = self.turn
        #If neither is the case, the move is valid, the corresponding entry in board_array is updated with X or O, and the turn value is changed from X to O or from O to X.
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
    
    #Add a whats_next() method
    def whats_next(self):
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
                    break
            if not cat:
                break
        #If the board is full but no one has won, it returns a tuple where the first value is True and the second value is "Cat's Game"
        if cat:
            return (True, "Cat's Game.")
        
        win = False

        #Check rows
        for i in range(3):
            if self.board_array[i][0] != " " and \
               self.board_array[i][0] == self.board_array[i][1] == self.board_array[i][2]:
                win = True
                break

        #Check columns
        if not win:
            for i in range(3):
                if self.board_array[0][i] != " " and \
                   self.board_array[0][i] == self.board_array[1][i] == self.board_array[2][i]:
                    win = True
                    break

        # Check diagonals
        if not win:
            if self.board_array[1][1] != " ":
                if self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2] or \
                   self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0]:
                    win = True

        #Returns a tuple where the first value is False and the second value is either "X's turn" or "O's turn"
        if not win:
            return (False, f"{self.turn}'s turn.")
        ##If there are 3 X's or 3 O's in a row, it returns a tuple, where the first value is True and the second value is either "X has won" or "O has won".
        else:
            winner = "O" if self.turn == "X" else "X"
            return (True, f"{winner} wins!")


#Game
if __name__ == "__main__":
    #Display the board by doing a print(board)
    board = Board()

    while True:
        #At the start of the game, an instance of the board class is created
        #The methods of the board class are used to progress through the game
        print(board)
        print(f"{board.turn}'s move. Valid moves are:\n{Board.valid_moves}")
        #Use the input() function to prompt for each move, indicating whose turn it is
        move = input("Please enter next move: ").strip().lower()

        #Note that you need to call board.move() within a try block, with an except block for TictactoeException.
        try:
            board.move(move)
        except TictactoeException as e:
            print(f"Error: {e.message}")
            continue

        done, message = board.whats_next()
        if done:
            print(board)
            print(message)
            break
