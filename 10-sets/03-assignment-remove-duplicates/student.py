def remove_duplicates(xs):
    seen = set()
    result = []

    for item in xs:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result