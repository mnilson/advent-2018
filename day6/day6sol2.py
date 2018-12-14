filename = 'workfile.txt'
coordinates = {}
max_x = 0
max_y = 0
target = 10000
grid = {}

def print_grid():
    out = ""
    for x in range(0, max_x):
        for y in range(0, max_y):
            out += str(grid[(x,y)])
        out += '\n'
    print(out)


def abs_total(target_coord, coords):
    sum = 0
    for coord in coords:
        sum += abs(target_coord[0] - coord[0]) + abs(target_coord[1] - abs(coord[1]))
        if sum >= target:
            return 0
    return 1

with open(filename, 'r') as file:
    ix = 0
    for num, line in enumerate(file):
        coords = line.split(", ")
        x = int(coords[0])
        y = int(coords[1].replace('\n', ''))
        if x >= max_x:
            max_x = x+1
        if y >= max_y:
            max_y = y+1

        coordinates[(x, y)] = ix
        ix += 1

print(f'max-x:{max_x} max-y:{max_y}')

total = 0
for x in range(0, max_x):
    for y in range(0, max_y):
        val = abs_total((x, y), coordinates)
        grid[(x,y)] = val
        total += val

print(total)
#print_grid()



