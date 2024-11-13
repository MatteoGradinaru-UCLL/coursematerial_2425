def remove_all(xs, item_to_remove):

    while item_to_remove in xs:
        xs.remove(item_to_remove)

xs = [1, 2, 3, 2, 1]
remove_all(xs, 2)
print(xs)