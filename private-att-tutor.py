from pprint import pprint


class Counter:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current

    def reset(self):
        self.__current = 0

counter = Counter()

counter.increment()
counter.increment()
pprint(counter.__dict__)


counter.__current = -999

print(counter.value())

print(counter.__current)
pprint(counter.__dict__)

counter = Counter()
print(counter._Counter__current)


