import json

class Main(object):
    """docstring for Main"""
    def __init__(self, fileName):
        super(Main, self).__init__()
        self.load_properties_from_json(fileName)

    def load_properties_from_json(self, fileName):
        dataFile = open(fileName, 'r')
        try:
            self.data = json.loads(dataFile.read())
        finally:
            dataFile.close()
            print("Properties from", fileName, "successfully loaded.")


def main():
    main = Main("properties.json")

if __name__ == '__main__':
    main()
