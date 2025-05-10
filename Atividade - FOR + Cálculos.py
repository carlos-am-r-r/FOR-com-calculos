while True:

    linha = '¸,ø¤º°`°º¤ø,¸¸,ø¤º°', '°º¤ø,¸¸,ø¤º°`°º¤ø,¸', '░▒▓█', '█▓▒░', '≪ ◦ ❖ ◦ ≫'
    tela = (f'{linha[0]}{linha[0]}\n'
            f'{linha[2]} Selecione o seu programa! {linha[3]}\n'
            f'{linha[0]}{linha[0]}')

    start = ('(♡ര‿ര)\n\n1 - Farenheit para Celcius\n2 - Farenheit para Celcius customizável\n'
             '3 - Soma quingentésima\n4 - Soma quingentésima exclusiva\n'
             '5 - Tabuada quinta\n6 - Tabuada livre\n'
             '7 - Sair do programa.')

    print(tela)
    print('obs: o programa está em um laço while para facilitar os testes\n')

    start=(input(start))
    print(f'{linha[0]}{linha[0]}')

    if start != "":
        start=int(start)
    if start == 7:
        break


    # 1. A conversão de graus Fahrenheit para graus Celsius é obtida pela fórmula abaixo.
    # Calcule a conversão e construa o relatório de saída tabular (em forma de tabela de duas colunas)
    # de graus Celsius em função de graus Fahrenheit que que variam de 45 a 80 de 1 em 1.
    # Fórmula: c = 5 ( f - 32 )

    if start == 1:

        for f in range(45,81,1):

            # Fahreinheit | Celsius

            print(f'{f} Fº | {5/9*(f-32):.3F} Cº')


    #2. Melhore o programa anterior para torná-lo mais abrangente.
    # Agora, o usuário fornecerá os valores inicial e final de graus Fahrenheit.
    # Calcule a conversão e gere o relatório de saída tabular (em forma de tabela) considerando o intervalo digitado.
    #Gere o relatório na ordem crescente, se o valor inicial for menor ou igual ao valor final.
    # E na ordem decrescente, se valor inicial for maior que o valor final.

    if start == 2:

        inicial=int(input('Selecione o valor inicial.'))

        final=int(input('Selecione o valor final'))

        if inicial < final:

            for f in range(inicial, final+1, 1):

                print(f'{f} Fº | {5 / 9 * (f - 32):.3F} Cº')

        elif inicial > final:

            for f in range(inicial, final-1, -1):

                print(f'{f} Fº | {5 / 9 * (f - 32):.3F} Cº')

    #3. Elabore o programa para somar todos os números inteiros que se encontram no intervalo de um a quinhentos.

    if start == 3:
        soma=0
        for i in range(1, 501, 1):
            soma=soma+i
        print(soma)

        #4. Elabore o programa para somar todos os números inteiros que são
        #ao mesmo tempo ímpar e múltiplo de três que se encontram no intervalo de um a quinhentos.

    if start == 4:
        soma=0
        for i in range(1,501,1):
            po=0
            if i % 6 == 0:
                po = i
            soma+=po
        print()
        print(soma)

    if start == 5:
        o = 5
        for i in range(1, 11, 1):
            print(f'{i} X {o} = {i * o}')

    if start == 6:
        o=int(input('Selecione seu número'))
        for i in range(1,11,1):
            print(f'{i} X {o} = {i*o}')

    print(f'{linha[0]}{linha[0]}')
    again=input('\nreiniciar? y/n\n')
    if again == 'n':
        break

print('"(っ - ‸ - ς)ᶻ 𝗓 𐰁')