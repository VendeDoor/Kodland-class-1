import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Porfavor, ingrese la longitud de su contrasena"))
contrasena = ""

for i in range(longitud):
    caracter = random.choice(caracteres)
    contrasena += caracter

print("contrasena generada:", contrasena)