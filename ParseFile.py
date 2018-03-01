class ParseFile:
    def __init__(self, file):
        self._file = open(file, 'r')

    def extractDataLine(self, separator):
        str = self._file.readline()
        if str == "":
            return []
        return str.split(separator)
