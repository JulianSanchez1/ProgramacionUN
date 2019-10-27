#Programa que calcula el perimetro y el area de un triangulo con sus vertices ademas halla un segundo triangulo en la mitad de la arista del primero y halla su area y perimetro
#Julian Sanchez
#GPLV3
def pedirdatos():
  vertice1=[]
  vertice2=[]
  vertice3=[]
  vertice1=datos(input())
  vertice2=datos(input())
  vertice3=datos(input())
  l1,l2,l3=longitud(vertice1,vertice2,vertice3)
  perimetro=perime(l1,l2,l3)
  area=ar(l1,l2,l3)
  pt1,pt2,pt3=puntost2(vertice1,vertice2,vertice3)
  lt1,lt2,lt3=longitud(pt1,pt2,pt3)
  perimetrot=perime(lt1,lt2,lt3)
  areat=ar(lt1,lt2,lt3)
  print(perimetro)
  print(area)
  print(perimetrot)
  print(areat)
def datos(x):
  lista=[]
  g=float(x[0:4])
  g1=float(x[5:9])
  lista.append(g)
  lista.append(g1)
  return lista
def longitud(x1,x2,x3):
  l1=((x1[0]-x2[0])**2+(x1[1]-x2[1])**2)**(1/2)
  l2=((x2[0]-x3[0])**2+(x2[1]-x3[1])**2)**(1/2)
  l3=((x1[0]-x3[0])**2+(x1[1]-x3[1])**2)**(1/2)
  return l1,l2,l3
def perime(l1,l2,l3):
  per=round(l1+l2+l3,2)
  return per
def ar(l1,l2,l3):
  p=round((l1+l2+l3)/2,2)
  a=round((p*(p-l1)*(p-l2)*(p-l3))**(1/2),2)
  return a
def puntost2(x1,x2,x3):
  pt1=[]
  pt2=[]
  pt3=[]
  pt1=calculosp2(x1,x2)
  pt2=calculosp2(x2,x3)
  pt3=calculosp2(x1,x3)
  return pt1,pt2,pt3
def calculosp2(x1,x2):
  m=[]
  for x in range(0,2):
    l=(x1[x]+x2[x])/2
    m.append(l)
  return(m)
pedirdatos()
