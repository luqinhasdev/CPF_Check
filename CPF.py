def CPF1(CPF):
    digitoverificador = 0
    CPF_Lista = list(str(CPF))
    CPF_Inteiro = [int(x) for x in CPF_Lista]
    multiplicando = 10
    verificado = []
    for index in CPF_Inteiro:
        verificado.append(index * multiplicando)
        multiplicando -= 1
    verificadosomado = sum(verificado)
    if verificadosomado % 11 < 2:
        digitoverificador = 0
    else:
        digitoverificador = 11 - (verificadosomado % 11)