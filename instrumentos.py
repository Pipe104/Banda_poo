from random import shuffle

class Instrumento:

    def afinar(self):
        pass

    def tocar(self):
        pass

    def mostrar(self):
        return "Instrumento: " + (str(type(self)).split(".")[-1][:-2])


class Guitarra(Instrumento):

    def afinar(self):
        return "Afinando guitarra"

    def tocar(self):
        return "Tocando guitarra"

class Tiple(Instrumento):

    def afinar(self):
        return "Afinando Tiple"

    def tocar(self):
        return "Tocando Tiple"

class Acordeon(Instrumento):

    def afinar(self):
        return "Afinando acordeon"

    def tocar(self):
        return "Tocando acordeon"
    
class Saxo(Instrumento):

    def afinar(self):
        return "Afinando saxo"

    def tocar(self):
        return "Tocando saxo"
    
class Piano(Instrumento):

    def afinar(self):
        return "Afinando piano"

    def tocar(self):
        return "Tocando piano"
    
class Arpa(Instrumento):

    def afinar(self):
        return "Afinando Arpa"

    def tocar(self):
        return "Tocando Arpa"
    
class Flauta(Instrumento):

    def afinar(self):
        return "Afinando flauta"

    def tocar(self):
        return "Tocando flauta"
    
class Tambor(Instrumento):

    def afinar(self):
        return "Afinando tambor"

    def tocar(self):
        return "Tocando tambor"
    
class Maracas(Instrumento):

    def afinar(self):
        return "Afinando maracas"

    def tocar(self):
        return "Tocando maracas"
    
class Violin(Instrumento):

    def afinar(self):
        return "Afinando violin"

    def tocar(self):
        return "Tocando violin"
