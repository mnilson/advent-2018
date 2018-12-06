from string import ascii_uppercase

infinite = set()
grid = {}
coordinates = {}
lower = (0,0)
max_x = 0
max_y = 0

def grid_print():
    print('*' * max_x)
    print(f'0:0 - {max_x}:{max_y}')
    print('*' * max_x)
    for x in range(0, max_x + 1):
        row = ''
        for y in range(0, max_y + 1):
            if (x, y) in grid:
                row += grid[(x, y)]
            else:
                row += '-'
        print(row)

def grow_single(id, coord, growth):
    x = coord[0]
    y = coord[1]
    if x < 0 or y < 0 or x > max_x or y > max_y:
        infinite.add(id)
        return growth
    if coord in grid:
        return growth
    print(f"{coord} {growth} {id}")
    if coord not in growth or growth[coord].lower() == id.lower():
        growth[coord] = id
    else:
        # this doesn't work - I think I need to grow all coordinates from a given seed and then put . where there are overlapping generation values at a given coordinate
        growth[coord] = '.'
    return growth


def grow(seed_growth):
    current_growth = {}
    for coord, id in seed_growth.items():
        if id == '.':
            continue
        grow_id = id.lower()
        # grow left
        grow_coord = (coord[0]-1, coord[1])
        current_growth = grow_single(grow_id, grow_coord, current_growth)
        # grow right
        grow_coord = (coord[0] + 1, coord[1])
        current_growth = grow_single(grow_id, grow_coord, current_growth)
        # grow up
        grow_coord = (coord[0], coord[1] - 1)
        current_growth = grow_single(grow_id, grow_coord, current_growth)
        # grow down
        grow_coord = (coord[0], coord[1] + 1)
        current_growth = grow_single(grow_id, grow_coord, current_growth)

    if current_growth is None or len(current_growth) == 0:
        return
    else:
        for key, val in current_growth.items():
            grid[key] = val
        grow(current_growth)
        print(grid)


with open('practice.txt', 'r') as file:
    for num, line in enumerate(file):
        coords = line.split(", ")
        x = int(coords[0])
        y = int(coords[1].replace('\n', ''))
        if x >= max_x:
            max_x = x+1
        if y >= max_y:
            max_y = y+1

        coordinates[ascii_uppercase[num]] = (y, x)
        grid[(y, x)] = ascii_uppercase[num]


grid_print()
grow(grid)
grid_print()
