print("EJERCICIO UNO")
'SON LAS 7 DE LA NOCHE YA ME QUIERO IR'
# SI ENCUENTRA EL NUMERO 7 Y ES MENOR A 8
# IMPRIMIR EL NUMERO 7 CONVERTIDO A INT
# Y EL TEXTO ' ES HORA DE IRNOS SON LAS: '7''

tex = "SON LAS 7 DE LA NOCHE YA ME QUIERO IR"
if "7" in tex:
    num = 7
if num < 8:
    print("ES HORA DE IRNOS SON LAS:" + str(num))


print("\n"+"EJERCICIO DOS")
#0.CREAR UNA LSITA DE NUMEROS DEL 1 AL 10
#1.CONVERTIR LA LISTA EN UN SET PARA ELIMINAR DUPLICADOS
#2.CALCULAR LA SUMA DE LOS NUMEROS USANDO UNA LISTA
#3.CALCULAR LA SUMA DE LOS NUMEROS USANDO UN SET
#4.CREAR UN DICCIONARIO PARA ALAMCENAR LAS ESTADISTICAS
"""   NUMEROS UNICOS, SUMA TOTAL LISTA, SUMA TOTAL SET,
   MAXIMO VALOR, MINIMO VALOR
   IMPRIMIR LAS ESTADISTICAS
"""
print("\n" + "#0")
numeros = [1,2,5,3,2,3,3,6,10,8,9]
print(numeros)

print("\n" + "#1")
numerosSet = set(numeros)
print(numerosSet)

print("\n" + "#2")
sumaLista = sum(numeros)
print(sumaLista)

print("\n" + "#3")
sumaSet = sum(numerosSet)
print(sumaSet)

print("\n" + "#4")
len(numerosSet)
max(numeros)
min(numeros)

# print("\n"+"Numeros Unicos" +"\n"+ str(len(numerosSet)))
# print("\n"+"Numero Maximo" +"\n"+ str(max(numeros)))
# print("\n"+"Numero Minimo" +"\n"+ str(min(numeros)))

diccionario2 = {
    "Numeros Unicos": len(numerosSet),
    "Numero Maximo": max(numeros),
    "Numero Minimo": min(numeros),
    "Suma Total Lista": sumaLista,
    "Suma Total Set": sumaSet
}

print("DICCIONARIO" +"\n"+str(diccionario2))


print("\n"+"EJERCICO TRES")
print("INGRESA TU NOMBRE...")
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