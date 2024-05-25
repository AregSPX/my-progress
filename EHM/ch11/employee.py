class Employee:

    def __init__(self, first, last, salary):
        self.name = first
        self.surname = last
        self.w = salary
    
    def give_raise(self, d = 5000):
        self.w += d