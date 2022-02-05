s1 = int(input('Digite um valor inicial:'))
s2 = int(input('Digite um valor final:'))
qda_positivo = 0
qda_par = 0
qda_impar = 0
soma_positivo = 0
soma_par = 0
soma_impar = 0
cont = s1
if s1 < s2:
    while cont <= s2:
        if cont > 0:
            qda_positivo = qda_positivo + 1
            soma_positivo = soma_positivo + cont
        if cont % 2 == 0:
            qda_par = qda_par + 1
            soma_par = soma_par + cont
        else:
            qda_impar = qda_impar + 1
            soma_impar = soma_impar + cont
        cont = cont + 1
    media_positivo = soma_positivo / qda_positivo
    media_par = soma_par / qda_par
    media_impar = soma_impar / qda_impar
    print('Quantidade de valores positivo: {}'.format(qda_positivo))
    print('Media de valores positivos:{}'.format(media_positivo))
    print('Quantidade de valores pares:{}'.format(qda_par))
    print('Media de valores pares:{}'.format(media_par))
    print('Quantidade de valores impares:{}'.format(qda_impar))
    print('Medias de valores impares:{}'.format(media_impar))

else:
        print('Voce digitou um valor inicial maior ou igual ao final. Encerrando o programa.... ')




