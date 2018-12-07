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
        for y in range(0, max_y + 1):
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
        for y in range(0, max_y + 1):
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
    #doesn't appear to be hitting all keys for a given generation
    for coord in generations_grid.keys():
        if generations_grid[coord] != generation:
            continue
        print(generation, coord)

        size = len(generations_grid)
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
        print_map(id, growth_map)

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
        break


grid_print()
grow(grid)
grid_print()
