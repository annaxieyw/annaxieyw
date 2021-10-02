# from: Anna Xie
#
# Computer Science 111 - ps9pr1.py
# Connect-Four Board class 
#

class Board:
    """ a data type for a Connect Four board with
        arbitrary dimensions
    """
    def __init__(self, height, width):
        """ constructs a new Board object """
        self.height = height
        self.width = width
        self.slots = [[' ']* width for r in range(height)]

    def __repr__(self):
        """ returns a string representation of a Board """
        s = '' 
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'
        s += self.width * 2 * '-' + '-'
        s += '\n'
        for i in range(self.width):
            s += ' ' + str(i % 10)
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker to column col """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        row = self.height - 1
        while self.slots[row][col] != ' ':
            row -= 1
        self.slots[row][col] = checker

    def reset(self):
        """ reset the Board object on which it is called by setting all slots to contain a space character """
        self.slots = [[' ']* self.width for r in range(self.height)]

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'
        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """ returns True if it is valid to place a checker in the column col on the calling Board object. Otherwise, it should return False """
        if col < 0 or col >= self.width:
            return False
        for row in range(self.height):
            if self.slots[row][col] == ' ':
                return True
        return False

    def is_full(self):
        """ returns True if the called Board object is completely full of checkers, and returns False otherwise """
        for col in range(self.width):
            if self.can_add_to(col) == True:
                return False
        return True

    def remove_checker(self, col):
        """ removes the top checker from column col of the called Board object """
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                break

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for col in range(self.width):
            for row in range(self.height - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False

    def is_up_diagonal_win(self, checker):
        """ Checks for a up diagonal win for the specified checker.
        """
        for col in range(self.width):
            for row in range(self.height - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col - 1] == checker and \
                   self.slots[row + 2][col - 2] == checker and \
                   self.slots[row + 3][col - 3] == checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        """ Checks for a down diagonal win for the specified checker.
        """
        for col in range(self.width - 3):
            for row in range(self.height - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
        return False

    def is_win_for(self, checker):
        """ returns True if there are four consecutive slots containing checker on the board. Otherwise, it should return False.
            input: a parameter checker that is either 'X' or 'O'
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) == True or \
           self.is_vertical_win(checker) == True or \
           self.is_up_diagonal_win(checker) == True or \
           self.is_down_diagonal_win(checker) == True:
            return True
        return False
