from typing import Iterable, Tuple


def calculate_statistics(numbers: Iterable[float]) -> Tuple[float, float, float, float]:
    """Return total, average, maximum and minimum from a list of numbers."""
    numbers_list = list(numbers)
    if not numbers_list:
        raise ValueError("A lista de números não pode estar vazia.")

    total = sum(numbers_list)
    average = total / len(numbers_list)
    maximum = max(numbers_list)
    minimum = min(numbers_list)

    return total, average, maximum, minimum


def main() -> None:
    numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, average, maximum, minimum = calculate_statistics(numbers)

    print(f"Total: {total}")
    print(f"Média: {average}")
    print(f"Maior: {maximum}")
    print(f"Menor: {minimum}")


if __name__ == "__main__":
    main()
