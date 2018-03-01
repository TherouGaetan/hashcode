class Ride:
    def __init__(self, array, id):
        self._rowStart = array[0]
        self._colStart = array[1]
        self._rowEnd = array[2]
        self._colEnd = array[3]
        self._start = array[4]
        self._end = int(array[5])
        self._id = id

    def printRide(self):
        print(self._rowStart, self._colStart, self._rowEnd, self._colEnd, self._start, self._end)
