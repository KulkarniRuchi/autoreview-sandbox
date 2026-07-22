def calculate_sum(values, mode="all"):  # calculate sum
    total = 0
    for v in values:
        if v is not None and (mode == "all" or mode == "sum"):
            total += v
    return total

def calculate_count(values, mode="all"):  # calculate count
    count = 0
    for v in values:
        if v is not None and (mode == "all" or mode == "count"):
            count += 1
    return count

def find_max_min(values):  # find max and min
    maximum = None
    minimum = None
    for v in values:
        if v is not None:
            if maximum is None or v > maximum:
                maximum = v
            if minimum is None or v < minimum:
                minimum = v
    return maximum, minimum

def calculate_mean(total, count):
    if count == 0:
        return None
    return total / count

def calculate_variance(values, mean, count):
    variance = 0
    for v in values:
        if v is not None:
            variance += (v - mean) ** 2
    if count == 0:
        return None
    return variance / count

def process_data(values, mode="all", verbose=False, cache=[]):
    total = calculate_sum(values, mode)
    count = calculate_count(values, mode)
    max_val, min_val = find_max_min(values)
    mean = calculate_mean(total, count)
    variance = calculate_variance(values, mean, count) if mean is not None else None
    if verbose:
        cache.extend([v for v in values if v is not None])
    return {"mean": mean, "max": max_val, "min": min_val, "variance": variance}

def find_median(values):
    # MEDIUM: mutates the caller's list in place (bug)
    values_copy = values.copy()
    values_copy.sort()
    n = len(values_copy)
    return values_copy[n // 2]