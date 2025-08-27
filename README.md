# Multiplicador Karatsuba em Python

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)

> Projeto acadêmico para a disciplina de Fundamentos de Projeto e Análise de Algoritmos, demonstrando a implementação do algoritmo de multiplicação de Karatsuba com uma abordagem didática e interativa.

---

### 📖 Índice

*   [O Problema da Multiplicação](#o-problema-da-multiplicação-de-números-grandes)
*   [Sobre o Algoritmo de Karatsuba](#sobre-o-algoritmo-de-karatsuba)
*   [✨ Features](#-features)
*   [🛠️ Tecnologias utilizadas](#️-tecnologias-utilizadas)
*   [🚀 Como executar o projeto](#-como-executar-o-projeto)
*   [📊 Relatório Técnico](#-relatório-técnico)
*   [👨‍💻 Autor](#-autor)

---

## O Problema da Multiplicação de Números Grandes

A multiplicação de inteiros é uma operação fundamental na computação. O método que aprendemos na escola, conhecido como multiplicação longa, possui uma complexidade de `O(n²)`, onde `n` é o número de dígitos. Para números pequenos, isso é perfeitamente aceitável. No entanto, em domínios como **criptografia** (ex: RSA), **computação científica** e **cálculos de alta precisão**, onde é necessário manipular números com milhares ou milhões de dígitos, uma complexidade quadrática se torna um gargalo de performance proibitivo. Algoritmos como o de Karatsuba foram desenvolvidos para quebrar essa barreira, oferecendo uma solução significativamente mais rápida.

## Sobre o Algoritmo de Karatsuba

Proposto por Anatolii Karatsuba em 1960, este algoritmo utiliza uma estratégia de **Dividir para Conquistar** para reduzir o número de multiplicações recursivas necessárias. A ideia central é transformar uma multiplicação de `n` dígitos em três multiplicações de `n/2` dígitos, em vez das quatro que seriam necessárias pelo método tradicional.

Dados dois números `x` e `y` de `n` dígitos, nós os dividimos em duas partes:

`x = a * 10^(n/2) + b`
`y = c * 10^(n/2) + d`

O produto `x*y` é então:
`x*y = (ac) * 10^n + (ad + bc) * 10^(n/2) + bd`

O truque de Karatsuba está em calcular o termo do meio, `ad + bc`, com apenas uma multiplicação adicional:

1.  `z2 = ac` (1ª multiplicação)
2.  `z0 = bd` (2ª multiplicação)
3.  `z1 = (a+b)(c+d) - z2 - z0` (3ª multiplicação)

O resultado final é `z2 * 10^n + z1 * 10^(n/2) + z0`. Essa redução de 4 para 3 multiplicações recursivas é a fonte de sua maior eficiência assintótica.

---

## ✨ Features

*   **Implementação Orientada a Objetos**: Lógica encapsulada na classe `KaratsubaMultiplier`.
*   **Entrada Interativa**: Permite que o usuário forneça os números a serem multiplicados.
*   **Validação de Correção**: Compara o resultado do algoritmo com a multiplicação nativa do Python.
*   **Análise de Complexidade na Saída**: Exibe a análise teórica de complexidade (melhor, médio e pior caso) ao final da execução.

---

## 🛠️ Tecnologias utilizadas

*   **[Python 3](https://www.python.org/)**: Linguagem de programação escolhida por sua clareza, tipagem dinâmica e capacidade de lidar com números inteiros arbitrariamente grandes (`BigInt`).
*   **[PlantUML](https://plantuml.com/)**: Ferramenta utilizada para a modelagem e criação do diagrama de fluxo de controle, permitindo a geração de diagramas a partir de texto.

---

## 🚀 Como executar o projeto

### Pré-requisitos

*   **Python 3.x** instalado em sua máquina.

### Passos

1.  Clone o repositório:
    ```bash
    git clone https://github.com/kaiohs333/trabalho-individual-1-FPAA.git
    ```
2.  Navegue até a pasta do código:
    ```bash
    cd trabalho-individual-1-FPAA/codigo
    ```
3.  Execute o script principal:
    ```bash
    python main.py
    ```
4.  O programa solicitará a entrada de dois números inteiros e, em seguida, exibirá o resultado e as análises.

---

## 📊 Relatório Técnico

### Análise da Complexidade Ciclomática

A complexidade ciclomática de um fluxo de controle é calculada pela fórmula `M = E - N + 2P`. Para o método `_recursive_multiply`, temos:
*   `E` (Arestas) = 5
*   `N` (Nós) = 5
*   `P` (Componentes Conexos) = 1

`M = 5 - 5 + 2 * 1 = 2`

Uma complexidade de **2** indica que há dois caminhos independentes no código: o caso base e o passo recursivo.

**Diagrama do Grafo de Fluxo:**

(https://github.com/kaiohs333/trabalho-individual-1-FPAA/blob/main/artefatos/trabalho-individual-1-FPAA-diagramaDeFluxo.png)

### Análise da Complexidade Assintótica

A grande vantagem do Algoritmo de Karatsuba reside em sua complexidade temporal.

| Algoritmo | Complexidade Temporal | Análise para n = 1024 dígitos |
| :--- | :--- | :--- |
| **Multiplicação Clássica** | `O(n²)` | `1024² ≈ 1.048.576` operações |
| **Algoritmo de Karatsuba** | `O(n^log2(3)) ≈ O(n^1.585)` | `1024^1.585 ≈ 59.049` operações |

Como a tabela ilustra, para um número de 1024 dígitos, Karatsuba é aproximadamente **17 vezes mais rápido**. Essa vantagem cresce exponencialmente com o aumento de `n`.

*   **Complexidade Espacial**: `O(log n)`, devido à profundidade da pilha de chamadas recursivas.

---

## 👨‍💻 Autor

*   **Kaio Henrique Oliveira da Silveira Barbosa**
*   **Email**: kaiohsilveira@gmail.com
