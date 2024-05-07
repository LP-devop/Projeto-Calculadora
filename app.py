n1 = float(input("primeiro numero: "))
n2 = float(input("segundo numero: "))
funcao = str(input(
    "selecione uma funcao: adicão(a), subtracao(s) multiplicacao(m) divisao(d) -> "))

print("resultado:", end="")
if funcao == "a":
    print(n1 + n2)
elif funcao == "s":
    print(n1 - n2)
elif funcao == "m":
    print(n1 * n2)
elif funcao == "d":
    print(n1 / n2)
