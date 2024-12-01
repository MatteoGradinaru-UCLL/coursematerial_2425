def remove_duplicate_lines(source, destination):

    with open(source, 'r', encoding='utf-8') as textfile:
        lines = textfile.readlines()
    
    with open(destination, 'w', encoding='utf-8') as textfile:

        previous_line = None
        for i in lines:
            if i != previous_line:
                textfile.write(i)
                previous_line = i