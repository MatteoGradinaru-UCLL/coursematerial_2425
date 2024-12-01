def remove_empty_lines(source, destination):

    with open(source, "r", encoding="utf-8") as file:
        lines = file.read().split("\n")

    with open(destination, "w", encoding="utf-8") as file:
        file.writelines([x + "\n" for x in lines if x])

print(remove_empty_lines("input.txt", "output.txt"))