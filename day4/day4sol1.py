guards = set()
sleeping_tuples = {}
sleeping_minutes = {}
current_guard = ""
start_sleep = -1
with open('workfile.txt', 'r') as file:
    for line in file:
        chunks = line.split(']')
        if chunks[1][1:6] == "Guard":
            current_guard = chunks[1].split(" ")[2]
            continue

        time = str(chunks[0][1:]).split(" ")[1]
        hours = time.split(":")[0]
        minutes = time.split(":")[1]
        if hours != "00":
            continue

        if start_sleep == -1:
            start_sleep = minutes
        else:
            sleep_tuple = (int(start_sleep), int(minutes))
            start_sleep = -1
            if current_guard in sleeping_tuples:
                mins_list = sleeping_tuples[current_guard]
                mins_list.append(sleep_tuple)
                sleeping_tuples[current_guard] = mins_list
            else:
                sleeping_tuples[current_guard] = [sleep_tuple]

max_guard = ""
mins_sleep = 0
for guard, asleeps in sleeping_tuples.items():
    guard_asleep = 0
    for asleep in asleeps:
        guard_asleep += (asleep[1] - asleep[0])

    if guard_asleep > mins_sleep:
        max_guard = guard
        mins_sleep = guard_asleep


minutes_asleep = list()
for asleep in sleeping_tuples[max_guard]:
    for min in range(asleep[0], asleep[1]):
        minutes_asleep.append(min)

most_common_minute = max(set(minutes_asleep), key=minutes_asleep.count)
result = int(max_guard[1:]) * most_common_minute
print (f"Result = {max_guard} * {most_common_minute} = {result}")