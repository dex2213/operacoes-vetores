# CODIGO PARA OPERAÇÕES COM VETORES
# Versão: Python Puro

vetor1 = list(range(1, 12))
vetor2 = list(range(1, 12))

entrada1 = input("Primeiro vetor, separe com ',' :  ")
vetor1 = [int(x.strip()) for x in entrada1.split(',')]

entrada2 = input("Segundo vetor, separe com ',' : ")
vetor2 = [int(x.strip()) for x in entrada2.split(',')]

op = input("Escolha a operação (+, -, *, /): ")

if len(vetor1) != len(vetor2):
    print("Os vetores têm tamanhos diferentes.")
else:
    res = []
    for v1, v2 in zip(vetor1, vetor2):
        if op == '+':
            res.append(v1 + v2)
        elif op == '-':
            res.append(v1 - v2)
        elif op == '*':
            res.append(v1 * v2)
        elif op == '/':
            if v2 == 0:
                print(f"Erro: divisão por zero no elemento {v1} / {v2}. Operação cancelada.")
                break
            res.append(v1 / v2)
        else:
            print("Operação inválida.")
            break
    else:
        print("Primeiro vetor:", vetor1)
        print("Segundo vetor:", vetor2)
        print("Resultado da operação", op, "elemento a elemento:", res)

        vetor3 = res
        print("Terceiro vetor (resultados):", vetor3)
