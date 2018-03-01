class Vehicule:
    def __init__(self, id):
        self._row = 0
        self._col = 0
        self._ride = None
        self._id = id

    def attributeRide(self, ride):
        self._ride = ride