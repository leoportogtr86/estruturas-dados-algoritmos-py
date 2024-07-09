# Busca Linear em Python

A **busca linear**, também conhecida como busca sequencial, é um dos algoritmos de busca mais simples. Como o nome sugere, ele percorre a lista de elementos de maneira sequencial, procurando pelo elemento desejado.

## Como funciona a Busca Linear?

A busca linear começa no primeiro elemento da lista e compara cada elemento com o valor que estamos procurando. Se o elemento atual for igual ao valor que estamos procurando, o algoritmo termina e retorna a posição do elemento. Se o algoritmo chegar ao final da lista sem encontrar o valor desejado, ele retorna uma indicação de que o valor não foi encontrado.

## Implementação em Python

Aqui está um exemplo simples de como você pode implementar a busca linear em Python:

```python
def busca_linear(lista, valor_desejado):
    for i in range(len(lista)):
        if lista[i] == valor_desejado:
            return i
    return -1
```

Neste código, a função `busca_linear` recebe uma lista e um `valor_desejado` como parâmetros. Ela percorre cada elemento da lista. Se encontrar o `valor_desejado`, retorna o índice desse elemento. Se não encontrar o `valor_desejado` após percorrer toda a lista, retorna `-1`.

## Exemplo de Uso

Vamos ver como usar essa função com um exemplo:

```python
numeros = [5, 3, 9, 1, 6, 8]
indice = busca_linear(numeros, 9)

if indice != -1:
    print(f"Valor encontrado no índice {indice}")
else:
    print("Valor não encontrado")
```

Neste exemplo, estamos procurando o número `9` na lista `numeros`. A função `busca_linear` retorna o índice do número `9`, que é `2`. Portanto, a saída do programa será `Valor encontrado no índice 2`.

Espero que este artigo tenha ajudado a entender melhor a busca linear e como implementá-la em Python. Se você tiver alguma dúvida ou comentário, fique à vontade para perguntar!
