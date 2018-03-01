class Vehicule:
    def __init__(self, id):
        self._row = 0
        self._col = 0
        self._ride = None
        self._nbRide = 0
        self._id = id

    def attributeRide(self, ride):
        self._ride = ride

    def distanceToEndRide(self):
        return abs((self._col - self._ride._colStart) + (self._row - self._ride._rowStart))