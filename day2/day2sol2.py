frequencies = set()
current = 0
frequencies.add(current)


def print_result(word1, word2):
    result = ""
    for ix, letter1 in enumerate(word1):
        if word2[ix:ix+1] == letter1:
            result += letter1
    print(f"Result: {result}")


with open('workfile2', 'r') as file:
    words = []

    for word in file:
        words.append(word)

    words.sort()

    for word_ix, word1 in enumerate(words):
        sublist = words[word_ix + 1:]
        for word2 in sublist:
            miss = False
            double_miss = False
            for ix, letter1 in enumerate(word1):
                if letter1 != word2[ix]:
                    if miss:
                        double_miss = True
                        break
                    miss = True

            if not double_miss:
                print_result(word1, word2)
                exit(0)
