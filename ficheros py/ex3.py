import json
from globales import getFile, toListOfDictionaries, constants

def writeOnJson (book : list):
    with open(constants.PATHFITXEROJSON, "w") as outfile:
        jsonString = json.dumps(book)
        outfile.write(jsonString)
def main3():
    file = getFile(constants.SEPARADOROLD)
    if file == None:
        return
    book = toListOfDictionaries(file)
    writeOnJson(book)
    print("El teu fitxer json s'ha creat correctament, el path és: " + constants.PATHFITXEROJSON)
if __name__ == "__main__":
    main3()