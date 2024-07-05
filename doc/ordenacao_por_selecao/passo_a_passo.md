Claro, vamos dividir a explicação do código de ordenação por seleção em 10 etapas detalhadas.

### Passo a Passo Explicativo da Implementação do Selection Sort em Python

Aqui está o código para referência:

```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


array = [64, 25, 12, 22, 11]
sorted_array = selection_sort(array)
print("Array ordenado:", sorted_array)
```

### Etapa 1: Definição da Função

```python
def selection_sort(arr):
```

- **O que faz:** Define a função `selection_sort` que recebe um array `arr` como argumento.
- **Importância:** Estabelece a estrutura inicial da função que realizará a ordenação.

### Etapa 2: Loop Externo

```python
for i in range(len(arr)):
```

- **O que faz:** Inicia um loop que percorre cada elemento do array `arr`.
- **Importância:** Este loop garante que cada posição do array será avaliada para encontrar o menor elemento e
  posicioná-lo corretamente.

### Etapa 3: Inicialização do Índice Mínimo

```python
min_idx = i
```

- **O que faz:** Define `min_idx` como o índice do elemento atual `i`.
- **Importância:** `min_idx` mantém o índice do menor elemento encontrado na parte não ordenada do array.

### Etapa 4: Loop Interno

```python
for j in range(i + 1, len(arr)):
```

- **O que faz:** Inicia um segundo loop que começa a partir do próximo elemento `i+1` até o final do array.
- **Importância:** Este loop é usado para encontrar o menor elemento na parte não ordenada do array.

### Etapa 5: Comparação de Elementos

```python
if arr[j] < arr[min_idx]:
    min_idx = j
```

- **O que faz:** Compara o elemento atual `arr[j]` com o menor elemento encontrado `arr[min_idx]`.
- **Importância:** Se `arr[j]` for menor que `arr[min_idx]`, atualiza `min_idx` para `j`. Isso mantém `min_idx`
  apontando para o menor elemento na parte não ordenada.

### Etapa 6: Troca de Elementos

```python
arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

- **O que faz:** Troca o elemento na posição `i` com o elemento na posição `min_idx`.
- **Importância:** Coloca o menor elemento encontrado na posição correta na parte ordenada do array.

### Etapa 7: Repetição do Processo

- **O que faz:** Os passos 2 a 6 são repetidos para cada elemento do array.
- **Importância:** Garante que todos os elementos do array sejam ordenados ao final do processo.

### Etapa 8: Retorno do Array Ordenado

```python
return arr
```

- **O que faz:** Retorna o array `arr` que agora está ordenado.
- **Importância:** Permite que a função `selection_sort` forneça o array ordenado como saída.

### Etapa 9: Teste da Função

```python
array = [64, 25, 12, 22, 11]
sorted_array = selection_sort(array)
```

- **O que faz:** Define um exemplo de array `array` e chama a função `selection_sort` passando este array.
- **Importância:** Testa a função com um conjunto de dados específico para verificar se a ordenação está correta.

### Etapa 10: Impressão do Resultado

```python
print("Array ordenado:", sorted_array)
```

- **O que faz:** Imprime o array ordenado `sorted_array`.
- **Importância:** Exibe o resultado final da ordenação, permitindo verificar visualmente se a função funcionou como
  esperado.

### Conclusão

Esse passo a passo detalhado explica cada trecho do código do algoritmo de ordenação por seleção, ajudando a entender o
funcionamento e a lógica por trás de cada etapa. Com essa compreensão, você pode adaptar e aplicar este algoritmo em
diferentes situações onde a ordenação de dados seja necessária.