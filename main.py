# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

peso = input('Seu peso: ')
altura = input('Sua altura: ')
conv_peso = float(peso)
conv_alt = float(altura)

imc = conv_peso / (pow(conv_alt, 2))
#
#  24.99 = 1.76, 2 = 3.0976 -> 24.99 * 3.0976 = peso

def pesoIdeal(imc):

    calc_peso_inicial = 18.5 * ( pow(conv_alt, 2) )
    calc_peso_final = 25.0 * ( pow(conv_alt, 2) )

    if(imc < 18.5):
        peso_ideal_inicial = calc_peso_inicial - conv_peso
        peso_ideal_final = calc_peso_final - conv_peso
        print("Você pode ganhar até " + str( "%.2f" % peso_ideal_inicial ) + "Kg para estar no inicio do seu IMC.")
        print("PESO ATUAL: " + str( ( "%.2f" % ( conv_peso ) ) ) + "Kg." )
        print("PESO IDEAL INICIAL: " + str( ( "%.2f" % ( conv_peso + peso_ideal_inicial ) ) ) + "Kg." )

        print("#######################################################################################################")
        print("Seu peso ideal final é de: " + str( peso_ideal_final ) + "Kg para estar no inicio do seu IMC, de acordo com a sua altura.")
        print("PESO ATUAL: " + str( ( "%.2f" % ( conv_peso ) ) ) + "Kg.")
        print("PESO IDEAL FINAL: " + str( ( "%.2f" % ( conv_peso + peso_ideal_final ) ) ) + "Kg.")

    elif(imc > 25.0):
        peso_ideal_inicial =  conv_peso - calc_peso_inicial
        peso_ideal_final = conv_peso - calc_peso_final
        print("Você pode perder até " + str( "%.2f" % peso_ideal_inicial ) + "Kg para estar no inicio do seu IMC, de acordo com a sua altura.")
        print("PESO ATUAL: " + str( ( "%.2f" % ( conv_peso ) ) ) + "Kg." )
        print("PESO IDEAL INICIAL: " + str( ( "%.2f" % ( conv_peso - peso_ideal_inicial ) ) ) + "Kg.")

        print("#######################################################################################################")
        print("Você pode perder até " + str( "%.2f" % peso_ideal_final ) + "Kg para estar no final do seu IMC.")
        print("PESO ATUAL: " + str( ( "%.2f" % ( conv_peso ) ) ) + "Kg.")
        print("PESO IDEAL FINAL: " + str( ( "%.2f" % ( conv_peso - peso_ideal_final ) ) ) + "Kg.")
    else:
        print()

if(imc < 16.0):
    print('Peso inexistente.', "%.2f" % imc)
elif(imc >= 16.0 and imc < 16.9):
    print('Muito abaixo do peso:', "%.2f" % imc)
    pesoIdeal(imc)
elif(imc >= 17.0 and imc < 18.5):
    print ('Abaixo do peso:', "%.2f" % imc)
    pesoIdeal(imc)
elif(imc >= 18.5 and imc < 25.0):
    print ('Peso normal:', "%.2f" % imc)
    pesoIdeal(imc)
elif(imc >= 25.0 and imc < 30.0):
    print ('Acima do peso:', "%.2f" % imc)
    pesoIdeal(imc)
elif(imc >= 30.0 and imc < 35.0):
    print ('Obsesidade grau I:', "%.2f" % imc)
    pesoIdeal(imc)
elif (imc >= 35.0 and imc < 40.1):
    print ('Obsesidade grau II:', "%.2f" % imc)
    pesoIdeal(imc)
else:
    print ('Obesidade grau III:', "%.2f" % imc)
    pesoIdeal(imc)