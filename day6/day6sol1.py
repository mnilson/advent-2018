from collections import defaultdict
from string import ascii_lowercase
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
        for y in range(0, max_y):
            if (x, y) in grid:
                row += grid[(x, y)]
            else:
                row += '-'
        print(row)


def print_map(id, map):
    print(('*' * max_x), id, ('*' * max_x))

    print(f'0:0 - {max_x}:{max_y}')
    print('*' * max_x)
    for x in range(0, max_x + 1):
        row = ''
        for y in range(0, max_y):
            if (x, y) in map:
                num = map[(x, y)]
                if num > 34:
                    num = ascii_uppercase[num - 34]
                elif num > 9:
                    num = ascii_lowercase[num - 9]
                else:
                    num = str(num)
                row += num
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


def grow_gen_coord(coord, generations_grid, generation):
    if coord in generations_grid:
        return generations_grid

    if coord[0] < 0 or coord[1] < 0 or coord[0] > max_x or coord[1] > max_y:
        return generations_grid

    generations_grid[coord] = generation
    return generations_grid


def grow_gen(generations_grid, generation):
    size = len(generations_grid)
    coordinates = list(generations_grid.keys())
    for coord in coordinates:
        if generations_grid[coord] != generation:
            continue

        grow_coord = (coord[0] - 1, coord[1])
        generations_grid = grow_gen_coord(grow_coord, generations_grid, generation + 1)

        grow_coord = (coord[0] + 1, coord[1])
        generations_grid = grow_gen_coord(grow_coord, generations_grid, generation + 1)

        grow_coord = (coord[0], coord[1] + 1)
        generations_grid = grow_gen_coord(grow_coord, generations_grid, generation + 1)

        grow_coord = (coord[0], coord[1] - 1)
        generations_grid = grow_gen_coord(grow_coord, generations_grid, generation + 1)

    if (len(generations_grid) == size):
        #did not grow / done
        return generations_grid
    else:
        return grow_gen(generations_grid, generation+1)

def grow(seed_growth):
    growth_maps = {}
    for coord, id in seed_growth.items():
        gen_zero = {}
        gen_zero[coord] = 0
        growth_map = grow_gen(gen_zero, 0)
        growth_maps[id] = growth_map
        # print_map(id, growth_map)

    for x in range (0, max_x+1):
        for y in range(0, max_y):
            best_id = ''
            best_value = 999999
            for id, growth_map in growth_maps.items():
                if growth_map[(x, y)] < best_value:
                    best_value = growth_map[(x, y)]
                    best_id = id
                elif growth_map[(x, y)] == best_value:
                    best_id = '.'
            if best_id == '.':
                grid[(x,y)] = best_id
            elif best_value > 0:
                grid[(x,y)] = best_id.lower()

    for x in range (0, max_x + 1):
        if grid[(x, 0)] == '.':
            continue
        else:
            infinite.add(grid[(x,0)].upper())

    for y in range (0, max_y):
        if grid[(0, y)] == '.':
            continue
        else:
            infinite.add(grid[(0,y)].upper())

    for x in range (0, max_x + 1):
        if grid[(x, max_y-1)] == '.':
            continue
        else:
            infinite.add(grid[(x,max_y-1)].upper())

    for y in range (0, max_y):
        if grid[(max_x, y)] == '.':
            continue
        else:
            infinite.add(grid[(max_x,y)].upper())

def calc_max():
    max_counts = {}
    for x in range (0, max_x + 1):
        for y in range(0, max_y):
            val = grid[(x, y)]
            if val == '.':
                continue
            if val in max_counts:
                max_counts[val] += 1
            else:
                max_counts[val] = 1
    return max_counts

with open('workfile.txt', 'r') as file:
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
print(infinite)
max_counts = calc_max()
print(max_counts)
for id, val in max_counts.items():
    if id.upper() in infinite:
        continue
    print(f'{id}={val}')

