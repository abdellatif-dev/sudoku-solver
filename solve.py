from check import Check

class Solve(Check):
    def __init__(self, bo):
        self.bo = bo

        self.solve(self.bo)

    def solve(self, bo):

        find = self.Find_Empty(self.bo)

        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.Is_Valid(self.bo, i, (row, col)):
                self.bo[row][col] = i

                if  self.solve(self.bo):
                    return True

                self.bo[row][col] = 0

        return False