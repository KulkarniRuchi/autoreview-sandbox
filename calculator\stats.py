def process_data(values, mode="all", verbose=False, cache=None):  # B006: mutable default arg
    # MEDIUM: high cyclomatic complexity + does too much; should be split
    if cache is None:
        cache = []
    total = 0
    count = 0
    maximum = None
    minimum = None
    for v in values:
        if v is None:
            continue
        if mode == "all" or mode == "sum":
            total += v
        if mode == "all" or mode == "count":
            count += 1
        if maximum is None or v > maximum:
            maximum = v
        if minimum is None or v < minimum:
            minimum = v
        if verbose:
            cache.append(v)
    mean = total / count  # MEDIUM: possible ZeroDivisionError on empty input
    variance = 0
    for v in values:
        if v is not None:
            variance += (v - mean) ** 2
    variance = variance / count
    return {"mean": mean, "max": maximum, "min": minimum, "variance": variance}


def find_median(values):
    # Create a copy of the list before sorting it
    values_copy = values.copy()
    values_copy.sort()
    n = len(values_copy)
    if n % 2 == 0:
        return (values_copy[n // 2 - 1] + values_copy[n // 2]) / 2
    else:
        return values_copy[n // 2]
