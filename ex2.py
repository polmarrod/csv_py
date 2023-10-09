from globales import constants, getFile, toDictionarie
#region funciones de calculos
def searchForParameter(book: dict[str: list], parameter : str, searcher : bool):
    higher = 0
    index = 0
    for i, number in enumerate(book[parameter]):
        if searcher :
            if float(number) > higher : 
                higher = float(number)
                index = i
        else:
            if float(number) < higher : 
                higher = float(number)
                index = i
    return index
def listForTeams(book: dict[str: list]):
    dictTeams : dict[str, dict[str, float]] = {}
    for i, item in enumerate(book[constants.TEAM]):
        if not item in dictTeams:
            dictTeams[item] = {
                constants.HEIGHT : 0.0,
                constants.WEIGHT : 0.0,
                "people" : 0
            }
        dictTeams[item][constants.HEIGHT] += float(book[constants.HEIGHT][i])
        dictTeams[item][constants.WEIGHT] += float(book[constants.WEIGHT][i])
        dictTeams[item]["people"] += 1
    return dictTeams
def calculateRange(parameter : str, list : dict[str, int]):
    return str(round(list[parameter] / list["people"], 2))
def countForPosition(book: dict[str, list], parameter : str):
    dictParameter : dict[str, int] = {}
    for item in book[parameter]:
        if not item in dictParameter:
            dictParameter[item] = 1
        else:
            dictParameter[item] += 1
    return dictParameter
#endregion
#region Funciones visuales
def ShowPlayerWeight(book: dict[str: list]):
    index = searchForParameter(book, constants.WEIGHT, True)
    print("El jugador amb el pes mes alt és: " + book[constants.NAME][index] + ", el seu pes és de " + book[constants.WEIGHT][index] +" kg" )
def ShowPlayerHeight(book: dict[str: list]):
    index = searchForParameter(book, constants.HEIGHT, False)
    print("El jugador amb la altura mes baixa és: " + book[constants.NAME][index] + ", la seva altura és de " + book[constants.HEIGHT][index] +" cm" )
def ShowRangeOfTeams(book : dict[str : list]):
    dictTeams = listForTeams(book)
    for team in dictTeams:
        print("Del equip " + team + " la seva mitjana d'altura és: " + calculateRange(constants.HEIGHT, dictTeams[team]) + " cm, i la mitjana de pes és de: " + calculateRange(constants.WEIGHT, dictTeams[team]) + " kg.")
def ShowPlayersByParameter (book : dict[str, list], parameter :str):
    dictParameter = countForPosition(book, parameter)
    for item in dictParameter:
        if (parameter == constants.POSITION):
            print("De la possició: " + item+ " hi han " + str(dictParameter[item]) + " jugadors.")
        else:
            print("De la edat de: " + item+ " hi han " + str(dictParameter[item]) + " jugadors.")

#endregion
def main2 ():
    file = getFile(constants.SEPARADORNEW)
    book = toDictionarie(file)
    ShowPlayerWeight(book)
    ShowPlayerHeight(book)
    ShowRangeOfTeams(book)
    ShowPlayersByParameter(book, constants.POSITION)
    ShowPlayersByParameter(book, constants.AGE)
main2()