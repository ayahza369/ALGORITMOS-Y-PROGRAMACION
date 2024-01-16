

print('Bienvenidos a nuestra humible restaurante de Arepa')
Agua=3/2
Harina_pan=1
aceite_vegetal=2/3
mantequilla=1/3
sal_marina=1/6/16
sal_himalayan=1/3/16
Pollo=1
Aguacate=1/2
Mayonesa=1/2
Caraotas_Cocidas=1
Queso=1
op_1=raw_input('Te gustaria cosinar con aceite (A) o mantequilla (M)')
if op_1=="A":
    op_1_b=aceite_vegetal
else:
    op_1_b=mantequilla
op_2=raw_input('Ok, Perfecto. Ahora escoje si vas a usar sal marina (SM) o sal Himalayan (SH)')
if op_2=='SM':
    op_2_b=sal_marina
else:
    op_2_b=sal_himalayan
op_3=raw_input('Finalmente te gustaria Arepas Reina Pepiada (RP) de Queso (Q) o Domino (D)')
if op_3=='RP':
    op_3_b=Mayonesa+Aguacate+Pollo
elif op_3=='Q':
    op_3_b=Queso
elif op_3=='D':
    op_3_b=Caraotas_Cocidas+Queso
print('Despues de mezclar sus ingredientes, este es el peso/volumen de su arepa!:')
print(op_1_b+op_2_b+op_3_b+Harina_pan+Agua)
print('Buen Provecho!')
