# Implementação do Algoritmo de Karatsuba em Python

## Descrição do projeto

Este projeto apresenta uma implementação em Python do algoritmo de Karatsuba. O código foi estruturado de forma modular e orientada a objetos, encapsulando a lógica de multiplicação dentro da classe `KaratsubaMultiplier`.

O algoritmo utiliza uma abordagem de **dividir para conquistar** para multiplicar números inteiros grandes com uma complexidade assintótica melhor do que o método de multiplicação tradicional. O script principal é interativo, permitindo ao usuário fornecer seus próprios números para o cálculo.

### Lógica do Algoritmo

A lógica principal está no método privado `_recursive_multiply`, que segue os seguintes passos:

1.  **Caso Base**: A recursão para quando os números `x` ou `y` são menores que 10.
2.  **Divisão dos Números**: Os números são divididos em duas metades (`a`, `b` para `x`; `c`, `d` para `y`).
3.  **Chamadas Recursivas**: O algoritmo faz três chamadas recursivas para calcular os produtos `ac`, `bd` e um termo combinado `(a+b)*(c+d)`.
4.  **Combinação dos Resultados**: Os resultados são combinados usando a fórmula de Karatsuba para formar o produto final.

## Como executar o projeto

1.  Clone este repositório para sua máquina local.
2.  Navegue até a pasta do projeto.
3.  Execute o arquivo `main.py` usando o Python.
    ```bash
    python main.py
    ```
4.  O script iniciará em **modo interativo**. Ele solicitará que o usuário digite dois números inteiros. Após a entrada, o programa exibirá o resultado do cálculo, uma verificação de correção e a análise de complexidade teórica do algoritmo.

## Relatório Técnico

### Análise da Complexidade Ciclomática

A análise de complexidade ciclomática foca no método `_recursive_multiply`, que contém a lógica central do algoritmo. Usamos a fórmula `M = E - N + 2P`, resultando em uma complexidade de **2**, que representa o caminho do caso base e o caminho recursivo.

### Análise da Complexidade Assintótica

#### Complexidade Temporal

A relação de recorrência para o algoritmo é `T(n) = 3 * T(n/2) + O(n)`. Pelo **Teorema Mestre**, a complexidade temporal é:
**`O(n^log2(3))`** ≈ **`O(n^1.585)`**.

#### Complexidade Espacial

A profundidade da pilha de recursão determina a complexidade espacial, que é **`O(log n)`**.

#### Análise de Casos

O desempenho do algoritmo depende apenas do número de dígitos (`n`) da entrada, não dos valores.

*   **Melhor Caso**: `O(n^1.585)`
*   **Caso Médio**: `O(n^1.585)`
*   **Pior Caso**: `O(n^1.585)`
