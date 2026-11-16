
def gauss():
    print("======================================")
    print(" MÉTODO DE ELIMINAÇÃO DE GAUSS")
    print(" CLASSIFICAÇÃO DE SISTEMAS LINEARES")
    print("======================================")

    # Entrada da dimensão da matriz
    n = int(input("\nDigite a ordem da matriz (mínimo 3): "))

    while n < 3:
        print("A matriz deve ser no mínimo 3x3!")
        n = int(input("Digite novamente a ordem da matriz: "))

    # Entrada dos coeficientes e termos independentes
    matriz = []

    print("\nDigite os coeficientes e o termo independente:")

    for i in range(n):
        linha = []

        for j in range(n):
            valor = float(input(
                f"Digite o elemento A[{i+1}][{j+1}]: "
            ))
            linha.append(valor)

        b = float(input(f"Digite o termo independente b[{i+1}]: "))
        linha.append(b)

        matriz.append(linha)

    # Exibição da matriz aumentada
    print("\nMatriz aumentada inicial:")
    for linha in matriz:
        print(linha)

    # Método de Eliminação de Gauss
    for i in range(n):

        # Procurar o maior pivô em módulo
        pivo = i

        for k in range(i + 1, n):
            if abs(matriz[k][i]) > abs(matriz[pivo][i]):
                pivo = k

        # Trocar as linhas, se necessário
        matriz[i], matriz[pivo] = matriz[pivo], matriz[i]

        # Verificar se o pivô é zero
        if abs(matriz[i][i]) < 1e-10:
            continue

        # Eliminar os elementos abaixo do pivô
        for k in range(i + 1, n):
            fator = matriz[k][i] / matriz[i][i]

            for j in range(i, n + 1):
                matriz[k][j] -= fator * matriz[i][j]

    # Exibir matriz após a eliminação
    print("\nMatriz após a eliminação de Gauss:")
    for linha in matriz:
        print([round(x, 4) for x in linha])

    # Classificação do sistema
    posto_a = 0
    posto_ab = 0

    for i in range(n):
        tem_coeficiente = False

        for j in range(n):
            if abs(matriz[i][j]) > 1e-10:
                tem_coeficiente = True

        tem_termo = abs(matriz[i][n]) > 1e-10

        if tem_coeficiente:
            posto_a += 1
            posto_ab += 1
        elif tem_termo:
            posto_ab += 1

    print("\n======================================")
    print(" CLASSIFICAÇÃO DO SISTEMA")
    print("======================================")

    print("Posto da matriz A:", posto_a)
    print("Posto da matriz aumentada:", posto_ab)

    if posto_a != posto_ab:
        print("\nSistema Possível e Impossível (SI)")
        print("O sistema NÃO possui solução.")

    elif posto_a == n:
        print("\nSistema Possível e Determinado (SPD)")
        print("O sistema possui solução única.")

        # Retrosubstituição
        x = [0.0] * n

        for i in range(n - 1, -1, -1):
            soma = matriz[i][n]

            for j in range(i + 1, n):
                soma -= matriz[i][j] * x[j]

            x[i] = soma / matriz[i][i]

        print("\nSolução do sistema:")

        for i in range(n):
            print(f"x{i+1} = {x[i]:.4f}")

    else:
        print("\nSistema Possível e Indeterminado (SPI)")
        print("O sistema possui infinitas soluções.")


# Executar o programa
gauss()
