class Jar:
    def __init__(self, capacity=12, size=0):
        if capacity > 0:
            self.capacity = capacity
        else:
            raise ValueError("Capacity must be More than zero")
        self.size = size

    def __str__(self):
        # if print(jar)
        return "🍪" * self.size

    # should add n cookies to the cookie jar
    def deposit(self, n):
        if n <= (self.capacity - self.size) and n > 0:
            self.size += n
        else:
            raise ValueError("To many cookies !")

    # should remove n cookies from the cookie jar
    def withdraw(self, n):
        if n < self.size:
            self.size -= n
        else:
            raise ValueError("To few cookies !")

    # getter for capacity
    @property
    def capacity(self):
        return self._capacity

    # getter for size
    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) > 0 :
            self._capacity = capacity
        else:
            raise ValueError("capacity not True !")

    @size.setter
    def size(self, size):
        if int(size) >= 0:
            self._size = size
        else:
            raise ValueError("size not True !")


def main():
    print(Jar)


if __name__ == "__main__":
    main()
