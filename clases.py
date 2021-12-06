import os
import string
import time
import sys

possible_answer = ['si', 'yes', 'y', 's', 'n', 'no']
affirmative_answer = ['si', 's', 'yes', 'y']
possible_choices = ['1', '2', '3', '4', '5', 'A', 'B', 'C', 'D']

def choices_in_main ():
    choice = str(input("""\n\n\nCon qué deseas interactuar? O a donde quieres ir? > """)).capitalize()
    while choice not in possible_choices:
        choice = str(input("""\n\n\nPor favor, ingrese un valor válido > """)).capitalize()
    return choice

def safebox_game (name):
    tries = 10
    safebox_game_answer= str(input("""\n\n\nQueres intentar abrir la caja fuerte? > """)).lower()
    print(safebox_game_answer)
    while safebox_game_answer not in possible_answer:
        safebox_game_answer = str(input("""\n\n\nPor favor, ingrese un valor válido > """)).lower()
    if safebox_game_answer in affirmative_answer:
        for value in range(tries):
            print("Tenes {} intentos".format(tries))
            tries-=1
            final_code = str(input("Ingrese el código de 4 números > "))
            print("""\n\n\nSerá el valor correcto???""")
            time.sleep(5)
            if final_code == '1503':
                print("""\n\n\nPerfecto! Se abrió la caja y adentro hay una llave!
                \n\n\nEsa llave la usamos para abrir la puerta y finalmente logramos escapar!""")
                print("\n\n\nGracias por salvarme la vida {}".format(name.capitalize()))
                sys.exit()
            else:
                print("""\n\n\nUna chicharra roja nos avisa que el código es incorrecto!""")
        Death.bomb_death(name)
        StartGame.retry_game(name)


class StartGame():

    def __init__(self):
        os.system("clear")
        name_player= input("Cual es tu nombre? > ")
        answer_player= input("Bienvenide {}, no encuentro las llaves, podrías ayudarme a encontrarlas? > \n\n\n".format(name_player.capitalize()))
        answer_player= answer_player.lower()
        while answer_player not in possible_answer:
            answer_player= input("Por favor, ingrese una respuesta correcta > \n")
            answer_player= answer_player.lower()
            print(answer_player)
        if answer_player in affirmative_answer:
            os.system("clear")
            print("Perfecto!, empecemos entonces!\n\n\n")
            Scenario.living_room(name_player)
        else:
            os.system("clear")
            print("Bueno, entonces me voy a dormir, creo que no hay más comida\n\n\n")
            Death.starvation_death(name_player)
            StartGame.retry_game(name_player)

    def with_name(name):
        Scenario.living_room(name)

    def retry_game(name):
        answer_player= input("Quieres jugar nuevamente {}?\n".format(name.capitalize()))
        answer_player.lower()
        while answer_player not in possible_answer:
            answer_player= input("Por favor, ingrese una respuesta correcta > \n")
            answer_player.lower()
        if answer_player in affirmative_answer:
            StartGame.with_name(name)
        else:
            print("\n\n\n\n\nGracias por jugar!\n\n\n\n\n")


class Death():

    @staticmethod
    def starvation_death(name):
        print("""\n\n\n\n{}, no lograste encontrar la llave, me fui a dormir, y los vecinos nos encontraron
a las 5 semanas por el olor nauseabundo de nuestros cuerpos putrefactos\n\n\n\nFIN\n\n\n\n""".format(name.capitalize()))

    @staticmethod
    def heat_death(name):
        print("""\n\n\n\nNos acercamos un poco a la estufa porque hace un frío de cagarse, pero olvidaste que tenías puesto
el polar que prende más rápido que el Mudomental, perdón {}, pero moris calcinade. Recogo lo poco que queda de tu 
cuerpo, lo levanto con la escoba y lo llevo al incinerador\n\n\n\nFIN\n\n\n\n""".format(
            name.capitalize()))

    @staticmethod
    def slip_death(name):
        print("""\n\n\n\nTe advierto que no te acerques a la ducha porque recién me acabo de bañar, no me haces caso y un 
resbalón hace que tu cráneo se fracture y mueras instantaneamente. Perdón {}, pero tuve que llamar a las autoridades para 
tratar de no pasar el resto de mis días en prisión.

Terminan confirmando que fue simplemente una muerte por accidente hogareño.

**FUN FACT: Sabías que mueren más personas por año por resbalones en la bañera que por ataques terroristas?\n\n\n\nFIN\n\n\n\n""".format(
            name.capitalize()))

    @staticmethod
    def windows_death(name):
        print("""\n\n\n\nTe acercas a la ventana y a mi grito de: "{}, cuidado que la persiana está floja!!!", caes al vacío 
produciendo un estruendo en el pulmón del edificio que nadie le da demasiada relevancia\n\n\n\nFIN\n\n\n\n""".format(
            name.capitalize()))

    def bomb_death(name):
        print("""\n\n\n\nInexplicablemente, nadie nos avisa que cuando la caja fuerte llegaba a 0, explotaba todo el departamento
dejando una estela de muerte, caos y destrucción a nuestro alrededor. Perdón {}, mala mía.\n\n\n\n""".format(
            name.capitalize()))


class Scenario():

    @staticmethod
    def kitchen(name):

        kitchen_objects= ['Piedras', 'Bajomesada', 'Calefon', 'Heladera']
        scenarios = ['Living', 'Cocina', 'Pieza', 'Baño']

        print("""\n\n\nBueno {}, ahora estamos en la cocina y tenemos los siguientes objetos para interactuar:""".format(name.capitalize()))
        for object in range(len(kitchen_objects)):
            print(object+1, kitchen_objects[object])
        print("""\n\nSi queres, también podemos ir al:""")
        for scenario in range(len(scenarios)):
            print(string.ascii_lowercase[scenario].capitalize(), scenarios[scenario])
        choice = choices_in_main()
        while choice in possible_choices:
            if choice == '1':
                print("""\n\nPiedras de gato, no tiene mucha ciencia, pero si exploramos un poco, vemos que hay un código que dice
1503, qué será?""")
            elif choice == '2':
                print("""\n\nTuppers, té, ollas y demás yerbas... y yerba...""")
            elif choice == '3':
                print("""\n\nPrendido en nivel 5, máximo permitido""")
            elif choice == '4':
                print("""\n\nNo muchas cosas, la macrisis nos afecta a todos""")
            elif choice == 'A':
                print("""\n\nBuenisimo, nos vamos al living""")
                time.sleep(3)
                os.system("clear")
                Scenario.living_room(name)
            elif choice == 'B':
                print("""\n\nYa estamos en la cocina!""")
            elif choice == 'C':
                print("""\n\nBuenisimo, nos vamos a la pieza""")
                time.sleep(3)
                os.system("clear")
                Scenario.bedroom(name)
            elif choice == 'D':
                print("""\n\nBuenisimo, nos vamos al baño!""")
                time.sleep(3)
                os.system("clear")
                Scenario.bathroom(name)
            choice = choices_in_main()

    @staticmethod
    def bedroom(name):

        bedroom_objects= ['Cama', 'Televisor', 'Armario', 'Ventana', 'Caja de Seguridad']
        scenarios = ['Living', 'Cocina', 'Pieza', 'Baño']

        print("""\n\n\nBueno {}, ahora estamos en la pieza y tenemos los siguientes objetos para interactuar:""".format(name.capitalize()))
        for object in range(len(bedroom_objects)):
            print(object+1, bedroom_objects[object])
        print("""\n\nSi queres, también podemos ir al:""")
        for scenario in range(len(scenarios)):
            print(string.ascii_lowercase[scenario].capitalize(), scenarios[scenario])
        choice = choices_in_main()
        while choice in possible_choices:
            if choice == '1':
                print("""\n\nOiga!""")
            elif choice == '2':
                print("""\n\nCupcake Wars en la tele, gran programa""")
            elif choice == '3':
                print("""\n\nLa macrisis nos pegó mal, poca ropa, vieja y sucia""")
            elif choice == '4':
                Death.windows_death(name)
                StartGame.retry_game(name)
            elif choice == '5':
                print("""\n\nUna caja de seguridad que pide un código de 4 dígitos... que mierda es esto?""")
                safebox_game(name)
            elif choice == 'A':
                print("""\n\nBuenisimo, nos vamos al living""")
                time.sleep(3)
                os.system("clear")
                Scenario.living_room(name)
            elif choice == 'B':
                print("""\n\nBuenisimo, nos vamos a la cocina""")
                time.sleep(3)
                os.system("clear")
                Scenario.kitchen(name)
            elif choice == 'C':
                print("""\n\nYa estamos en la pieza!""")
            elif choice == 'D':
                print("""\n\nBuenisimo, nos vamos al baño!""")
                time.sleep(3)
                os.system("clear")
                Scenario.bathroom(name)
            choice = choices_in_main()

    @staticmethod
    def bathroom(name):

        bathroom_objects= ['Lavabo', 'Inodoro', 'Ducha', 'Toalla']
        scenarios = ['Living', 'Cocina', 'Pieza', 'Baño']

        print("""\n\n\nBueno {}, ahora estamos en el baño y tenemos los siguientes objetos para interactuar:""".format(name.capitalize()))
        for object in range(len(bathroom_objects)):
            print(object+1, bathroom_objects[object])
        print("""\n\nSi queres, también podemos ir al:""")
        for scenario in range(len(scenarios)):
            print(string.ascii_lowercase[scenario].capitalize(), scenarios[scenario])
        choice = choices_in_main()
        while choice in possible_choices:
            if choice == '1':
                print("""\n\nAmbas canillas funcionan bien, bien por mi que cambié los cueritos""")
            elif choice == '2':
                print("""\n\nRestos de una batalla""")
            elif choice == '3':
                Death.slip_death(name)
                StartGame.retry_game(name)
            elif choice == '4':
                print("""\n\nHay que cambiarlas, ya están sucias""")
            elif choice == 'A':
                print("""\n\nBuenisimo, nos vamos al living""")
                time.sleep(3)
                os.system("clear")
                Scenario.living_room(name)
            elif choice == 'B':
                print("""\n\nBuenisimo, nos vamos a la cocina""")
                time.sleep(3)
                os.system("clear")
                Scenario.kitchen(name)
            elif choice == 'C':
                print("""\n\nBuenisimo, nos vamos a la pieza""")
                time.sleep(3)
                os.system("clear")
                Scenario.bedroom(name)
            elif choice == 'D':
                print("""\n\nYa estamos en el baño""")
            choice = choices_in_main()

    @staticmethod
    def living_room(name):

        living_objects= ['Futon', 'Biblioteca', 'Televisor', 'Estufa', 'Documentos']
        scenarios = ['Living', 'Cocina', 'Pieza', 'Baño']

        print("""\n\n\nBueno {}, ahora estamos en el living y tenemos los siguientes objetos para interactuar:""".format(name.capitalize()))
        for object in range(len(living_objects)):
            print(object+1, living_objects[object])
        print("\n")
        for scenario in range(len(scenarios)):
            print(string.ascii_lowercase[scenario].capitalize(), scenarios[scenario])
        choice = choices_in_main()
        print(choice)
        while choice in possible_choices:
            if choice == '1':
                print("""\n\nEn el futón solo veo los almohadones, pelos de gatos y los controles remotos, nada más""")
            elif choice == '2':
                print("""\n\nEn la biblioteca solo veo libros de Poker y de Psicología, nada relevante""")
            elif choice == '3':
                print("""\n\nEn la tele está puesto C5N, la jefa vuelve a fin de año!""")
            elif choice == '4':
                Death.heat_death(name)
                StartGame.retry_game(name)
            elif choice == '5':
                print("""\n\nEzequiel Gresia, DNI 33111140""")
            elif choice == 'A':
                print("""\n\nYa estamos en el living""")
            elif choice == 'B':
                print("""\n\nBuenisimo, nos vamos a la cocina""")
                time.sleep(3)
                os.system("clear")
                Scenario.kitchen(name)
            elif choice == 'C':
                print("""\n\nBuenisimo, nos vamos a la pieza""")
                time.sleep(3)
                os.system("clear")
                Scenario.bedroom(name)
            elif choice == 'D':
                print("""\n\nBuenisimo, nos vamos al baño""")
                time.sleep(3)
                os.system("clear")
                Scenario.bathroom(name)
            choice = choices_in_main()







