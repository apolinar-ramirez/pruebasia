# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os

def ejemplo(x1,x2):
    return x1+x2

"""
# la entrada es de tipo str
sx = input("Dame un número:")
print("el número fué "+ sx)

x = float(sx)
if x == 6:
    print("El número fue 6")
    print(x)
else:
    print("el número no fue 6")
    
for letra in "Hola":
    print("La letra fue: "+ letra)
"""

"""
try:
    Value = int(input("Type a number between 1 and 10: "))
except (ValueError, KeyboardInterrupt):
    print("You must type a number between 1 and 10!")
except:
    print("This is the generic error!")
else:
    if (Value > 0) and (Value <= 10):
        print("You typed: ", Value)
    else:
        print("The value you typed is incorrect!")
"""
"""
# lanza una excepción      
try:
    raise ValueError
except ValueError as e:
    print("ValueError Exception!", e.strerror)
"""
"""
# muestra carpeta de trabajo
print(os.getcwd())
# cambia area de trabajo 
os.chdir('/home/apolinar/anaconda/area')
# muestra contenido de la carpeta de trabajo
os.listdir()
"""
"""
# ejemplo de uso de un paquete 
import archivo
archivo.SayHello('Oscar')
"""
"""
# imprime en orden mediante el operador 'splat'
Colors = ["Red", "Orange", "Yellow", "Green", "Blue"]
print(*Colors, sep='\n')
# imprime usando un formato los dos primeros elementos
print('First: {0}\nSecond: {1}'.format(*Colors))

# empleo de la clase Counter
from collections import Counter
MyList = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1, 5]
ListCount = Counter(MyList)
print(ListCount)
for ThisItem in ListCount.items():
    print("Item: ", ThisItem[0],
          " Appears: ", ThisItem[1])
print("The value 2 appears {0} times."
    .format(ListCount.get(2)))
"""

"""
# tuplos
Mituplo = ("uno", "dos", "tres")
print(Mituplo)
# uso de la función dir que muestra las funciones aplicables
print(dir(Mituplo))
# concatena al inicio del tuplo
Mituplo = ("cuatro",)+ Mituplo
# concatena al final del tuplo
Mituplo = Mituplo.__add__(("cinco",))
print(Mituplo)
"""

"""
# diccionarios
Colors = {'Sam': 'Blue', 'Amy': 'Red', 'Sarah': 'Yellow'}
print(Colors["Sarah"])
# agrega un item al diccionario
Colors.update({'Harry': 'Orange'})
for item in Colors.keys():
    print("{0} usa el color {1}".format(item, Colors[item]))
"""

"""
# queues (colas)  primero en entrar, primero en salir
import queue
# se crea cola con 3 items
MyQueue = queue.Queue(3)
# se pregunta si está vacía
print(MyQueue.empty())
input("Press any key when ready...")
# se agregan items
MyQueue.put(1)
MyQueue.put(2)
# se pregunta si está llena
print(MyQueue.full())
input("Press any key when ready...")
MyQueue.put(3)
print(MyQueue.full())
input("Press any key when ready...")
# se saca item
print(MyQueue.get())
print(MyQueue.empty())
print(MyQueue.full())
input("Press any key when ready...")
print(MyQueue.get())
print(MyQueue.get())
"""
"""
# deques
import collections
MyDeque = collections.deque("abcdef", 10)
print("Starting state:")
for Item in MyDeque:
    print(Item, end=" ")
print("\r\n\r\nAppending and extending right")
MyDeque.append("h")
MyDeque.extend("ij")
for Item in MyDeque:
    print(Item, end=" ")
print("\r\nMyDeque contains {0} items."
      .format(len(MyDeque)))
print("\r\nPopping right")
print("Popping {0}".format(MyDeque.pop()))
for Item in MyDeque:
    print(Item, end=" ")
print("\r\n\r\nAppending and extending left")
MyDeque.appendleft("a")
MyDeque.extendleft("bc")
for Item in MyDeque:
    print(Item, end=" ")
print("\r\nMyDeque contains {0} items."
      .format(len(MyDeque)))
print("\r\nPopping left")
print("Popping {0}".format(MyDeque.popleft()))
for Item in MyDeque:
    print(Item, end=" ")
# remueve la 1er. 'a'    
print("\r\n\r\nRemoving")
MyDeque.remove("a")
for Item in MyDeque:
    print(Item, end=" ")
"""
"""
# clases
class Miclase:
    # metodo de clase -> no puede usarse desde una instancia
    def hola():
        print("hola clase")
    # método de la instancia; self hace referencia a la instancia
    def decir_hola(self):
        print("hola instancia")
    Mivariable = 10

Mi_instancia = Miclase()
print(Mi_instancia.Mivariable)
# método de clase, solo puede emplearlo la clase
Miclase.hola()
# Mi_instancia.hola() NO es válido
Mi_instancia.decir_hola()
"""
"""
# uso de constructor
class MyClass:
    Greeting = ""
    # inicializa variable de la clase con un argumento en 
    # función __init__
    def __init__(self, Name="there"):
        self.Greeting = Name + "!"
    def SayHello(self):
        print("Hello {0}".format(self.Greeting))

Mi_instancia = MyClass()
Mi_instancia.SayHello()
Mi_instancia2 = MyClass("José")
Mi_instancia2.SayHello()
"""
"""
# Ejemplo de Herencia
class Animal:
    def __init__(self, Name="", Age=0, Type=""):
        self.Name = Name
        self.Age = Age
        self.Type = Type
    def GetName(self):
        return self.Name
    def SetName(self, Name):
        self.Name = Name
    def GetAge(self):
        return self.Age
    def SetAge(self, Age):
        self.Age = Age
    def GetType(self):
        return self.Type
    def SetType(self, Type):
        self.Type = Type
    def __str__(self):
        return "{0} is a {1} aged {2}".format(self.Name,
                                              self.Type,
                                              self.Age)
class Chicken(Animal):
    def __init__(self, Name="", Age=0):
        self.Name = Name
        self.Age = Age
        self.Type = "Chicken"
    def SetType(self, Type):
        print("Sorry, {0} will always be a {1}"
              .format(self.Name, self.Type))
    def MakeSound(self):
        print("{0} says Cluck, Cluck, Cluck!".format(self.Name))
# instancia de la clase heredada        
m= Chicken("negra",2)
m.MakeSound()
m.__str__()
"""

# almacenando en archivos
import csv
import os.path
import sys
class FormatData2:
    def __init__(self, Name="", Age=0, Married=False):
        self.Name = Name
        self.Age = Age
        self.Married = Married
    def __str__(self):
        OutString = "'{0}', {1}, {2}".format(
            self.Name,
            self.Age,
            self.Married)
        return OutString
    def SaveData(Filename = "", DataList = []):
        with open(Filename,
                  "w", newline='\n') as csvfile:
            DataWriter = csv.writer(
                csvfile,
                delimiter='\n',
                quotechar=" ",
                quoting=csv.QUOTE_NONNUMERIC)
            DataWriter.writerow(DataList)
            csvfile.close()
            print("Data saved!")
    def ReadData(Filename = ""):
        with open(Filename,
                  "r", newline='\n') as csvfile:
            DataReader = csv.reader(
                csvfile,
                delimiter="\n",
                quotechar=" ",
                quoting=csv.QUOTE_NONNUMERIC)
            Output = []
            # it sees the nonterminating entries
            #(those that aren’t last in the file \n) as actually 
            #being two list entries. The first entry
            #contains data; the second is blank 
            for Item in DataReader:
                Output.append(Item[0])
            csvfile.close()
            print("Data read!")
            return Output

'''
# agregando registros
NewData = [FormatData2("George", 65, True),
FormatData2("Sally", 47, False),
FormatData2("Doug", 52, True)]
FormatData2.SaveData("TestFile.csv", NewData)
'''

# lectura del archivo
if not os.path.isfile("TestFile.csv"):
    print("Favor de cambiar de trayectoria a /home/apolinar/anaconda/area!")
    sys.exit(99)
datos = FormatData2.ReadData("TestFile.csv")

# se muestran registros
for registro in datos:
        print(registro)
        
'''        
# agregando un registro en la lista en memoria        
print("\r\nAdding a record for Harry en memoria.")
NewRecord = "'Harry', 23, False"
datos.append(NewRecord)
for registro in datos:
    print(registro)        
        
# guardando lista en un nuevo archivo
FormatData2.SaveData("TestFile2.csv", datos)
'''
'''
# borrando un registro
print("\r\nRemoving Doug's record.")
try:
    Location = datos.index("'Doug', 52, True")
    print('registro: '+ str(Location))
    Registro = datos[Location]
    datos.remove(Registro)
    # se muestran registros
    for registro in datos:
            print(registro)
    print('Registro borrado: '+ Registro)            
except ValueError:
    print('Registro NO localizado')
    
# Modificando un registro
print("\r\nModifying Sally's record.")
try:
    Location = datos.index("'Sally', 47, False")
    Record = datos[Location]
    # retorna una lista con los datos del registro separado por coma
    Split = Record.split(",")
    NewRecord = FormatData2(Split[0].replace("'", ""),
                            int(Split[1]),
                            bool(Split[2]))
    NewRecord.Married = True
    NewRecord.Age = 48
    datos.append(NewRecord.__str__())
    datos.remove(Record)
    for Entry in datos:
        print(Entry)
    FormatData2.SaveData("TestFile3.csv", datos)
    print('Registro modificado.')
except ValueError:
    print('Registro NO localizado.')    
'''

# borrando un archivo
os.remove('TestFile3.csv')
print('Archivo borrado.')    

