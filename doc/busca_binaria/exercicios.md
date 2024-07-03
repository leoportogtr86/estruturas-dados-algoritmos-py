### Lista de Exercícios sobre Busca Binária

1. **Implementação Básica**:
    - Implemente a busca binária em Python para uma lista de números inteiros ordenados. Teste seu algoritmo com
      diferentes valores de entrada.

2. **Verificação de Elementos Não Existentes**:
    - Modifique sua implementação de busca binária para retornar uma mensagem específica quando o elemento não estiver
      presente na lista.

3. **Busca em Lista de Strings**:
    - Adapte a busca binária para funcionar em uma lista ordenada de strings. Verifique se uma determinada palavra está
      na lista.

4. **Contagem de Comparações**:
    - Modifique a função de busca binária para contar o número de comparações feitas durante a pesquisa e retorne esse
      valor junto com o índice do elemento (ou -1 se não encontrado).

5. **Busca em Lista de Tuplas**:
    - Dada uma lista de tuplas onde cada tupla contém dois valores (por exemplo, [(1, 'a'), (2, 'b'), (3, 'c')]), adapte
      a busca binária para encontrar uma tupla baseada no primeiro valor.

6. **Intervalo de Busca**:
    - Modifique a busca binária para retornar um intervalo (início e fim) de índices onde um determinado valor pode
      estar em uma lista que permite duplicatas.

7. **Aplicação em Dados Ordenados Decrescentes**:
    - Adapte a busca binária para funcionar em uma lista ordenada em ordem decrescente.

8. **Busca com Recurosão**:
    - Implemente a busca binária utilizando recursão em vez de um loop `while`.

9. **Análise de Complexidade**:
    - Explique e demonstre, através de exemplos, como a complexidade de tempo da busca binária é O(log n) em comparação
      com a busca linear, que é O(n).

10. **Aplicação Prática**:
    - Use a busca binária para resolver um problema prático, como encontrar a raiz quadrada inteira de um número inteiro
      dado. Por exemplo, para um número `x`, encontre o maior inteiro `y` tal que `y^2 <= x`.

### Soluções Sugeridas

Aqui estão algumas direções para resolver cada exercício:

1. **Implementação Básica**:
    - Refaça a implementação básica fornecida anteriormente.

2. **Verificação de Elementos Não Existentes**:
   ```python
   def busca_binaria(lista, alvo):
       inicio = 0
       fim = len(lista) - 1
       while inicio <= fim:
           meio = (inicio + fim) // 2
           if lista[meio] == alvo:
               return f"Elemento encontrado no índice: {meio}"
           elif lista[meio] < alvo:
               inicio = meio + 1
           else:
               fim = meio - 1
       return "Elemento não encontrado na lista."
   ```

3. **Busca em Lista de Strings**:
    - Apenas substitua a lista de inteiros por uma lista de strings e mantenha o mesmo algoritmo.

4. **Contagem de Comparações**:
   ```python
   def busca_binaria(lista, alvo):
       inicio = 0
       fim = len(lista) - 1
       comparacoes = 0
       while inicio <= fim:
           comparacoes += 1
           meio = (inicio + fim) // 2
           if lista[meio] == alvo:
               return meio, comparacoes
           elif lista[meio] < alvo:
               inicio = meio + 1
           else:
               fim = meio - 1
       return -1, comparacoes
   ```

5. **Busca em Lista de Tuplas**:
   ```python
   def busca_binaria(lista, alvo):
       inicio = 0
       fim = len(lista) - 1
       while inicio <= fim:
           meio = (inicio + fim) // 2
           if lista[meio][0] == alvo:
               return meio
           elif lista[meio][0] < alvo:
               inicio = meio + 1
           else:
               fim = meio - 1
       return -1
   ```

6. **Intervalo de Busca**:
   ```python
   def busca_binaria_intervalo(lista, alvo):
       inicio = 0
       fim = len(lista) - 1
       primeiro = -1
       ultimo = -1

       while inicio <= fim:
           meio = (inicio + fim) // 2
           if lista[meio] == alvo:
               primeiro = meio
               fim = meio - 1
           elif lista[meio] < alvo:
               inicio = meio + 1
           else:
               fim = meio - 1

       inicio = 0
       fim = len(lista) - 1

       while inicio <= fim:
           meio = (inicio + fim) // 2
           if lista[meio] == alvo:
               ultimo = meio
               inicio = meio + 1
           elif lista[meio] < alvo:
               inicio = meio + 1
           else:
               fim = meio - 1

       return (primeiro, ultimo)
   ```

7. **Aplicação em Dados Ordenados Decrescentes**:
   ```python
   def busca_binaria_decrescente(lista, alvo):
       inicio = 0
       fim = len(lista) - 1
       while inicio <= fim:
           meio = (inicio + fim) // 2
           if lista[meio] == alvo:
               return meio
           elif lista[meio] > alvo:
               inicio = meio + 1
           else:
               fim = meio - 1
       return -1
   ```

8. **Busca com Recursão**:
   ```python
   def busca_binaria_recursiva(lista, alvo, inicio=0, fim=None):
       if fim is None:
           fim = len(lista) - 1
       if inicio > fim:
           return -1
       meio = (inicio + fim) // 2
       if lista[meio] == alvo:
           return meio
       elif lista[meio] < alvo:
           return busca_binaria_recursiva(lista, alvo, meio + 1, fim)
       else:
           return busca_binaria_recursiva(lista, alvo, inicio, meio - 1)
   ```

9. **Análise de Complexidade**:
    - Forneça exemplos e gráficos que mostrem a diferença na complexidade de tempo entre busca linear e busca binária.

10. **Aplicação Prática**:
   ```python
   def raiz_quadrada_inteira(x):
       if x < 2:
           return x
       inicio, fim = 2, x // 2
       while inicio <= fim:
           meio = (inicio + fim) // 2
           quadrado = meio * meio
           if quadrado == x:
               return meio
           elif quadrado < x:
               inicio = meio + 1
           else:
               fim = meio - 1
       return fim
   ```

Esses exercícios cobrem uma variedade de aspectos da busca binária e ajudam a reforçar o entendimento do algoritmo e
suas aplicações.