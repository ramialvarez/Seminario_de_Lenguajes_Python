from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
# Variables contadoras de los fallos y aciertos del jugador
hits = 0
failures = 0
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    # Si el operador es / (division) chequeo que el segundo numero (el divisor) no sea 0, ya que no se puede dividir por 0.
    if operator == "/":
        while(number_2 == 0):
             number_2 = randrange(10)
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = float(input("resultado: "))
    # Comprobamos el operador y realizamos la cuenta
    match operator:
        case "+":
            result_2 = number_1 + number_2
        case "-":
            result_2 = number_1 - number_2
        case "*":
            result_2 = number_1 * number_2
        case "/":
            result_2 = round(number_1 / number_2,2) # Redondeo el resultado para que el usuario solo tenga que agregar dos digitos decimales, sobre todo en caso de que el resultado sea un numero periodico
    # Comprobamos si el usuario acertó o falló
    if (result == result_2):
        print("Correcto!!!")
        hits += 1
    else:
        print("Incorrecto!!!")
        failures += 1
            
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
# Mostramos los aciertos y fallos del jugador
print(f"\n Has acertado {hits} veces y has fallado {failures} veces") 
