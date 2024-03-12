numero_1 = int(input("Informe o primeiro número"))
numero_2 = int(input("Informe o segundo número"))
operador = input("Informe o operador\n + adicao \n - subtracao \n / divisao \n * multiplicacao \n => ")
if operador == "+":
    resultado = numero_1 + numero_2
    print(f"resultados= {resultado}")
elif operador == "-":
    resultado = numero_1 - numero_2
    print(f"resultados= {resultado}")
elif operador == "/":
    resultado = numero_1 / numero_2
    print(f"resultados= {resultado}")
elif operador == "*":
    resultado = numero_1 * numero_2
    print(f"resultados= {resultado}")
else: print("escolha uma das quatro opções")
def adicao (a, b):
    return a + b
def subtracao (a, b):
    return a - b
def divisao (a, b):
    if b !=0:
        return a / b
    else:
        return "Não é possível..."

def multiplicacao (a, b):
    return a * b
