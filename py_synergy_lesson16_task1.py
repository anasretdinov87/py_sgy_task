class cashbox(object):
    sum = 0
    def top_up(self, x):
        self.sum += x
    def count_1000(self):
        print(f'Целых тысяч в кассе: {self.sum // 1000}')
    def take_away(self, x):
        if x <= self.sum:
            self.sum -= x
            print(f'Из кассы забрали {x}. Остаток: {self.sum}')
        else:
            raise Exception("Недостаточно денег")

c1 = cashbox()
c1.top_up(1000)
c1.count_1000()
c1.take_away(1000)
c1.take_away(1000)