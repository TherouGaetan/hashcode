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
        i = 1
        while len(data) != 0:
            ride = Ride(data, i)
            self._rides.append(ride)
            data = parser.extractDataLine(' ')
            i += 1

    def initCity(self, data):
        self._rows = data[0]
        self._cols = data[1]
        self._bonus = data[4]
        self._stepMax = int(data[5])
        for i in range (0, data[2]) :
            list.append(Vehicule(i))

    def printCity(self):
        print('Row: ', self._rows)
        print('Col: ', self._cols)
        print('Max step: ', self._stepMax)
        print('Nb ride: ', len(self._rides))
        print('Nb Vehicule: ', len(self._fleet))

    def algo(self):
        return None


if __name__ == "__main__":
    city = City()

    city.parseFile("./a_example.in")
    city.printCity()
