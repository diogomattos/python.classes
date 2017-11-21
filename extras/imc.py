print ("Descubra o seu IMC e como está sendo considerado o seu peso.")
peso = int(input("Digite o seu peso (em kilos): "))
altura = float(input("Digite a sua altura (em metros ex:1.56): "))
gender = input("Digite o seu gênero (M ou F): ")

cimc = peso / (altura ** 2)
imc = round(cimc,2)

if (imc < 20.7 and gender == "M") or (imc < 19.1 and gender == "F"):
    print ("O seu IMC é",imc,"e é considerado Abaixo do Peso")
elif (imc >= 20.7 and imc <= 26.4 and gender == "M") or (imc >= 19.1 and imc <= 25.8 and gender == "F"):
    print ("O seu IMC é",imc,"e é considerado Peso ideal")
elif (imc >= 26.5 and imc <= 27.8 and gender == "M") or (imc >= 25.9 and imc <= 27.3 and gender == "F"):
    print ("O seu IMC é",imc,"e é considerado Pouco acima do peso")
elif (imc >= 27.9 and imc <= 31.1 and gender == "M") or (imc >= 27.4 and imc <= 32.3 and gender == "F"):
    print ("O seu IMC é",imc,"e é considerado Acima do peso")
else :
    print ("O seu IMC é",imc,"e é considerado Obesidade")
    
