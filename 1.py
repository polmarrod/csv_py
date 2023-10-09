import csv
from globales import constants, toDictionarie, getFile

#region FunctionsUpdateData
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
def changeAge(book : dict[str, list] , decimals : int):
    for index, age in enumerate(book[constants.AGE]):
        book[constants.AGE][index] = int(round(float(age), decimals))
    return book
#endregion
def newCSVFile(book : dict[str, list]):    
    with open(constants.PATHNEWFITXERO, mode= "w", encoding="ASCII",newline='') as file:
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
            if any(row.values()):
                writer.writerow(row)
def main ():
    file = getFile(constants.PATHFITXERO, constants.SEPARADOROLD)
    book = toDictionarie(file)
    book = changePosition(book)
    book = changeHeightOrWeight(book, constants.HEIGHT)
    book = changeHeightOrWeight(book, constants.WEIGHT)
    book = changeAge(book, 0)
    newCSVFile(book)
main()