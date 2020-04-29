
lista=[]
listaPar=[]
while True:
    print("Introduce número / para salir introduce * ")
    a=input()
    if(a=='*'):
        break
    else:
        lista.append(int(a))

for i in lista:
    if(i%2==0):
        listaPar.append(i)
    
print("Ha introducido", len(listaPar),"números pares")
print("Los números introducidos son:",listaPar)

