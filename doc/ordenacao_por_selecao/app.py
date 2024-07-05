def ordenacao_por_selecao(arr):
    for i in range(len(arr)):
        indice_minimo = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j

        arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]

    return arr


elementos_desordenados = [10, 5, 0, 1, 100, -100, -78]
ordenados = ordenacao_por_selecao(elementos_desordenados)

print(ordenados)
