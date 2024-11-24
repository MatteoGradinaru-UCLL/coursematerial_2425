class Interval:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper    

    
    def is_empty(self):
        if self.lower > self.upper:
            return True
        else:
            return False
        
    def contains(self, value):
        if self.lower <= value <= self.upper:
            return True
        else:
            return False
    
    def overlaps_with(self, other):

        if self.is_empty() or other.is_empty(): 
            return False
        else:
            return self.contains(other.lower) or self.contains(other.upper) or other.contains(self.lower) or other.contains(self.upper)

my_interval = Interval(1, 5)
print(my_interval.overlaps_with(Interval(6, 10)))