# Variables
x = 0
nombreMessi = "MESSI"
nombreCristiano = "CRISTIANO"
z = float(3)
y= int (3.2)
k= int("1")

# Condiciones
if x == 10:
    print(nombreMessi)
elif x == 7:
    print(nombreCristiano)
elif x == 0:
    print("HUEVOOOOS")
else:
    print("No existe")

# Strings
nombre = "Mario"
print(nombre[0])
print(nombre[1])
print(nombre[2])
print(nombre[3])
print(nombre[4])

# CICLOS
for letra in nombre:
    print(letra)

print((len(nombre)))

texto = "Alla en la fuente habia un chorrito"

print("chorrito" in texto)

if "chorrito" in texto:
    print("CHORRITO")

# Slicing String
b= "Hola Mundo"
c= b[5:10]
print(c)

# Slice desde el inicio
print(b[:5])

# Slice desde una posicion hasta el final
print(b[5:])

# Slice con posiciones negativas
print(b[-5:-2])

# Boleanos

# Mayor que
print(10 > 9)

# Igual que
print(10==9)

# Menor que
print(10<9)

# Variables Boleanas
enStock = True
isTiendaAbierta = True

if enStock and isTiendaAbierta:
    print("VENDER PRODUCTOS")

tieneEfectivo= False
tieneTarjeta = True
if tieneTarjeta or tieneEfectivo:
    print("PAGO ACEPTADO")

regresasteConEx = False
if not regresasteConEx:
    print("Mentiroso")

tienesNovie = True
if not tienesNovie:
    print("false")

paseLenguajes = True
if not paseLenguajes:
    print("REPROBASTE")

isUploaded = True
if not isUploaded:
    print("Reintentar")
isUploaded = True
if not isUploaded:
    print("Reintentar")

isUploaded = True
if not isUploaded:
    print("Reintentar")

# Operadores aritmeticos
print("\n" + "Operadores Aritmeticos")
h = 5
i = 6

# SUMA
print("\n" + "SUMA")
print(h + i)

# RESTA
print("\n" + "RESTA")
print(h - i)

# MULTIPLICACION
print("\n" + "MULTIPLICACION")
print(h * i)

# DIVISION
print("\n" + "DIVISION")
print(h / i)

# MODULO
print("\n" + "MODULO")
print(h % i)

# EXPONENTES
print("\n" + "EXPONENTES")
print(2**2)
print(h**2)
print(h**i)

# Floor division
print("\n" + "floor division")
print(4 // 2)
print(h // i)

# Operadores de asignacion
print("\n" + "Operadores de asignacion")
x = 30
x += 32
x -= 2
x *= 2
x /= 2
print(x)

# Operadores Logicos de Comparacion
print("\n" + "Operadores Logicos de Comparacion")
a = 3
b = 2

# IGUAL
print("\n" + "IGUAL")
print(a == b)
#DIFERENTE
print("\n" + "DIFERENTE")
print(a !=b)

# MAYOR
print("\n" + "MAYOR")
print(a > b)

# MENOR
print("\n" + "MENOR")
print(a < b)

# MAYOR IGUAL
print("\n" + "MAYOR IGUAL")
print(a >= b)
#MENOR IGUAL
print("\n" + "MENOR IGUAL")
print(a <= b)

# Operadores logicos
print("\n" + "Operadores logicos")

promedio = 0
asistencia = True
aprobado = (promedio > 70) and asistencia
#and, or, not
print(aprobado)

# OPERADORES DE IDENTIDAD
print("\n" + "OPERADORES DE IDENTIDAD")
u = "HOLA"
q = "HOLA "
#print(u is q.replace(__old=" ", __new="") )
#print(u is not q)

# Operadores de pertenencia
#print("A" in "HOLA")
#print("A" not in "HOLA")

# List, Tuple, Set, Dictionary
print("\n" + "List, Tuple, Set, Dictionary")

# Lista
print("\n" + "Lista")
lista1 =["🐥", "🐵", "🐷"]
lista1.insert(3, "🐶")
lista1[1] = "🦁"
print(lista1)

# Tupla
print("\n" + "Tupla")
tupla1 = ("🐥", "🐵", "🐷")
print(tupla1)

# Set
print("\n" + "Set")
set1 = {"🐥", "🐵", "🐷"}
set1.add("🐨")
set1.add("🐙")
set1.add("🐷")
print(set1)

# Diccionario
print("\n" + "Diccionario")
diccionario1 = {
    "pollo": "🐥",
    "monito": "🐵",
    "cerdito": "🐷"
}
diccionario1["koala"]= "🐨"
diccionario1["tigre"]= "🐯"
print(diccionario1["monito"])
print(diccionario1)

# CONDICIONES
print("\n" + "CONDICIONES")
print("\n" + "Ejemplo 1")
a = 208
b = 33

if b > a:
    print("b es mayo que a")
elif a == b:
    print("a y b son impares")
else:
    print("a es mayor que b")

# CICLO WHILE
print("\n" + "CICLO WHILE")

quiereVolver = True
vecesRegresaron = 0
while vecesRegresaron < 3:
    vecesRegresaron += 1
    print("Han vuelto " + str(vecesRegresaron) + " " + "Veces")

print("\n" + "BREAK")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
else:
    print("ERROR")

# Continue
print("\n" + "CONTINUE")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# Ciclo for - for each
print("\n" + "Ciclo for - for each")
frutas = ["🍎", "🍌", "🥭"]

# for - Por cada
buscar = False
if buscar:
    for fruta in frutas:
        if fruta == "🍌":
            print("Se encontro: " + fruta)
        else:
            print("NO COINCIDE")
else:
    print("NO SE ESTA BUSCANDO")

# FUNCIONES
print("\n" + "FUNCIONES CON PARAMETRO FINITOS Y KEYBOARDS")

x = 5
def saludar(nombre, edad):
    print("Hola " + nombre + " EDAD: " + str(edad))

saludar("Leydi", 20)
saludar("Luis", 21)
saludar("Octavio",21)
saludar("Axel",20)
saludar("Paty",21)

print("\n" + "FUNCIONES CON N PARAMETROS")
def asistencia(*alumnos):
    for alumno in alumnos:
        print("ASISTIO: " + alumno)

asistencia("LAURA", "ANGEL", "OCTAVIO","EMIR")
asistencia("AXEL","ROLEX")
asistencia("CJ")

# CLASES Y OBJETOS
print("\n" + "CLASES Y OBJETOS")

class Alumno:
    nombre = "EMIR"

# Creando Objeto
alumnoEmir: Alumno

# ENTRADA DE DATOS
print("\n" + "ENTRADA DE DATOS")
print("\n" + "INGRESA TU NOMBRE...")
nombre= input()
print(type(nombre))
palabras = nombre.split(" ")
nombre = nombre.capitalize()
a = ""
nombre = nombre.replace(" ","-")

for palabras in palabras:
    a += palabras.capitalize() + " "

print(a)
print("HOLA " + nombre)
