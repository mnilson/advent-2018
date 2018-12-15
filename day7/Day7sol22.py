from collections import defaultdict
from string import ascii_uppercase

# CABFDE = 15 seconds
# 436 Too Low
filename = 'practice.txt'
num_workers = 2
base_seconds = 0
# filename = 'workfile.txt'
# num_workers = 5
# base_seconds = 60

pres = set()
posts = set()
graph = defaultdict(list)
rev_graph = defaultdict(list)
done = []
in_progress = set()
to_do = set()
workers = []
current_tick = 0


def get_duration(letter):
    return base_seconds + ascii_uppercase.index(letter) + 1


def any_free_workers():
    return free_worker() is not None


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


def tick(time):
    #print(f'ticking {time} {workers}')
    out = f'ticking {time} '
    all_bored = True
    for w in workers:
        if len(w) == 0:
            out += '.'
        if len(w) > 1:
            all_bored = False
            w.remove(w[0])
            out += f'{w[0]}'
        elif len(w) == 1:
            all_bored = False
            letter = w[0]
            out += f'{w[0]}'
            in_progress.remove(letter)
            w.remove(letter)
            done.append(letter)
            print(f'done {letter}')

    out_done = ' '
    for d in done:
        out_done += d

    print(out + out_done)
    if all_bored:
        print('Nothing Happening!!!')
        exit(1)


def assign_work(w, letter):
    in_progress.add(letter)
    to_do.remove(letter)
    w.extend([letter] * get_duration(letter))
    # print(f'work assigned: {workers}')


def any_letters_ready():
    return len(ready_letters()) > 0


def ready_letters():
    ready = set()
    for val in to_do:
        finished = True
        for node in rev_graph[val]:
            if node not in done:
                finished = False
        # print(f'val {val} f{finished}')
        if finished:
            ready.add(val)
    return ready


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


def process(time):
    #
    # FIXME: it looks like it is processing correctly up until final letter, then it just finishes after first hit (ie only a single iteration of E)
    #
    if len(to_do) == 0 and all_free():
        return time

    while any_free_workers() and any_letters_ready():
        letters = list(ready_letters())
        letters.sort()
        assign_work(free_worker(), letters[0])

    tick(time)
    time += 1
    return process(time)


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
answer = process(0)
print(f'answer {answer}')
print(current_tick)
