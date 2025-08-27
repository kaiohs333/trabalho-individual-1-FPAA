
class KaratsubaMultiplier:
    """
    Encapsula a lógica de multiplicação de inteiros grandes usando o
    algoritmo de Karatsuba, seguindo uma abordagem orientada a objetos.
    """

    def multiply(self, x: int, y: int) -> int:
        """
        Interface pública para multiplicar dois números inteiros.

        Args:
            x: O primeiro número.
            y: O segundo número.

        Returns:
            O produto de x e y.
        """
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Ambas as entradas devem ser inteiros.")
        if x < 0 or y < 0:
            raise ValueError("Este método suporta apenas inteiros não-negativos.")

        return self._recursive_multiply(x, y)

    def _recursive_multiply(self, x: int, y: int) -> int:
        """
        Implementa a lógica recursiva de Karatsuba.
        """
        if x < 10 or y < 10:
            return x * y

        n = max(len(str(x)), len(str(y)))
        n2 = n // 2

        power_of_10_n2 = 10**n2
        a = x // power_of_10_n2
        b = x % power_of_10_n2
        c = y // power_of_10_n2
        d = y % power_of_10_n2

        ac = self._recursive_multiply(a, c)
        bd = self._recursive_multiply(b, d)
        ad_plus_bc = self._recursive_multiply(a + b, c + d) - ac - bd

        return (ac * 10**(2 * n2)) + (ad_plus_bc * power_of_10_n2) + bd


def main():
    """
    Função principal para demonstrar o uso interativo do KaratsubaMultiplier.
    """
    print("--- Calculadora de Multiplicação Karatsuba ---")

    try:
        num1_str = input("Digite o primeiro número inteiro: ")
        num2_str = input("Digite o segundo número inteiro: ")
        num1 = int(num1_str)
        num2 = int(num2_str)
    except ValueError:
        print("\nErro: Por favor, digite apenas números inteiros válidos.")
        return

    multiplier = KaratsubaMultiplier()
    resultado = multiplier.multiply(num1, num2)
    resultado_python = num1 * num2

    print("\n--- Resultados ---")
    print(f"Número 1: {num1}")
    print(f"Número 2: {num2}")
    print(f"Resultado com Karatsuba: {resultado}")
    print(f"Resultado com Python:   {resultado_python}")
    print(f"Resultados são iguais?  {resultado == resultado_python}")

    print("\n--- Análise de Complexidade Teórica do Algoritmo ---")
    complexidade = "O(n^log2(3)) ≈ O(n^1.585)"
    print(f"Melhor Caso: {complexidade}")
    print(f"Caso Médio:  {complexidade}")
    print(f"Pior Caso:   {complexidade}")
    print("(Independente dos valores de entrada, apenas do número de dígitos 'n'.)")


if __name__ == "__main__":
    main()

