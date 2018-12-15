from collections import defaultdict
from string import ascii_uppercase

# CABFDE = 15 seconds
# 436 Too Low
# filename = 'practice.txt'
# num_workers = 2
# base_seconds = 0
filename = 'workfile.txt'
num_workers = 5
base_seconds = 60

pres = set()
posts = set()
graph = defaultdict(list)
rev_graph = defaultdict(list)
done = []
in_progress = []
to_do = set()
workers = []
current_tick = 0


def get_duration(letter):
    return base_seconds + ascii_uppercase.index(letter) + 1


def free_worker():
    for w in workers:
        if len(w) == 0:
            return w
    return None


def all_free():
    for w in workers:
        if len(w) > 0:
            return True
    return False


def tick():
    print(f'ticking {workers}')
    new_roots = []
    for w in workers:
        if len(w) > 1:
            w.remove(w[0])
        elif len(w) == 1:
            letter = w[0]
            new_roots.extend(graph[letter])
            in_progress.remove(letter)
            w.remove(letter)
            to_do.remove(letter)
            print(f'done {letter}')

    if len(new_roots) > 0:
        print(f'ticked {new_roots}')
    return new_roots


def assign_work(w, letter):
    in_progress.append(letter)
    w.extend([letter] * get_duration(letter))
    # print(f'work assigned: {workers}')


def any_letters_ready():
    for val in to_do:
        finished = True
        for node in rev_graph[val]:
            if node in in_progress:
                finished = False
            if node not in done:
                finished = False
        if finished:
            return True
    return False


def next_roots(roots, new_roots):
    roots_extend = roots.extend(new_roots)
    if roots_extend is None:
        if len(roots) > 0:
            roots_extend = roots
        elif len(new_roots) > 0:
            roots_extend = new_roots
        else:
            roots_extend = []
    return roots_extend


def process(roots, time):
    orig_size = len(roots)
    while len(roots) == 0:
        if len(to_do) == 0:
            return time, ''
        time += 1
        roots.extend(tick())

    new_roots = []
    while free_worker() is None:
        time += 1
        new_roots.extend(tick())

    roots.sort()
    root = None
    for check in roots:
        ready = True
        for node in rev_graph[check]:
            if node not in done:
                ready = False
        if ready:
            root = check
            break

    result = ''
    if root is not None:
        roots.remove(root)
        if root not in done:
            assign_work(free_worker(), root)
            result = root
            done.append(root)

    roots = next_roots(roots, new_roots)
    while any_letters_ready() and free_worker() is not None and len(roots) == orig_size:
        new_roots = tick()
        roots = next_roots(roots, new_roots)
        time += 1

    recurse = process(roots, time)
    return recurse[0], result + recurse[1]


with open(filename, 'r') as file:
    for line in file:
        words = line.split()
        pre = words[1]
        post = words[7]
        pres.add(pre)
        posts.add(post)
        to_do.add(pre)
        to_do.add(post)
        graph[pre].append(post)
        rev_graph[post].append(pre)

print(graph)

for id in range(0, num_workers):
    worker = []
    workers.append(worker)

roots = list(pres.difference(posts))
print(f'difference: {roots}')
answer = process(roots, 1)
print(f'answer {answer}')
print(current_tick)
