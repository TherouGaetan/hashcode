class Ride:
    def __init__(self, array, id):
        self._rowStart = int(array[0])
        self._colStart = int(array[1])
        self._rowEnd = int(array[2])
        self._colEnd = int(array[3])
        self._start = int(array[4])
        self._end = int(array[5])
        self._id = int(id) - 1

    def printRide(self):
        print(self._id, self._rowStart, self._colStart, self._rowEnd, self._colEnd, self._start, self._end)

    def __lt__(self, other):
        return self._start < other._start
