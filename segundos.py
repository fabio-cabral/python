segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
minutos_total = segundos // 60          # divisão inteira para obter a quantidade total de minutos
segundos_restantes = segundos % 60
horas_total = minutos_total // 60
minutos_restantes = minutos_total % 60
dias_total = horas_total // 24
horas_restantes = horas_total % 24
print(dias_total, "dias,", horas_restantes, "horas,", minutos_restantes, "minutos e", segundos_restantes, "segundos.")