frequencies = set()
current = 0
frequencies.add(current)

while(True):
    with open('workfile', 'r') as file:
        for adjustment in file:
            adjustment = adjustment.split(',')[0]
            current += int(adjustment)
            #print(str(adjustment) + " " + str(current) + " " + str(frequencies))
            if current in frequencies:
                print("result: " + str(current))
                exit(0)
            else:
                frequencies.add(current)