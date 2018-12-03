fabric = {}
with open('workfile1', 'r') as file:
    for chunk in file:
        # #1 @ 1,3: 4x4
        chunk = chunk.replace('\n', '')
        items = chunk.split(" ")
        id = items[0]
        start_coords = items[2]
        length_width = items[3]
        width = int(length_width.split('x')[0]);
        length = int(length_width.split('x')[1]);
        side = int(start_coords.split(',')[0]);
        top = int(start_coords.split(',')[1].replace(":", ""));
        #print(f"{id} = {side} {top} {length} {width}")

        for w in range(side, side+width):
            for h in range(top, top+length):
                key = f"{w},{h}"
                if key in fabric:
                    fabric[key] = 'x'
                else:
                    fabric[key] = id

        #print(fabric)


    counter = 0
    for key, elem in fabric.items():
        if elem == 'x':
            counter += 1

    print(f"result: {counter}")

