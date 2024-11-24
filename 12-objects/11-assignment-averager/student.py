class Averager:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add(self, value):
       self.total += value
       self.count += 1

    def average(self):
        return self.total / self.count
    
    def reset(self):
        self.total = 0
        self.count = 0

my_average = Averager()
my_average.add(5)
my_average.add(20)

print(my_average.average())