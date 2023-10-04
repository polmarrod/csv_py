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

def showLines(reader : enumerate):
    for index, row in reader:
        print(",".join(row) , end=" ")
        print("Row number:" + str(index))
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
def changePosition(book : dict[str, list]):
    for index, position in enumerate(book[constants.POSITION]):        
        book[constants.POSITION][index] = constants.NEWPOSITIONS[position]
    return book      
def changeHeightOrWeight(book : dict[str, list], parameter : str):
    value = 0.0
    if parameter == constants.HEIGHT:
        value = constants.FOOT
    elif parameter == constants.WEIGHT : 
        value = constants.POUND
    else : 
        return
    for index, thing in enumerate(book[parameter]):
        book[parameter][index] = round( round(float(thing), 2) * value, 2)
        index += 1
    return book

def showParameter (book : dict[str, list], parameter: str):
    for thing in book[parameter]:
        print(thing)

def changeAge(book : dict[str, list] , decimals : int):
    for index, age in enumerate(book[constants.AGE]):
        book[constants.AGE][index] = int(round(float(age), decimals))
    return book

def newCSVFile(book : dict[str, list]):    
    with open(constants.PATHNEWFITXERO, mode= "w") as file:
        writer = csv.DictWriter(file, delimiter=constants.SEPARADORNEW, fieldnames= constants.NEWHEADERS)
        writer.writeheader()
        for index in range(len(book[constants.NAME])):
            row = {
                constants.NEWHEADERS[0] : book[constants.NAME][index], 
                constants.NEWHEADERS[1] : book[constants.TEAM][index], 
                constants.NEWHEADERS[2] : book[constants.POSITION][index], 
                constants.NEWHEADERS[3] : book[constants.HEIGHT][index], 
                constants.NEWHEADERS[4] : book[constants.WEIGHT][index], 
                constants.NEWHEADERS[5] : book[constants.AGE][index]
                   }
            writer.writerow(row)
def main ():
    fileReader = open(constants.PATHFITXERO, "r")
    filecsv = csv.reader(fileReader,  delimiter = constants.SEPARADOROLD)
    
    book = toDictionarie(enumerate(filecsv))
    book = changePosition(book)
    book = changeHeightOrWeight(book, constants.HEIGHT)
    book = changeHeightOrWeight(book, constants.WEIGHT)
    book = changeAge(book, 0)
    "showParameter(book, constants.HEIGHT)"
    newCSVFile(book)
main()