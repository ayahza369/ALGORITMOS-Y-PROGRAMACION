print("Bienvenidos a este calculadora de anos bisiestos!")
num=(input("Escoje un ano entre 1900 y 2199"))

if num not in range(1900,2199):
    print("su opcion no esta entre el rango")
else: print("Ahora, calculamos!")

num_list=list(range(1900,num))
print(num_list)
