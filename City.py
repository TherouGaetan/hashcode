from hashcode.ParseFile import ParseFile


class City:
    def __init__(self):
        self._rows = 0
        self._cols = 0
        self._stepMax = 0
        self._rides = list()
        self._fleet = list()

    def parseFile(self, file):
        parser = ParseFile(file)
        self.initCity(parser.extractDataLine(' '))

    def initCity(self, data):
        self._rows = data[0]

    def algo(self):
        return None

if __name__ == "__main__":
    city = City()

    city.parseFile("./a_example.in")
