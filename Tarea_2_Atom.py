print("Bienvenidos a este calculadora de anos bisiestos!")
num=int(input("Escoje un ano entre 1900 y 2199"))
if num not in range(1900,2199):
    print("su opcion no esta entre el rango")
    quit()
else:
    print("Ahora, calculamos!")

for i in range(1900,num+1):
    x=list[i%4]
    print(x)
