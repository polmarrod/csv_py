import csv
class constants ():
    PATHFITXERO = "basket_players.csv"
    PATHNEWFITXERO = "jugadors_basket.csv"
    FOOT = 2.54
    POUND = 0.45
    SEPARADOROLD= ";"
    SEPARADORNEW = "^"
    NAME = "names"
    TEAM = "team"
    POSITION = "position"
    HEIGHT = "height"
    WEIGHT = "weight"
    AGE = "age"
    
    NEWHEADERS = ["Nom", "Equip", "Posicio", "Altura", "Pes", "Edat"]
    NEWPOSITIONS = {
        "Point Guard" : "Base",
        "Shooting Guard" : "Escorta",
        "Small Forward" : "Aler",
        "Power Forward" : "Ala-pivot",
        "Center" : "Pivot"
    }

def toDictionarie(reader : enumerate):
    dictionarie = {
        constants.NAME : [],
        constants.TEAM : [],
        constants.POSITION : [],
        constants.HEIGHT : [],
        constants.WEIGHT : [],
        constants.AGE : []
    }
    for index, row in reader:
        if index != 0:
            dictionarie[constants.NAME].append(row[0])     
            dictionarie[constants.TEAM].append(row[1])  
            dictionarie[constants.POSITION].append(row[2])     
            dictionarie[constants.HEIGHT].append(row[3])  
            dictionarie[constants.WEIGHT].append(row[4])  
            dictionarie[constants.AGE].append(row[5])  
    return dictionarie

def showLines(reader : enumerate):
    for index, row in reader:
        print(",".join(row) , end=" ")
        print("Row number:" + str(index))

def showParameter (book : dict[str, list], parameter: str):
    for thing in book[parameter]:
        print(thing)

def getFile(path : str, separador: str):
    fileReader = open(path, "r", encoding= "ASCII")
    filecsv = csv.reader(fileReader,  delimiter = separador,)
    return enumerate(filecsv)