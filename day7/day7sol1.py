from collections import defaultdict

# filename = 'practice.txt'
filename = 'workfile.txt'

def process(roots):
    if len(roots) == 0:
        return ''

    roots.sort()
    root = None
    print(f'process: {root} {roots}')
    for check in roots:
        ready = True
        for node in rev_graph[check]:
            if node not in done:
                ready = False
        if ready:
            root = check
            break

    if root is None:
        print(f'no roots ready in {roots}')
        exit(-1)

    roots.remove(root)
    if root in done:
        result = ''
        new_roots = roots
    else:
        result = root
        done.append(root)
        new_roots = graph[root] + roots
    result += process(new_roots)
    return result

pres = set()
posts = set()
graph = defaultdict(list)
rev_graph = defaultdict(list)
done = []

with open(filename, 'r') as file:
    for line in file:
        words = line.split()
        pre = words[1]
        post = words[7]
        pres.add(pre)
        posts.add(post)
        graph[pre].append(post)
        rev_graph[post].append(pre)

print(graph)

roots = list(pres.difference(posts))
result = process(roots)
print(result)