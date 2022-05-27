class Mamifero:
  def __init__(self, cantMamas, esperanzaDeVida):
    self.cantMamas = cantMamas
    self.__esperanzaDeVida = esperanzaDeVida

  def mamar(self):
    print("¡Aún estoy chiquito! Debo seguir comiendo")

  def nacer():
    print("¡Estoy naciendo!")

  def __str__(self):
    return f"Mi esperanza de vida es de {self.__esperanzaDeVida} años y tengo {self.cantMamas} mamas" 

  def get_esperanzaDeVida(self):
    return self.__esperanzaDeVida

  def set_esperanzaDeVida(self, esperanzaDeVida):
    self.__esperanzaDeVida = esperanzaDeVida    

class AnimalMarino:
  def __init__(self, tieneBranqueas, especie):
    self.__tieneBranqueas = tieneBranqueas
    self.__especie = especie

  def nadar(self):
    print("Estoy aprendiendo a nadar")

  def __str__(self):
    return f"Nosotras las {self.__especie} somos animales marinos y tenemos {self.__tieneBranqueas} no branqueas"

  def get_tieneBranqueas(self):
    return self.__tieneBranqueas

  def set_tieneBranqueas(self, tieneBranqueas):
    self.__tieneBranqueas = tieneBranqueas

  def get_especie(self):
    return self.__especie

  def set_especie(self, especie):
    self.__especie = especie 

class Cetaceo(Mamifero, AnimalMarino):
  def __init__(self, cantMamas, esperanzaDeVida, tieneBranqueas, especie, notas, viveEn, peso):

    Mamifero.__init__(self, cantMamas, esperanzaDeVida )
    AnimalMarino.__init__(self, tieneBranqueas, especie)
       
    self.__notas = notas
    self.__viveEn = viveEn
    self.__peso = peso

  def __str__(self):
    return  Mamifero.__str__(self) + "\n" + AnimalMarino.__str__(self) + f"\nMido más de {self.__notas} metros, vivo en el {self.__viveEn}, y peso hasta {self.__peso} toneladas xd" 

cetaceo = Cetaceo(2, 80, "pulmones", "ballenas", 29, "oceano", 180)  
print(f"{cetaceo}")
