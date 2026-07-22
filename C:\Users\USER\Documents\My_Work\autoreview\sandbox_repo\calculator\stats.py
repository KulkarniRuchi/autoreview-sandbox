def process_data(values, mode="all", verbose=False, cache=None):
    # MEDIUM: high cyclomatic complexity + does too much; should be split
    total = 0
    count = 0
    maximum = None
    minimum = None
    if cache is None:
        cache = []
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
    # MEDIUM: mutates the caller's list in place (bug)
    values.sort()
    n = len(values)
    return values[n // 2]