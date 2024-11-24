class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
    
    def reset(self):
        self.count = 0

my_counter = Counter()
my_counter.increment()
my_counter.increment()

print(my_counter.count)