# 1. **Implementação Básica**:
# - Implemente a busca binária em Python para uma lista de números inteiros ordenados.
# Teste seu algoritmo com diferentes valores de entrada.
def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio
        elif alvo > lista[meio]:
            inicio = meio + 1
        else:
            fim = meio - 1


lista = [10, 1, 5, 7, 100, 0, 2000, -45]

lista.sort()

print(f"Lista ordenada: {lista}")
print(busca_binaria(lista, 2000))
