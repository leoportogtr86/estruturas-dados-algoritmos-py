## Algoritmo de Ordenação por Seleção

### Introdução

A ordenação por seleção (Selection Sort) é um dos algoritmos de ordenação mais simples e intuitivos. Ele pertence à
categoria dos algoritmos de ordenação por comparação e é caracterizado pela sua simplicidade e fácil implementação.
Apesar de não ser o algoritmo mais eficiente para grandes volumes de dados, ele é uma excelente escolha para aprender os
conceitos básicos de ordenação.

### Funcionamento do Algoritmo

O algoritmo de ordenação por seleção funciona da seguinte forma:

1. **Passo Inicial**: Divida o array em duas partes: a parte ordenada e a parte não ordenada. Inicialmente, a parte
   ordenada está vazia e a parte não ordenada contém todos os elementos.

2. **Seleção do Menor Elemento**: Encontre o menor elemento na parte não ordenada do array.

3. **Troca de Elementos**: Troque o menor elemento encontrado com o primeiro elemento da parte não ordenada. Agora, este
   menor elemento faz parte da parte ordenada.

4. **Repetição**: Repita os passos 2 e 3 até que todos os elementos estejam ordenados.

### Implementação em Python

Vamos agora ver uma implementação prática do algoritmo de ordenação por seleção em Python.

```python
def selection_sort(arr):
    # Percorre todos os elementos do array
    for i in range(len(arr)):
        # Encontra o menor elemento na parte não ordenada
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Troca o menor elemento encontrado com o primeiro elemento não ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# Exemplo de uso
array = [64, 25, 12, 22, 11]
sorted_array = selection_sort(array)
print("Array ordenado:", sorted_array)
```

### Passo a Passo da Implementação

Aqui está um passo a passo detalhado da implementação acima:

1. **Definição da Função**: A função `selection_sort` é definida e recebe como parâmetro um array `arr`.

2. **Loop Externo**: Um loop `for` percorre todos os elementos do array. A variável `i` representa o índice do primeiro
   elemento da parte não ordenada.

3. **Inicialização do Índice Mínimo**: A variável `min_idx` é inicializada com o valor de `i`, que é o índice do
   primeiro elemento da parte não ordenada.

4. **Loop Interno**: Um segundo loop `for` começa com `j` de `i+1` até o final do array para encontrar o menor elemento
   na parte não ordenada.

5. **Comparação de Elementos**: Dentro do loop interno, comparamos `arr[j]` com `arr[min_idx]`. Se `arr[j]` for menor,
   atualizamos `min_idx` com `j`.

6. **Troca de Elementos**: Fora do loop interno, trocamos `arr[i]` com `arr[min_idx]`, posicionando o menor elemento
   encontrado na posição correta.

7. **Repetição**: Os passos 2 a 6 são repetidos até que todos os elementos estejam ordenados.

8. **Retorno do Array Ordenado**: A função retorna o array ordenado.

9. **Teste da Função**: Criamos um exemplo de array, chamamos a função `selection_sort` e imprimimos o array ordenado.

10. **Execução**: Executamos o código para verificar se a ordenação foi realizada corretamente.

### Conclusão

O algoritmo de ordenação por seleção é uma ótima escolha para aprender os conceitos básicos de algoritmos de ordenação.
Sua implementação é simples e direta, o que facilita o entendimento dos passos necessários para ordenar um array. Apesar
de não ser o mais eficiente para grandes volumes de dados, seu estudo é fundamental para a compreensão de algoritmos
mais avançados.