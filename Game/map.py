from utils import randbool
from utils import randcell
from utils import randcell2
#0 - field
#1 - tree
#2 - river
#3 - hospital 🏥
#4 - upgrade store 🏫

class Map:  
    def generate_river(self, l):
        sum_free_cells = 0
        for i in range(self.h):
            for j in range(self.w):
                if self.cells[i][j] != 2:
                    sum_free_cells += 1
        if  sum_free_cells > 0:
            check_init_cell = False
            while not check_init_cell:       
                rc = randcell(self.w, self.h)
                rx, ry = rc[0], rc[1]
                if (self.check_water(rx, ry)):
                    self.cells[rx][ry] = 2 
                    l -= 1
                    check_init_cell = True
        if l > sum_free_cells:
            l = sum_free_cells
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]            
            if (self.check_bounds(rx2, ry2)):
                    if (self.check_water(rx2, ry2)):
                        self.cells[rx2][ry2] = 2
                        rx, ry = rx2, ry2
                        l -= 1
                    else:
                        rx = rx2
                        ry = ry2
    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
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

    def check_water(self, x, y):
        if self.cells[x][y] == 2:
            return False
        return True          

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]


tmp = Map(9, 10)
tmp.generate_forest(3, 10)
tmp.generate_river(10)
tmp.print_map()
