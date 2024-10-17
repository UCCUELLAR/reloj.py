# Realizar un codigo en python que simule un reloj
# formato 24 horas
# que empiece en 00:00 hasta 23:59 y se reinicie
# pero que implemente time.sleep(x) para que se actualice
# cada segundo o mas  acelerado.

import time

def reloj_simulado():
    horas = 0
    minutos = 0
    
    while True:
        # Formatear la hora en formato 24 horas
        tiempo_actual = f"{horas:02}:{minutos:02}"
        print(tiempo_actual, end='\r')  # Imprime en la misma línea
        
        # Espera un segundo
        time.sleep(1)  # Cambia a un valor menor para acelerar
        
        # Incrementar los minutos
        minutos += 1
        
        # Si los minutos llegan a 60, incrementamos las horas y reiniciamos los minutos
        if minutos == 60:
            minutos = 0
            horas += 1
            
            # Si las horas llegan a 24, reiniciamos las horas
            if horas == 24:
                horas = 0


reloj_simulado()
