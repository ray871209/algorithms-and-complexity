"""Stable counting sort of non-negative integers with a modest value domain."""

def counting_sort(values: list[int], max_value: int = 10000) -> list[int]:
    if max_value < 0:
        raise ValueError("max_value must be non-negative")
    if any(type(value) is not int or value < 0 or value > max_value for value in values):
        raise ValueError("Input values must be integers in the supported range")
    counts = [0] * (max(values, default=0) + 1)
    for number in values:
        counts[number] += 1
    return [number for number, count in enumerate(counts) for _ in range(count)]
