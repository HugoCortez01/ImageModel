from collections.abc import Sequence
from typing import NamedTuple


class Statistics(NamedTuple):
    total: float
    average: float
    maximum: float
    minimum: float


def calculate_statistics(numbers: Sequence[float]) -> Statistics:
    """Return statistics for a non-empty sequence of numbers."""
    values = list(numbers)
    if not values:
        raise ValueError("A lista de números não pode estar vazia.")

    total = sum(values)
    average = total / len(values)
    maximum = max(values)
    minimum = min(values)

    return Statistics(total=total, average=average, maximum=maximum, minimum=minimum)


def display_statistics(statistics: Statistics) -> None:
    """Print the calculated statistics in a readable format."""
    print(f"Total: {statistics.total}")
    print(f"Média: {statistics.average}")
    print(f"Maior: {statistics.maximum}")
    print(f"Menor: {statistics.minimum}")


def main() -> None:
    sample_numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    statistics = calculate_statistics(sample_numbers)
    display_statistics(statistics)


if __name__ == "__main__":
    main()
