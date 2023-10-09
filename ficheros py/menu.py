from ex1 import main1
from ex2 import main2
from ex3 import main3
import os
def main():
    print("Benvingut al menu de l'exercici, aixó no era necessari pero considero que així es mes visual"
          + "\n Abans de començar explico varies coses: per els exercicis pots escollir d'on agafas el fitxer, \n "
          + "pero el fitxer del exercici 1 es crea en el directori d'on s'hagi executat el programa. Quan seleccionis el exercici haurás de escollir el fitxer.")
    selection = 0
    while selection != 4:
        try:
            selection = int(input("Quin exercici vols veure?\n"
                            + "\t1. Exercici 1\n"
                            + "\t2. Exercici 2\n"
                            + "\t3. Exercici 3\n"
                            + "\t4. EXIT\n"))
            while selection not in range(1, 5):
                selection = int(input("Quin exercici vols veure?\n"
                            + "\t1. Exercici 1\n"
                            + "\t2. Exercici 2\n"
                            + "\t3. Exercici 3\n"
                            + "\t4. EXIT\n"))
            if selection == 4:
                break
            if os.name == 'posix': 
                 os.system('clear')
            elif os.name == 'nt':
                os.system('cls')
            match selection:
                case 1:
                    main1()
                case 2:
                    main2()
                case 3:
                    main3()
        except:
            print("Has d'introduir un número")
main()