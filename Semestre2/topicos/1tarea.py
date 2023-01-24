#Juego de suma 0 entre 2 personas

#Matriz de pagos: es lo que B tiene que pagar a A en cada caso
# a/b  1  2  3 
# 1    3  2 -3
# 2    0 -4  6
# 3    0 -5  5

#Cual es el valor esperado del pago que B hará al jugador A ?
# Probabilidades de A  1(2/3) 2(1/3) 3 (0)
# Probabilidades de B  1(0)   2(3/5) 3 (2/5)

# Se tienen 3 opciones a elegir (1,2,3) por cada jugador
# Existen 9 combinaciones posibles, pero no todas aplican, así que la matriz quedaría:

#Nueva matriz de pagos: es lo que B tiene que pagar a A en cada caso
# a/b  1  2  3 
# 1    0  2 -3
# 2    0 -4  6
# 3    0  0  0

# quedamos con solo 4 opciones (A,B) (1,2) (1,3) (2,2) (2,3)

payments = {
    "12":2,
    "13":-3,
    "22":-4,
    "23":6
    }

# Selecciones de cada jugador segun su probabilidad

options_a = [1,1,2]
options_b = [2,2,2,3,3]

import random
list_a = []

def randomizer(test_number):
    for num in range(0, test_number):
        randNumber_a = random.randint(0, 2)
        randNumber_b = random.randint(0, 4)
        selected_a = options_a[randNumber_a]
        selected_b = options_b[randNumber_b]
        list_a.append(str(selected_a)+str(selected_b))
    return list_a

def paymentSum(resultList,payments):
    totalPayment = 0
    for i in resultList:
        totalPayment += payments[i]
        #print(totalPayment)
    return(totalPayment)
    

test_number = 10000000
resultList = randomizer(test_number)
totalPayment = paymentSum(resultList, payments)
paymentPerPlay = totalPayment/(test_number)

print(f'El promedio de pago por cada juego (jugando {test_number} veces) es de {paymentPerPlay}')

#Lo checo con la suma de probabilidades

prob_a1 = 2/3
prob_a2 = 1/3
prob_b2 = 3/5
prob_b3 = 2/5

prob_a1Ub2 = prob_a1*prob_b2
prob_a2Ub2 = prob_a2*prob_b2
prob_a1Ub3 = prob_a1*prob_b3
prob_a2Ub3 = prob_a2*prob_b3

print('Validación con probabilidad')
print(f'''las probabilidades son: 
{prob_a1Ub2},{prob_a1Ub3}
{prob_a2Ub2},{prob_a2Ub3}
''')

#Matriz de pagos

pago_a1Ub2 = 2
pago_a2Ub2 = -4
pago_a1Ub3 = -3
pago_a2Ub3 = 6

# verifico los pagos segun cada probabilibad

total_esperado = (prob_a1Ub2*pago_a1Ub2)+(prob_a2Ub2*pago_a2Ub2)+(prob_a1Ub3*pago_a1Ub3)+(prob_a2Ub3*pago_a2Ub3)
# print(prob_a1Ub2*pago_a1Ub2)
# print(prob_a2Ub2*pago_a2Ub2)
# print(prob_a1Ub3*pago_a1Ub3)
# print(prob_a2Ub3*pago_a2Ub3)
print(f'El total esperado (utilizando suma de probabilidades) es {total_esperado}')
