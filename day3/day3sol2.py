fabric = {}
overlaps = set()
ids = set()
with open('workfile1', 'r') as file:
    for chunk in file:
        # #1 @ 1,3: 4x4
        chunk = chunk.replace('\n', '')
        items = chunk.split(" ")
        id = items[0]
        ids.add(id)
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
                    overlaps.add(id)
                    overlaps.add(fabric[key])
                    fabric[key] = 'x'
                else:
                    fabric[key] = id

        #print(fabric)

    res = [item for item in ids if item not in overlaps]

    idsize = len(ids)
    os = len(overlaps)
    print(f"overlaps size: {os} ids size {idsize}")
    print(f"overlaps: {overlaps} ids: {ids}")
    print(f"result: {res}")

