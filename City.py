from hashcode.ParseFile import ParseFile
from hashcode.Ride import Ride


class City:
    def __init__(self):
        self._rows = 0
        self._cols = 0
        self._bonus = 0
        self._stepMax = 0
        self._rides = list()
        self._fleet = list()

    def parseFile(self, file):
        parser = ParseFile(file)
        self.initCity(parser.extractDataLine(' '))
        data = parser.extractDataLine(' ')
        while len(data) != 0:
            ride = Ride(data)
            self._rides.append(ride)
            data = parser.extractDataLine(' ')

    def initCity(self, data):
        self._rows = data[0]
        self._cols = data[1]
        self._bonus = data[4]
        self._stepMax = int(data[5])

    def printCity(self):
        print('Row: ', self._rows)
        print('Col: ', self._cols)
        print('Max step: ', self._stepMax)
        print('Nb ride: ', len(self._rides))

    def algo(self):
        return None


if __name__ == "__main__":
    city = City()

    city.parseFile("./a_example.in")
    city.printCity()
