class Cuenta:
  def __init__(self, nombre, apellido, cantidad=0):
   self.nombre=nombre
   self.apellido=apellido
   self.cantidad=cantidad

  def mostrar(self):
    print("---DATOS DE LA CUENTA---")
    print("Nombre del titular:",self.nombre, self.apellido, "tiene $", self.cantidad,"en su cuenta")

  def ingresar(self, cantidad):
      self.cantidad = self.cantidad + cantidad

  def retirar(self, cantidad):
   if (cantidad > 0):
      self.cantidad = self.cantidad - cantidad
      print("Usted retiró $",cantidad, "de su cuenta. Su saldo es de $", self.cantidad, "pesos")



cuenta=Cuenta("Joaquin", "Torres", 100)
cuenta.ingresar(200)
cuenta.mostrar()
cuenta.retirar(450)
