class Vehicule:
    def __init__(self, id):
        self._row = 0
        self._col = 0
        self._ride = None
        self._nbRide = 0
        self._rideAttr = list()
        self._id = id
        self._startRide = False

    def isOnRide(self):
        if self._ride is not None:
            return True
        else:
            return False

    def attributeRide(self, ride):
        self._ride = ride
        self._nbRide += 1
        self._startRide = False
        self._rideAttr.append(self._ride._id)
        print('attribut ride id:', self._ride._id)

    def distanceToEndRide(self):
        return abs((self._col - self._ride._colStart) + (self._row - self._ride._rowStart))

    def move(self):
        if not self._startRide:
            print(self._col, self._row, self._ride._colStart, self._ride._rowStart)
            if not self.target(self._ride._colStart, self._ride._rowStart):
                self._startRide = True
                print('START RIDE')
            self.target(self._ride._colEnd, self._ride._rowEnd)
        else:
            if not self.target(self._ride._colEnd, self._ride._rowEnd):
                self._startRide = False
                self._ride = None

    def target(self, col, row):
        if self._col < col:
            self._col += 1
        elif self._col > col:
            self._col -= 1
        elif self._row < row:
            self._row += 1
        elif self._row > row:
            self._row -= 1
        else:
            print('target false')
            return False
        return True

    def print(self):
        print(self._nbRide, self._rideAttr)
