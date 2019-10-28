#Programa de administración de una heladeria
#Julian Sanchez
#GPLV3
def menu(inventario):           
  entrada=0
  while entrada != "q":
    print("""
    *****Administración de heladeria*****\n
Seleccione una opción (1 - 5) o q para salir 
1. Comprar
2. Agregar un nuevo producto
3. Ver inventario
4. Agregar al inventario
5. Total de ventas del dia
q: Salir""")
    entrada=input()
    x=["1","2","3","4","5","q"]
    if entrada in x:
      if entrada=="1":
        comprar()
      if entrada=="2":
        inventario=agregarproducto(inventario)
      if entrada=="3":
        verinventario(inventario)
      if entrada=="4":
        inventario=agregarinventario(inventario)
      if entrada=="5":
        ventas()
    else:
      print("Entrada inválida. Por favor intente de nuevo")
def agregarproducto(lista):
  print("""\nTipo de producto (1 o 2)
1. Helado 
2. Cobertura
q. salir""")
  x=0
  while x != "q":
    x=input()
    if x=="1":
      NProducto=input("\nIngrese el nombre del producto(Ejemplo:Galletas,M&Ms, etc.): ")
      lista[0][0].append(NProducto)
      valor=int(input("ingrese el valor de la porción: "))
      lista[0][1].append(valor)
      porciones=int(input("Ingrese el número de porciones disponibles: "))
      lista[0][2].append(porciones)  
      x="q"
    elif x=="2":
      NProducto=input("\nIngrese el nombre del producto(Ejemplo:Galletas,M&Ms, etc.): ")
      lista[1][0].append(NProducto)
      valor=int(input("ingrese el valor de la porción: "))
      lista[1][1].append(valor)
      porciones=int(input("Ingrese el número de porciones disponibles: "))
      lista[1][2].append(porciones)
      x="q"
    else:
      print("Entrada inválida. Por favor intente de nuevo")
  return lista
def agregarinventario(inventario):
  print("""\nTipo de producto (1 o 2)
1. Helado 
2. Cobertura
q. salir""")
  x=0
  while x != "q":
    x=input()
    if x=="1":
      print("\nSeleccione un producto")
      for y in range(0,len(inventario[0][0])):
        espacios="                         "
        espacios1="        "
        a=25-int(len(inventario[0][0][y]))
        a1=25-int(len(str(inventario[0][1][y])))
        print("{}) {}".format(y+1,inventario[0][0][y])+espacios[0:a]+str(inventario[0][1][y])+espacios1[0:a1]+str(inventario[0][2][y]))
      x=int(input())
      print("\nUsted seleccionó:")
      for y in range(0,len(inventario[0][0])):
        if (x-1)==y:
          print("{}) {}".format(y+1,inventario[0][0][y])+espacios[0:a]+str(inventario[0][1][y])+espacios1[0:a1]+str(inventario[0][2][y]))
          print("\nIngrese la cantidad de porciones a registrar:")
          h=int(input())
          suma=h+inventario[0][2][y]
          inventario[0][2][y]=suma
      x="q"
    elif x=="2":
      print("\nSeleccione un producto")
      for y in range(0,len(inventario[1][0])):
        espacios="                         "
        espacios1="        "
        a=25-int(len(inventario[1][0][y]))
        a1=25-int(len(str(inventario[1][1][y])))
        print("{}) {}".format(y+1,inventario[1][0][y])+espacios[0:a]+str(inventario[1][1][y])+espacios1[0:a1]+str(inventario[1][2][y]))
      x=int(input())
      print("\nUsted seleccionó:")
      for y in range(0,len(inventario[1][0])):
        if (x-1)==y:
          print("{}) {}".format(y+1,inventario[1][0][y])+espacios[0:a]+str(inventario[1][1][y])+espacios1[0:a1]+str(inventario[1][2][y]))
          print("\nIngrese la cantidad de porciones a registrar:")
          h=int(input())
          suma=h+inventario[1][2][y]
          inventario[1][2][y]=suma
      x="q"
    else:
      print("Entrada inválida. Por favor intente de nuevo")
  return inventario
def verinventario(inventario):
  print("\nHelados")
  for y in range(0,len(inventario[0][0])):
    espacios="                         "
    espacios1="        "
    a=25-int(len(inventario[0][0][y]))
    a1=25-int(len(str(inventario[0][1][y])))
    print("{}) {}".format(y+1,inventario[0][0][y])+espacios[0:a]+str(inventario[0][1][y])+espacios1[0:a1]+str(inventario[0][2][y]))
  print("\nCoberturas")
  for y in range(0,len(inventario[1][0])):
    espacios="                         "
    espacios1="        "
    a=25-int(len(inventario[1][0][y]))
    a1=25-int(len(str(inventario[1][1][y])))
    print("{}) {}".format(y+1,inventario[1][0][y])+espacios[0:a]+str(inventario[1][1][y])+espacios1[0:a1]+str(inventario[1][2][y]))

def main():
  inventario=[[[],[],[]],[[],[],[]]] #[helado[nombre][valor][cantidad]][cobertura[nombre][valor][cantidad]]
  menu(inventario)
main()
