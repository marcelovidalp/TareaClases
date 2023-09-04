class Playlist:
    def __init__(self, cancion, Estado = "Reproduciendo"):
        self.cancion = cancion
        self.Estado = Estado
        self.lista = []
        

    def anadirCancion(self):
        for canciones in self.lista:
            if self.cancion not in canciones:
                self.lista.append(self.cancion)
                print(f"La cancion ha sido exitosamente añadida a la playlist.")

    def eliminarCancion(self):
        for canciones in self.lista: 
            if self.cancion == canciones:
                self.lista.remove(self.cancion)
                print(f"\nLa cancion {self.cancion} ha sido eliminada de la playlist.")
        pass

    def mostrarCanciones(self):
        for j, cancion in enumerate(self.lista):
            print(f"{j+1}.- {cancion}")

    def reproducirCancion(self):
        
        pass

    def selecCancion(self):

        pass

    def pausarCancion(self):
        pass

    def detenerCancion(self):
        pass

    def nextCancion(self):
        pass

    def backCancion(self):
        pass

    def rep_Cancion_Aleatoria(self):
        pass

    def verEstado_playlist(self):
        pass

    def verCancion_reproducida(self):
        pass
        

