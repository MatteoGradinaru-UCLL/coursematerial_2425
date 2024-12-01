def count_lines_in_file(path):
    
    with open(path, 'r', encoding='utf-8') as textfile:
        return len(textfile.readlines())

print(count_lines_in_file("test.txt"))