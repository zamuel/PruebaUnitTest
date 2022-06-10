def perimetro(elementos):
    s = 0
    for el in elementos:
        s += el
    return s


class Figura:

    def __init__(self, lados):
        self.lados = lados
        self.long = [*range(lados)]
        self.perimetro = perimetro(self.long)

    def lados(self):
        print("I have " + str(self.lados))

    def llenar(self):
        for el in range(self.lados):
            print("Dame la longuitud")
            x = input()
            self.long[el] = int(x)


class Triangulo(Figura):

    def __init__(self):
        super().__init__(3)
