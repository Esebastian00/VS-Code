class Vehiculo():
    
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        
    def __str__(self):
        return "color {}, {} ruedas, {} puertas".format( self.color, self.ruedas, self.puertas )
        
        
class Coche(Vehiculo):
    
    def __init__(self, velocidad, cilindrada):
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return Coche.__str__(self) + ", {} velocidad, {}cilindrados".format(self.velocidad, self.cilindrada)

mi_coche = Coche('gris', '4', '2', '300', '1100')
print(mi_coche)
