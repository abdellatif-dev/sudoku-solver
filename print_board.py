class Print_board:
    def __init__(self, bo):
        self.bo = bo

        for i in range(len(self.bo)):
            if i % 3 == 0 and i != 0:
                print("-------------------")

            for j in range(len(self.bo[0])):
                if j % 3 == 0 and j != 0:
                    print("|", end="")

                if j == 8:
                    print(self.bo[i][j])

                else:
                    print(str(self.bo[i][j]) + " ", end="")

