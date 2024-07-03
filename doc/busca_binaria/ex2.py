# 2. **Verificação de Elementos Não Existentes**:
# - Modifique sua implementação de busca binária para retornar uma mensagem específica
# quando o elemento não estiver presente na lista.
def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return f"O alvo está presente no índice {meio}."
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return "O número não foi encontrado..."


lista = [10, 1, 5, 7, 100, 0, 2000, -45]

lista.sort()

print(f"Lista ordenada: {lista}")
print(busca_binaria(lista, -450))
