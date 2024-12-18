class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [0] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        assert (
            i < self.size
        )  # Can only set an index that is within the size of the array
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.size += 1

        self.set(self.size - 1, n)

    def popback(self) -> int:
        assert self.size > 0  # Can only pop if the array has items

        self.size -= 1
        return self.array[self.size]

    def resize(self) -> None:
        newSize = self.capacity * 2
        self.array += [0] * self.capacity
        self.capacity = newSize

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
