words = set([w.lower() for w in open("/usr/share/dict/american-english", "r" ).read().split('\n') if len(w) > 2])

def letters_to_word(letters):
    include = []
    dont_include = False
    for word in words:
        word = word.lower()
        new_list = []
        for l in letters:
            new_list.append(l)
        copy = ''.join([w for w in word])
        for c in word:
            try:
                new_list.pop(new_list.index(c))
            except:
                dont_include = True
                break
        if not dont_include:
            include.append(copy)
        dont_include = False
        output = [[len(w), w] for w in include]
        output.sort()
    for o in output:
        print(o[1])
    print(len(output), "results")


while True:
    print("----------")
    lettres = input("which letters?\n")
    print("----------")
    letters_to_word(lettres)
