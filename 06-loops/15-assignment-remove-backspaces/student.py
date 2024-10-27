def remove_backspaces(string):
    result = ""
    
    for char in string:
        if char == '\b':
            if len(result) > 0:
                result = result[:-1]
        else:
            result += char
    return result

print(remove_backspaces("abc"))