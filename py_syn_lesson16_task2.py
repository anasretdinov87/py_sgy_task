class turtle(object):
    s = 1
    x = 1
    y = 1
    def go_up(self):
        self.y += self.s
    def go_down(self):
        self.y -= self.s
    def go_left(self):
        self.x -= self.s
    def go_right(self):
        self.x += self.s
    def evolve(self):
        self.s += 1
    def degrade(self):
        if (self.s - 1) > 0:
            self.s -= 1
        else:
            raise Exception('Ошибка. Шаг не может быть меньше нуля.')
    def count_moves(self, x2, y2):
        dist_x = abs(self.x - x2)
        dist_y = abs(self.y - y2)
        if dist_x % self.s == 0 and dist_y % self.s == 0:
            print(f'Минимальное количество действий, чтобы добраться: {int((dist_x + dist_y) / self.s)}')
        else: 
            raise Exception(f'При шаге {self.s} точка {x2}:{y2} от текущих координат не будет достигнута')    
    def current_coordinates(self):
        print(f'x:{self.x}:y:{self.y}')

t1 = turtle()
t1.current_coordinates()
t1.count_moves(1,6)
t1.go_up()
t1.count_moves(1,6)
t1.go_up()
t1.count_moves(1,6)
t1.go_up()
t1.count_moves(1,6)
t1.go_up()
t1.count_moves(1,6)
t1.go_up()
t1.count_moves(1,6)
t1.current_coordinates()
t1.count_moves(6,1)
t1.current_coordinates()
t1.go_right()
t1.go_down()
t1.go_right()
t1.go_down()
t1.go_right()
t1.go_down()
t1.go_right()
t1.go_down()
t1.go_right()
t1.go_down()
t1.count_moves(6,1)
t1.current_coordinates()
t1.evolve()
t1.evolve()
t1.count_moves(9,1)
t1.evolve()
t1.evolve()
t1.evolve()
t1.evolve()
t1.evolve()
t1.count_moves(9,1)
