from random import choice
import tkinter as tk
from time import sleep
from os import system

ventana = None
ventanaJuego = None
canvas = None

ventana = tk.Tk()
ventana.title("Asistente de juego del AHORCADO")
ventana.geometry("800x750")
ventana.resizable(False, False)
ventana.configure(bg="#346CA3")
botonesTeclado = {}

opcionCategoria = None
opcionDificultad = None
opcionModalidad = None
opcionCategoria = tk.StringVar(value="")
opcionDificultad = tk.StringVar(value="")
opcionModalidad = tk.StringVar(value="")

titulo = tk.Label(ventana, text="🎮 AHORCADO 🐍", font=("Arial", 32, "bold"), bg="#305E8B", fg="white")
titulo.pack(pady=15)

mainFrame = tk.Frame(ventana, bg="#3C6A99")
mainFrame.pack(fill="both", expand=True, padx=20)

frameCategoria = tk.LabelFrame(mainFrame, text="1️⃣ Selecciona una Categoría", font=("Arial", 12, "bold"), bg="#385E97", fg="white", padx=10, pady=10)
frameCategoria.pack(pady=8, fill="x")
opcionesCat = [("🌎 Países del mundo", "Países del mundo", "#369BB9"), ("🦁 Animales del mundo", "Animales del mundo", "#3A9C37"), ("🎉 ¡FIESTA!", "¡FIESTA!", "purple")] 
for texto, valor, color in opcionesCat:
    btn = tk.Radiobutton(frameCategoria, text=texto, variable=opcionCategoria, value=valor, indicatoron=0, font=("Arial", 10, "bold"), bg=color, fg="white", selectcolor=color, activebackground=color, width=20, height=2)
    btn.pack(side="left", padx=5, expand=True, fill="x")

frameDificultad = tk.LabelFrame(mainFrame, text="2️⃣ Selecciona Dificultad", font=("Arial", 12, "bold"), bg="#385E97", fg="white", padx=10, pady=10)
frameDificultad.pack(pady=8, fill="x")
opcionesDificultad = [("Fácil (6❤️)", "1", "#3A9C37"), ("Medio (5❤️)", "2", "#D4D227"), ("Difícil (4❤️)", "3", "orange"), ("Extremo (3❤️)", "4", "red")]
for texto, valor, color in opcionesDificultad:
    btn = tk.Radiobutton(frameDificultad, text=texto, variable=opcionDificultad, value=valor, indicatoron=0, font=("Arial", 9, "bold"), bg=color, fg="white", selectcolor=color, activebackground=color, width=14)
    btn.pack(side="left", padx=3, expand=True)

frameModalidad = tk.LabelFrame(mainFrame, text="3️⃣ Selecciona Modalidad", font=("Arial", 12, "bold"), bg="#385E97", fg="white", padx=10, pady=10)
frameModalidad.pack(pady=8, fill="x")
opcionesMod = [("RONDAS", "1", "#369BB9"), ("MUERTE SÚBITA", "2", "purple")]
for texto, valor, color in opcionesMod:
    btn = tk.Radiobutton(frameModalidad, text=texto, variable=opcionModalidad, value=valor, indicatoron=0, font=("Arial", 10, "bold"), bg=color, fg="white", selectcolor=color, activebackground=color, width=28)
    btn.pack(side="left", padx=5, expand=True)

def seleccionarDificultad():
    while True:
        try:
            dificultad = int(input("Selecciona el nivel de dificultad:\n 1. Fácil\n 2. Medio\n 3. Díficil\n 4. Extremo\n"))
            if ((dificultad >= 1) and (dificultad <= 4)):
                    if dificultad == 1:
                          contadorVidas = 6
                    elif dificultad == 2:
                          contadorVidas = 5
                    elif dificultad == 3:
                          contadorVidas = 4
                    else:
                          contadorVidas = 3
                    return contadorVidas
            else:
                    print("ERROR: Nivel de dificultad no válido")
        except ValueError:
                print("ERROR: Valor ingresado no válido. Intenta de nuevo")

def seleccionarCategoria():
    while True:
        try:
            categoria = int(input("Selecciona la categoría:\n 1. Países del mundo\n 2. Animales del mundo\n 3. ¡FIESTA!\n"))
            if ((categoria >= 1) and (categoria <= 3)):
                    return categoria
            else:
                    print("ERROR: Categoría no válida")
        except ValueError:
                print("ERROR: Valor ingresado no válido. Intenta de nuevo")   

def seleccionarModalidad():
    while True:
        try:
            modalidad = int(input("Selecciona la categoría:\n 1. Rondas\n 2. Muerte súbita\n"))
            if ((modalidad >= 1) and (modalidad <= 2)):
                    return modalidad
            else:
                    print("ERROR: Modalidad no válida")
        except ValueError:
                print("ERROR: Valor ingresado no válido. Intenta de nuevo")

def elegirPalabra(categoria, paises, fauna, todasPalabras):
    if categoria == 1:
        glosario = paises
    elif categoria == 2:
        glosario = fauna
    else:
        glosario = todasPalabras
    disponibles = list(glosario.keys())
    pista = choice(disponibles)
    listaDePalabras = glosario[pista]
    palabra = choice(listaDePalabras)
    listaDePalabras.remove(palabra)
    if not listaDePalabras:
        del glosario[pista]
    sopa = listaDePalabras
    return pista, palabra, sopa

def inicializarListas(palabra):
    tam = len(palabra)
    palabra = palabra.upper()
    pAdivinada = "_"*tam
    listaPalabra = list(palabra)
    listaAdivinada= list(pAdivinada)
    letrasAdivinadas = set()
    return tam, palabra,listaPalabra, listaAdivinada, letrasAdivinadas

def leerLetra():
    while True:
        letra = input("Ingresa una letra: ").strip().upper()
        if len(letra) != 1:
            print("\nERROR: Has ingresado múltiples caracteres")
        elif not letra.isalpha():
            print("\nERROR: No has ingresado una letra del alfabeto")
        else:
             break 
    letraP = ''
    if letra == 'A':
        letraP = 'Á'
    if letra == 'E':
        letraP = 'É'
    elif letra == 'I':
        letraP = 'Í'
    elif letra == 'O':
        letraP = 'Ó'
    elif letra == 'U':
        letraP = 'Ú'

    if letra == 'Á':
        letraP = 'A'
    if letra == 'É':
        letraP = 'E'
    elif letra == 'Í':
        letraP = 'I'
    elif letra == 'Ó':
        letraP = 'O'
    elif letra == 'Ú':
        letraP = 'U'
    return letra, letraP

def comprobarRepeticion(letra, letraP, letrasAdivinadas):
    if (letra in letrasAdivinadas) or (letraP in letrasAdivinadas):
        print("¡Ya has intentado con esta letra! Prueba con otra")
        return True
    else:
        return False

def buscarLetra(letra, listaPalabra, letraP, listaAdivinada, tam, contVidas):
    if letra in listaPalabra or letraP in listaPalabra:
        print("¡Letra encontrada!\n")
        for i in range(tam):
            if listaPalabra[i] == letra:
                listaAdivinada[i] = letra
            if listaPalabra[i] == letraP:
                listaAdivinada[i] = letraP
    else:
        print("¡Letra no encontrada!\n")
        contVidas -= 1
    return listaAdivinada, contVidas 

def finalizarRonda(listaAdivinada, palabra, contVidas, contadorRondas):
    if "".join(listaAdivinada) == palabra:
        print("¡FELICIDADES! Has adivinado el nombre del país: \n")
        print("".join(listaAdivinada)+"\n")
        contRondas = contadorRondas
        return False, contRondas
    elif contVidas == 0:
        print(f"¡PERDISTE! No has adivinado el nombre del país: {palabra}")
        contRondas = 0
        return False, contRondas
    else:
        return True, contadorRondas   

def jugarOtraRonda():
    while True:
        try:
            opc = int(input("¿Quieres jugar otra ronda?:\n 1: Sí\n 2: No\n"))
            if opc == 1:
                return True
            elif opc == 2:
                print("¡Adiós!")
                return False
            else:
                print("ERROR: Opción no válida. Ingrese 1 o 2")
        except ValueError:
            print("ERROR: Opción no válida. Ingrese 1 o 2")

def modoRondas(contadorVidas, categoria, contadorRondas, paises, fauna, todasPalabras):
    while True:
        contadorRondas = contadorRondas + 1
        print(f"\nRONDA {contadorRondas}")
        contVidas = contadorVidas
        pista, palabra, sopa = elegirPalabra(categoria, paises, fauna, todasPalabras)
        print(f"\n{pista}")
        tam, palabra, listaPalabra, listaAdivinada, letrasAdivinadas = inicializarListas(palabra)
        while contVidas > 0:
            print("".join(listaAdivinada))
            print(f"Vidas restantes: {contVidas}" + "\n")
            while True:
                letra, letraP = leerLetra()
                banderaRepeticion = comprobarRepeticion(letra, letraP, letrasAdivinadas)
                if not banderaRepeticion:
                    letrasAdivinadas.add(letra) 
                    if letraP != '':
                        letrasAdivinadas.add(letraP)
                    break
            listaAdivinada, contVidas = buscarLetra(letra, listaPalabra, letraP, listaAdivinada, tam, contVidas)
            bandera, contadorRondas = finalizarRonda(listaAdivinada, palabra, contVidas, contadorRondas)
            if not bandera:
                break
        otra = jugarOtraRonda()
        sleep(3)
        system("clear")
        if not otra:
            break
        if not sopa:
            print("Ya no quedan más palabras. Fin del juego.")
            break

def modoMuerteSubita(contadorVidas, categoria, contadorRondas, paises, fauna, todasPalabras):
    while True:
        contadorRondas = contadorRondas + 1
        print(f"\nRONDA {contadorRondas}")
        contVidas = contadorVidas
        pista, palabra, sopa = elegirPalabra(categoria, paises, fauna, todasPalabras)
        print(f"\n{pista}")
        tam, palabra, listaPalabra, listaAdivinada, letrasAdivinadas = inicializarListas(palabra)
        while contVidas > 0:
            print("".join(listaAdivinada))
            print(f"Vidas restantes: {contVidas}" + "\n")
            while True:
                letra, letraP = leerLetra()
                banderaRepeticion = comprobarRepeticion(letra, letraP, letrasAdivinadas)
                if not banderaRepeticion:
                    letrasAdivinadas.add(letra)
                    if letraP != '':
                        letrasAdivinadas.add(letraP)
                    break
            listaAdivinada, contVidas = buscarLetra(letra, listaPalabra, letraP, listaAdivinada, tam, contVidas)
            bandera, contadorRondas = finalizarRonda(listaAdivinada, palabra, contVidas, contadorRondas)
            if not bandera:
                break
        sleep(3)
        system("clear")
        if contVidas == 0:
            break
        if not sopa:
            print("Ya no quedan más palabras. Fin del juego.")
            break

def jugarAhorcado():

    contadorRondas = 0
    print("\n---¡Bienvenido al asistente de JUEGO DEL AHORCADO!---")

    america = ["Canadá", "Estados_Unidos", "México", "Guatemala", "Belice", "Honduras", "El_Salvador", "Nicaragua", "Costa_Rica", "Panamá", "Colombia", "Venezuela", "Guyana", "Ecuador", "Perú", "Bolivia", "Brasil", "Paraguay", "Uruguay", "Argentina", "Chile", "Bahamas", "Cuba", "República_Dominicana", "Haití", "Jamaica", "Antigua_y_Barbuda", "Barbados", "Trinidad_y_Tobago", "Dominica", "Granada", "San_Cristóbal_y_Nives", "San_Vicente_y_las_Granadinas", "Santa_Lucía"]
    oceania = ["Australia", "Nueva_Zelanda", "Fiyi", "Islas_Marshall", "Islas_Salomón", "Kiribati", "Estados_Federados_de_Micronesia", "Nauru", "Palaos", "Samoa", "Tonga", "Tuvalu", "Vanuatu"]
    europa = ["España", "Portugal", "Andorra", "Francia", "Mónaco", "Islandia", "Irlanda", "Reino_Unido", "Bélgica", "Países_Bajos", "Luxemburgo", "Suiza", "Italia", "San_Marino", "Ciudad_del_Vaticano", "Malta", "Liechtenstein", "Alemania", "Dinamarca", "Polonia", "Chequia", "Eslovaquia", "Austria", "Hungría", "Eslovenia", "Croacia", "Bosnia_y_Herzegovina", "Montenegro", "Albania", "Serbia", "Macedonia_del_Norte", "Kosovo", "Grecia", "Bulgaria", "Rumania", "Moldavia", "Ucrania", "Bielorrusia", "Estonia", "Letonia", "Lituania", "Noruega", "Suecia", "Finlandia", "Rusia"]
    asia = ["Afganistán", "Arabia_Saudita", "Armenia", "Azerbaiyán", "Bangladesh", "Bahréin", "Myanmar", "Brunéi", "Bután", "Camboya",  "Catar", "China", "Chipre", "Corea_del_Norte", "Corea_del_Sur", "Egipto", "Emiratos_Árabes_Unidos", "Filipinas", "Georgia", "India", "Indonesia", "Irak", "Irán", "Israel", "Japón", "Jordania", "Kazajistán", "Kirguistán", "Kuwait", "Laos", "Líbano", "Maldivas", "Malasia", "Mongolia", "Nepal", "Omán", "Pakistán", "Singapur", "Siria", "Sri Lanka", "Tailandia", "Tayikistán", "Timor_Oriental", "Turkmenistán", "Turquía", "Uzbekistán", "Vietnam", "Yemen"]
    africa = ["Angola", "Argelia", "Benín", "Botsuana", "Burkina_Faso", "Burundi", "Cabo_Verde", "Camerún", "Chad", "República_Centroafricana", "Comoras", "República_del_Congo", "República_Democrática_del_Congo", "Costa_de_Marfil", "Egipto", "Eritrea", "Etiopía", "Gabón", "Gambia", "Ghana", "Guinea", "Guinea_Bisáu", "Guinea_Ecuatorial", "Kenia", "Lesoto", "Liberia", "Libia", "Madagascar", "Malaui", "Malí", "Marruecos", "Mauricio", "Mauritania", "Mozambique", "Namibia", "Níger", "Nigeria", "Ruanda", "Santo_Tomé_y_Príncipe", "Senegal", "Seychells", "Sierra_Leona", "Somalia", "Suazilandia", "Sudáfrica", "Sudán", "Sudán_del_Sur", "Tanzania", "Togo", "Túnez", "Uganda", "Yibuti", "Zambia", "Zimbabue"] 

    mamiferos = ["Perro", "Gato", "León", "Elefante", "Venado", "Caballo", "Ballena", "Canguro", "Jirafa", "Delfin", "Murciélago", "Guepardo", "Leopardo", "Jaguar", "Conejo", "Liebre", "Borrega", "Pantera", "Rinoceronte", "Hipopotamo", "Tigre", "Alpaca", "Zorrillo", "Zorro", "Armadillo", "Ornitorrrinco"]
    reptiles = ["Tortuga", "Cocodrilo", "Serpiente", "Caimán", "Iguana", "Lagartija", "Camaleón", "Lagarto", "Salamandra"]
    aves = ["Paloma", "Loro", "Halcón", "Pato", "Cisne", "Garza", "Gaviota", "Pelicano", "Ganso", "Águila", "Avestruz", "Colibrí", "Quetzal", "Golondrina", "Flamenco", "Búho"]

    paises = {
        "América": america, 
        "Oceanía": oceania, 
        "Europa": europa, 
        "Asia": asia, 
        "África": africa
    }
    
    fauna = {
        "Mamíferos": mamiferos, 
        "Reptiles": reptiles, 
        "Aves": aves
    }

    todasPalabras = {**paises, **fauna} 

    categoria = seleccionarCategoria() 
    modalidad = seleccionarModalidad()  
    contadorVidas = seleccionarDificultad()


    if modalidad == 1:
        modoRondas(contadorVidas, categoria, contadorRondas, paises, fauna, todasPalabras)
    else:
        modoMuerteSubita(contadorVidas, categoria, contadorRondas, paises, fauna, todasPalabras)      

jugarAhorcado()