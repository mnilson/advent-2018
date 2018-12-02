frequencies = set()
current = 0
frequencies.add(current)

with open('workfile1', 'r') as file:
    total_two_count = 0
    total_three_count = 0

    for word in file:
        letters = {}
        for letter in word:
            if letter in letters:
                letters[letter] = letters[letter] + 1
            else:
                letters[letter] = 1

        two_count = False
        three_count = False
        for key in letters:
            if letters[key] == 2:
                two_count = True
            elif letters[key] == 3:
                three_count = True

            if two_count and three_count:
                break

        print(f"Word: {word} two={two_count} three={three_count}")

        if two_count:
            total_two_count += 1
        if three_count:
            total_three_count += 1

    print(f"Totals: 2={total_two_count} 3={total_three_count}")
    result = total_three_count * total_two_count
    print(f"Result: {result}")