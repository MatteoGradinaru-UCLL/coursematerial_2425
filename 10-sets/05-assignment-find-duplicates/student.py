def find_duplicates(xs):
    
    seen = set()
    duplicates = set()
    
    for x in xs:
        if x in seen:
            duplicates.add(x)
        else:
            seen.add(x)
    
    return list(duplicates)

print(find_duplicates([1, 2, 1, 3, 2, 1, 1]))