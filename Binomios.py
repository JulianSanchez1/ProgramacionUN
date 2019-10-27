#Programa que expande un binomio por medio del binomio de newton
#Julian Sanchez
#GPLV3
def factorial(n):
  if n == 0:
    return 1
  else:
    return n*factorial(n-1)
def coeficientebinomial(x):
  y=[1]
  for z in range(1,x):
    f1=factorial(x)
    f2=factorial(z)
    f3=factorial((x-z))
    h=f1/(f2*f3)  
    y.append(int(h))
  y.append(1)
  return y
def  valores (exp, variable):
  if exp>1:
    return variable+"**"+str(exp)+""
  elif exp==1:
    return variable+""
  else:
    return ""
def armar(n,z):
  c=[]
  for i in range(n+1):
    x = "x"
    y = "y"
    x1 = valores(n-i, x)
    y1 = valores(i, y)
    if z[i]>1:
      c.append(str(z[i])+'*'+str(x1)+"*"+str(y1))
    elif z[i] == 1:
      c.append(str(x1)+str(y1)) 
  for i in range(len(c)):
    if c[i][-1] == "*":
      c[i] = list(c[i])
      c[i].pop()
      c[i] = "".join(c[i])
  f="+".join(c)
  return f
def main():
  x=int(input())
  z=[]
  z=coeficientebinomial(x)
  c=[]
  c=armar(x,z)
  print(c)
  
main()
