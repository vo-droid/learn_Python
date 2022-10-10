class PNumbers:
    def __init__(self, n):
        self.numbers = []
        self.n = n
        self.i = 0

    def __iter__(self):
        self.i = 1
        return self

    def next(self):
        self.i += 1
        for prime in self.numbers:
            if self.i % prime == 0:
                return None
        self.numbers.append(self.i)
        return self.i

    def __next__(self):
        value = None
        while value is None:
            value = self.next()
        if self.i < self.n:
            return value
        else:
            raise StopIteration()


prime_number_iterator = PNumbers(n=10)
for number in prime_number_iterator:
    print(number)