#Programa que detecta si una lista esta en forma ascendente,descendente o desorden
#Julian Sanchez
#GPLV3
x2=0
c=0
c1=0
x1=int(input())
while x2 != -1:
  x2=int(input())
  if  x1<=x2 and x2 !=-1:
    c+=1
  if  x1>=x2 and x2 != -1:
    c1+=1
  x1==x2

if c1 == 0:
  print("ascendente")
if c == 0:
  print("descendente")
if c1 != 0 and c != 0:
  print("desorden")
