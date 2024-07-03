### Passo a Passo da Implementação da Busca Binária em Python

Vamos decompor a implementação da busca binária em Python em um guia de 10 etapas detalhadas:

1. **Definição da Função**
    ```python
    def busca_binaria(lista, alvo):
    ```
    - Definimos a função `busca_binaria` que recebe dois argumentos: `lista`, que é uma lista ordenada, e `alvo`, o valor que queremos encontrar.

2. **Inicialização dos Índices**
    ```python
    inicio = 0
    fim = len(lista) - 1
    ```
    - Inicializamos dois índices: `inicio`, que começa no início da lista (índice 0), e `fim`, que começa no último índice da lista (`len(lista) - 1`).

3. **Estrutura do Loop While**
    ```python
    while inicio <= fim:
    ```
    - Iniciamos um loop `while` que continua enquanto `inicio` for menor ou igual a `fim`. Isso garante que estamos examinando uma parte válida da lista.

4. **Cálculo do Índice do Meio**
    ```python
    meio = (inicio + fim) // 2
    ```
    - Calculamos o índice do meio da lista usando `(inicio + fim) // 2`. O operador `//` realiza uma divisão inteira, garantindo um valor inteiro como resultado.

5. **Comparação com o Alvo**
    ```python
    if lista[meio] == alvo:
    ```
    - Verificamos se o valor no índice `meio` é igual ao `alvo`. Se for, encontramos o valor e podemos retornar o índice `meio`.

6. **Retorno do Índice Encontrado**
    ```python
    return meio
    ```
    - Se `lista[meio]` for igual ao `alvo`, retornamos `meio` como o índice onde o alvo foi encontrado na lista.

7. **Verificação do Lado Direito**
    ```python
    elif lista[meio] < alvo:
        inicio = meio + 1
    ```
    - Se o valor no índice `meio` for menor que o `alvo`, ajustamos o índice `inicio` para `meio + 1`, descartando a metade esquerda da lista, pois sabemos que o alvo só pode estar na metade direita.

8. **Verificação do Lado Esquerdo**
    ```python
    else:
        fim = meio - 1
    ```
    - Se o valor no índice `meio` for maior que o `alvo`, ajustamos o índice `fim` para `meio - 1`, descartando a metade direita da lista, pois sabemos que o alvo só pode estar na metade esquerda.

9. **Loop Continuado**
    - O loop `while` continua, repetindo os passos 4 a 8, recalculando o `meio` e ajustando `inicio` ou `fim` até que `inicio` seja maior que `fim`.

10. **Retorno se o Alvo não for Encontrado**
    ```python
    return -1
    ```
    - Se o loop terminar e o alvo não tiver sido encontrado, retornamos -1 indicando que o alvo não está presente na lista.

### Código Completo

Aqui está o código completo novamente para referência:

```python
def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    
    return -1

# Exemplo de uso
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
alvo = 7
resultado = busca_binaria(lista, alvo)

if resultado != -1:
    print(f"Elemento encontrado no índice: {resultado}")
else:
    print("Elemento não encontrado na lista.")
```

### Conclusão

Este passo a passo detalhado explica como a busca binária funciona e como implementá-la em Python. Seguindo essas etapas, você deve ser capaz de entender e aplicar este algoritmo eficiente em suas próprias listas ordenadas.