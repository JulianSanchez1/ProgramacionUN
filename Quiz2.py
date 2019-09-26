x1=int(input())
y1=int(input())
r1=int(input())
x2=int(input())
y2=int(input())
r2=int(input())
cx=float(input())
cy=float(input())
d1=((x1-cx)**2+(y1-cy)**2)**1/2
d2=((x2-cx)**2+(y2-cy)**2)**1/2
if d1 <= r1:
  if d2 <= r2:
    print("Dentro")
  else:
    print("Dentro del circulo 1")
elif d2 <= r2:
  print("Dentro del circulo 2")
else:
  print("Fuera")
