segundosInput = int(input("Por favor, entre com o número de segundos que deseja converter:"))
dias = segundosInput // 60 // 60 // 24
horas = segundosInput // 60 // 60
minutos = segundosInput // 60
segundos = segundosInput-(minutos * 60)
print (dias, "dias,",horas - dias * 24,"horas,",minutos - horas * 60,"minutos e", segundos,"segundos.")
