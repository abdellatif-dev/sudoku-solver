class Check:
    def __init__(self, bo):
        self.bo = bo

    def Find_Empty(self, bo):
        for i in range(len(self.bo)):
            for j in range(len(self.bo[0])):
                if self.bo[i][j] == 0:
                    return (i, j) # cords

        return None

    def Is_Valid(self, bo, num, pos):

        #row
        for i in range(len(self.bo[0])):
            if self.bo[pos[0]][i] == num and pos[1] != i:
                return False

        #collum
        for i in range(len(self.bo)):
            if self.bo[i][pos[1]] == num and pos[0] != i:
                return False

        #box
        self.box_x = pos[1] // 3
        self.box_y = pos[0] // 3

        for i in range(self.box_y * 3, self.box_y*3+3):
            for j in range(self.box_x * 3, self.box_x*3+3):
                if bo[i][j] == num and (i, j) != pos:
                    return False

        return True
