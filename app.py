n1 = float(input("primeiro numero: "))
n2 = float(input("segundo numero: "))
funcao = str(input(
    "selecione uma funcao: soma(s), subtracao(m) multiplicacao(v) divisao(d) -> "))

print("resultado:", end="")
if funcao == "s":
    print(n1 + n2)
elif funcao == "m":
    print(n1 - n2)
elif funcao == "v":
    print(n1 * n2)
elif funcao == "d":
    print(n1 / n2)
