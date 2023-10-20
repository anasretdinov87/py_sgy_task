from utils import randbool

#0 - field
#1 - tree
#2 - river
#3 - hospital 🏥
#4 - upgrade store 🏫

class Map:  
    #def generate_rivers(self):
    
    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r. mxr):
                    self.cells[ri][ci] = 1
    def print_map(self):
        print('⬛ ' * (self.w + 2))
        for row in self.cells:
            print('⬛ ', end ="")
            for cell in row:
                if cell == 0:
                    print('🟩', end="")
                elif cell == 1:
                    print('🌲 ', end="")
                elif cell == 2:
                    print('🌊 ', end="")
                elif cell == 3:
                    print('🏥 ', end="")
                elif cell == 4:
                    print('🏫 ', end="") 
            print('⬛ ')    
        print('⬛ ' * (self.w + 2))    

    def check_bounds(self, x, y):
        if(x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True                      

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]


tmp = Map(10, 10)
tmp.cells[1][1] = 1
tmp.cells[2][2] = 2
tmp.cells[3][3] = 3
tmp.cells[4][4] = 4
if (tmp.check_bounds(5, 5)):
    print("YES")
tmp.print_map()
