class Elevator():
    _all_calls = 0

    def __init__(self, name=None):
        self.call_counter = 0
        self.level = 0
        self.name = name

    def lift(self):
        self.call_counter += 1
        Elevator._all_calls += 1

    def __add__(self, other):
        self.level += other
        self.lift()
        return self.level


    def __sub__(self, other):
        if self.call_counter != 0:
            self.level -= other
            self.lift()
            return self.level
        else:
            raise ValueError('Wrong operation')

    def __eq__(self, other):
        if self.call_counter > other.call_counter:
            print('The first bigger.')
            return self
        elif self.call_counter < other.call_counter:
            print('The second bigger.')
            return other
        else:
            print('The same (return True).')
            return True

    def __str__(self):
        return str(self.name) + ' ; ' + str(self.call_counter) + ' ; ' + str(self.call_counter / self._all_calls * 100) + '%'

a = Elevator()
b = Elevator()
a == b
a + 5
b + 1
a - 1
a == b
b == a
print(a.level)
print(b.level)
print(a.call_counter)
print(b.call_counter)
print(Elevator._all_calls)
print(a)