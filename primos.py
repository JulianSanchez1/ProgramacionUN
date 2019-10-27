#Programa que calcula los numeros primos de un número
#Julian Sanchez
#GPLV3
x=int(input())
lista=[]
count=0
primos=[]
for y in range(1,(x+1)):
  if x%y == 0:
    lista.append(y)
for z in range (1,len(lista)):
  for c in range(1,(lista[z]+1)):
    if lista[z]%c == 0:
      count=count+1
  if count == 2:
    primos.append(lista[z])
  count=0
for k in range(0,len(primos)):
  print(primos[k]) 
