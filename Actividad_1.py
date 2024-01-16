x =raw_input("Eres chico o chica?")
x = x.lower()
w="Bienvenid"
if x =="chico":
    w +="o"
else:
    w += "a"
print ( w , "al mundo de los pokemon!")

y=raw_input('Que edad tienes?')
if int(y)<10 and x=='chico':
    print("No tienes edad para ser entrenador")
elif int(y)<10 and x=='chica':
    print("No tienes edad para ser entrenadora")
else:
    print("Vamos!")

reg=raw_input("Necesitaras un companiero de viaje. En que region te encuentras?")
if reg=="Kanto" and x=="chico": #What is the purpose of Kanto condition? it doesn't work?

    print("Tu companiera de viaje es Misty!")
else:
    print("Tu companiero de viaje es Brook!")

tipo=raw_input("Que tipo de pokemon quieres para empezar?")
if tipo== "agua":
    print("Tu starter es Oshawott")
elif tipo=="fuego":
    print("Tu starter es Cyndaquil")
else:
    print("Tu starter es Rowlet")
