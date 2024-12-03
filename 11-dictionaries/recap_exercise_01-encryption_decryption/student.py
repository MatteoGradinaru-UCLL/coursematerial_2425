# write your code here
def decode1(word):

    new_word = ""
    for char in word:
        if char == "A":
            new_word += "o"
        else:
            new_word += char
    return new_word
print(decode1("SchAAL"))


def decode2(word):

    new_word = ""
    for i in range(0, len(word), 2):
        new_word += word[i]
    return new_word
print(decode2("hqovtzdpozgm"))


def decode3(sentence):

    words = sentence.split()
    if len(words) > 0:
        words[0] = words[0][::-1]
    return ' '.join(words)
print(decode3("sepocseleT are too expensive."))


def decode4(word):

    new_word = ""
    if len(word) >= 3:
        for i in word[2:(len(word)//2)+2]:
            new_word += i 
    elif len(word) == 2:
        new_word = word[2:]
    elif len(word) == 1:
        new_word = word[1:]
    return new_word
print(decode4("oddolfijnnjifl"))


def decode5(sentence):

    #Strategy 1
    sentence = decode1(sentence)

    #Strategy 2
    words = sentence.split()
    new_words = [decode2(word) for word in words]
    sentence = ' '.join(new_words)

    #Strategy 4
    words = sentence.split()
    new_words = [decode4(word) for word in words]
    sentence = ' '.join(new_words)

    
    
    #Strategy 3
    sentence = decode3(sentence)
    
    return sentence


print(decode5("MDEneEdU oAXnkgaCteJE vMtokdrHarpltSKuspcc aaaudAev xzsRkVrSoDlolMernyFZpRHQDdkX QggivNajnoQU youKdSeq lnegtwrvatpeXeUu"))
print(decode5("rAxNejhfTrns maGwcaifrIcRuEmzsHtxaUnVcSeWsllKnmsYiMiFwQpMZyRhabPu aHhPhyajvfeViSYg xrfAcphhadnqgIeodAAXyDjTcFGT"))