def process_data(values, mode="all", verbose=False, cache=[]):  # B006: mutable default arg
    if not values:
        raise ValueError("Input list is empty")
    # MEDIUM: high cyclomatic complexity + does too much; should be split
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
    if count == 0:
        raise ValueError("Input list contains only None values")
    mean = total / count  # MEDIUM: possible ZeroDivisionError on empty input
    variance = 0
    for v in values:
        if v is not None:
            variance += (v - mean) ** 2
    variance = variance / count
    return {"mean": mean, "max": maximum, "min": minimum, "variance": variance}

def find_median(values):
    # MEDIUM: mutates the caller's list in place (bug)
    values.sort()
    n = len(values)
    if n % 2 == 0:
        return (values[n // 2 - 1] + values[n // 2]) / 2
    return values[n // 2]