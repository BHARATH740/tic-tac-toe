class TicTacToe():

    def __init__(self, symbol):
        # initialize symbols
        self.symbols_list = []

        # defines all nine symbols; all start as blank  
        for i in range(9):
            self.symbols_list.append(" ") 

        # initializes the player symbol
        self.player_symbol = symbol


    def restart_game(self):
        for i in range(9):
            self.symbols_list[i] = " "


    def draw_grid(self):
        print("\n       A   B   C\n")
        
        # display first row 
        row1 = "   1   " + self.symbols_list[0]
        row1 += " ║ " + self.symbols_list[1]
        row1 += " ║ " + self.symbols_list[2]
        print(row1)

        # display divider
        print("      ═══╬═══╬═══")

        # display second row 
        row2 = "   2   " + self.symbols_list[3]
        row2 += " ║ " + self.symbols_list[4]
        row2 += " ║ " + self.symbols_list[5]
        print(row2)

        # display divider
        print("      ═══╬═══╬═══")

        # display third and last row 
        row3 = "   3   " + self.symbols_list[6]
        row3 += " ║ " + self.symbols_list[7]
        row3 += " ║ " + self.symbols_list[8]
        print(row3, "\n")


    def edit_square(self, coords):
        # swamps coordinates such as "1A" to "A1"
        if coords[0].isdigit():
            coords = coords[1] + coords[0]

        # divides the coordinate 
        col = coords[0].capitalize()
        row = coords[1]

        # converts "A1" to 0, "C3" to 8, and so forth 
        grid_index = 0

        if row == "1":
            if col == "A":
                grid_index = 0
            elif col == "B":
                grid_index = 1
            elif col == "C":
                grid_index = 2
        elif row == "2":
            if col == "A":
                grid_index = 3
            elif col == "B":
                grid_index = 4
            elif col == "C":
                grid_index = 5
        elif row == "3":
            if col == "A":
                grid_index = 6
            elif col == "B":
                grid_index = 7
            elif col == "C":
                grid_index = 8

        if self.symbols_list[grid_index] == " ":
            self.symbols_list[grid_index] = self.player_symbol


    def update_symbol_list(self, updated_list):
        for i in range(9):
            self.symbols_list[i] = updated_list[i]


    def did_win(self, symbol):
        g = []
        for i in range(9):
            g.append(self.symbols_list[i])
        s = symbol
        if g[0] == s and g[1] == s and g[2] == s:
            return True
        elif g[3] == s and g[4] == s and g[5] == s:
            return True
        elif g[6] == s and g[7] == s and g[8] == s:
            return True 
        elif g[0] == s and g[3] == s and g[6] == s:
            return True 
        elif g[1] == s and g[4] == s and g[7] == s:
            return True 
        elif g[2] == s and g[5] == s and g[8] == s:
            return True
        elif g[2] == s and g[4] == s and g[6] == s:
            return True 
        elif g[0] == s and g[4] == s and g[8] == s:
            return True 
        return False


    def is_draw(self):
        num_of_blanks = 0
        for i in range(9):
                if self.symbols_list[i] == " ":
                    num_of_blanks += 1
        if self.did_win(self.player_symbol) == False and num_of_blanks == 0:
            return True
        else:
            return False