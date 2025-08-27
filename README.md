# Implementação do Algoritmo de Karatsuba em Python

## Descrição do projeto

Este projeto apresenta uma implementação em Python do algoritmo de Karatsuba. O código foi estruturado de forma modular e orientada a objetos, encapsulando a lógica de multiplicação dentro da classe `KaratsubaMultiplier`.

O algoritmo utiliza uma abordagem de **dividir para conquistar** para multiplicar números inteiros grandes com uma complexidade assintótica melhor do que o método de multiplicação tradicional. O script principal é interativo, permitindo ao usuário fornecer seus próprios números para o cálculo.

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

A complexidade ciclomática do método `_recursive_multiply` é **2**. Isso significa que existem 2 caminhos linearmente independentes no grafo de fluxo de controle, como pode ser visto no diagrama abaixo.

**Diagrama do Grafo de Fluxo:**

![Diagrama do Grafo de Fluxo](../artefatos/trabalho-individual-1-FPAA-diagramaDeFluxo.png)

#### Análise dos Caminhos de Execução

Com base no grafo, identificamos os 2 caminhos independentes que uma execução pode seguir:

*   **Caminho 1: O Caso Base (N1 → N2 → N3 → N7)**
    *   Este caminho é executado quando a condição `x < 10 or y < 10` é **verdadeira**.
    *   O fluxo é o mais curto possível: a função realiza uma multiplicação simples e retorna o valor imediatamente, sem executar nenhuma chamada recursiva.

*   **Caminho 2: O Passo Recursivo (N1 → N2 → N4 → N5 → N6 → N7)**
    *   Este caminho é executado quando a condição `x < 10 or y < 10` é **falsa**.
    *   O fluxo executa a lógica completa do algoritmo de Karatsuba: divide os números em partes menores (N4), realiza três chamadas recursivas a si mesmo para calcular os subprodutos (N5) e, finalmente, combina esses resultados para obter o produto final (N6) antes de retornar.

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