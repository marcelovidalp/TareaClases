import random

class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []
        self.Estado = "Detenido"
        self.indiceActual = None
        

    def anadirCancion(self, cancion):
        self.canciones.append(cancion)

    def eliminarCancion(self, cancion):
        if cancion in self.canciones:
            self.canciones.remove(cancion)

    def mostrarCanciones(self):
        print(f"Canciones en {self.canciones}")
        for i, cancion in enumerate(self.canciones):
            print(f"{i}.- {cancion}")

    def reproducirCancion(self):
        if not self.canciones:
            print("No hay canciones en la playlist.")
            return
        
        if self.estado == "Detenido":
            self.estado == "Reproduciendo"
            self.indiceActual == 0
            print(f"Reproduciendo {self.canciones[0]}.")
        elif self.estado == "Pausa":
            self.estado == "Reproduciendo"
            print(f"Reanudando reproduccion de la cancion {self.canciones[self.indiceActual]}.")
        else:
            print("Ya se esta reproduciendo una cancion.")

    def selecCancion(self, indice):
        if 0 <= indice < len(self.canciones):
            self.indiceActual = indice
            if self.Estado == "Detenido":
                self.Estado = "Reproduciendo"
            print(f"Reproduciendo: {self.canciones[indice]}.")
        else:
            print("Indice no valido.")
    
    def pausarCancion(self):
        if self.Estado == "Reproduciendo":
            self.Estado = "Pausa"
            print(f"SE PAUSO LA CANCION {self.canciones[self.indiceActual]}")

    def detenerCancion(self):
        if self.Estado == "Reproduciendo":
            self.Estado = "Detenido"
            self.indiceActual = None
            print("Se detuvo la musica.")
        else:
            print("No se esta reproduciendo ninguna cancion.")

    def nextCancion(self):
        if not self.canciones:
            print("No hay canciones en la playlist.")
            return
        if self.indiceActual is not None:
            if 0 <= self.indiceActual < len(self.canciones) - 1:
                self.indiceActual += 1
                print(f"Reproduciendo la siguiente cancion {self.indiceActual}")
            else: 
                print("No hay mas canciones en la playlist.")
        else: 
            print("El reproductor esta detenido.")

    def backCancion(self):
        if not self.canciones:
            print("No hay canciones en la playlist.")
            return
        if self.indiceActual is not None:
            if self.indiceActual > 0:
                self.indiceActual -= 1
                print(f"Se esta reproduciendo la cancion anterior: {self.canciones[self.indiceActual]}")
            else:
                print("No hay canciones en la playlist.")
        else:
            print("El reproductor esta detenido.")

    def rep_Cancion_Aleatoria(self):
        if not self.canciones:
            print("No hay canciones en las playlist.")
            return
        if self.Estado == "Reproducindo":
            print(f"Ya se esta reproduciendo una cancion: {self.canciones}")
        else:
            cancionAleatoria = random.choice(self.canciones)
            self.indiceActual = self.canciones.index(cancionAleatoria)
            self.Estado = "Reproduciendo"
            print(f"Reproduciendo aleatoria: {cancionAleatoria}")

    def verEstado(self):
        if self.indiceActual is not None:
            print(f"Estado: {self.Estado}, cancion actual: {self.canciones[self.indiceActual]}")
        else:
            print(f"Estado. {self.Estado}")        

    def verCancion_reproducida(self):
        if self.indiceActual is not None:
            print(f"Cancion actual {self.canciones[self.indiceActual]}")
        else:
            print("No hay cancion reproduciendose.")

nombrePlaylist = input("Pongale nombre a su playlist: ")
miPlaylist = Playlist(nombrePlaylist)

while True:
    print("------------Bienvenido a tu playlist-----------")
    print("1.- Añadir cancion.")
    print("2.- Eliminar cancion.")
    print("3.- Mostrar canciones.")
    print("4.- Reproducir cancion.")
    print("5.- Seleccionar cancion.")
    print("6.- Pausar cancion.")
    print("7.- Detener cancion.")
    print("8.- Siguiente cancion.")
    print("9.- Cancion anterior.")
    print("10.- Reproducir una cancion aleatoria.")
    print("11.- Ver estado.")
    print("12.- Ver cancion reproducida.")
    print("13.- Salir.")
    opcion = int(input("\nSeleccione una opción (numero): "))

    if opcion == 1:
        cancion = input("Ingrese el nombre de la cancion: ")
        Playlist.anadirCancion()
        print(f"La cancion {cancion} ha sido añadida: ")
    elif opcion == 2:
        Playlist.mostrarCanciones()
        cancion = input("Ingrese el nombre de la cancion a eliminar")
        Playlist.eliminarCancion()
        print(f"La cancion {cancion} ha sido eliminada.")
    elif opcion == 3:
        Playlist.mostrarCanciones()
    elif opcion == 4:
        Playlist.reproducirCancion()
    elif opcion == 5:
        indice = int(input("Ingrese el indice de la cancion a seleccionar: "))
        Playlist.selecCancion(indice - 1)
    elif opcion == 6:
        Playlist.pausarCancion()
    elif opcion == 7:
        Playlist.detenerCancion()
    elif opcion == 8:
        Playlist.nextCancion()
    elif opcion == 9:
        Playlist.backCancion()
    elif opcion == 10:
        Playlist.rep_Cancion_Aleatoria()
    elif opcion == 11:
        Playlist.verEstado()
    elif opcion == 12:
        Playlist.verCancion_reproducida()
    elif opcion == 13:
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no calida")


        
