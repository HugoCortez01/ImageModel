def is_prime(n: int) -> bool:
    """Verifica se um número é primo.

    Args:
        n (int): O número inteiro a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.
    """
    if n <= 1:
        return False
    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            return False
    return True


def request_integer(prompt: str = "Digite um número inteiro: ") -> int:
    """Ask the user for an integer until a valid response is provided."""
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Entrada vazia. Tente novamente.")
            continue
        try:
            return int(user_input)
        except ValueError:
            print("Valor inválido. Digite um número inteiro, por favor.")


def main() -> None:
    """Read a number from the user and print whether it is prime."""
    number = request_integer()
    result = "é primo" if is_prime(number) else "não é primo"
    print(f"O número {number} {result}.")


if __name__ == "__main__":
    main()
