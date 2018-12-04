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

for guard, asleeps in sleeping_tuples.items():
    minutes_asleep = list()
    for asleep in asleeps:
        for min in range(asleep[0], asleep[1]):
            minutes_asleep.append(min)
    sleeping_minutes[guard] = minutes_asleep

max_guard = ""
max_minute_count = 0
max_minute = -1
for guard, minutes in sleeping_minutes.items():
    top_minute = max(set(minutes), key=minutes.count)
    minute_count = minutes.count(top_minute)
    if minute_count > max_minute_count:
        max_minute_count = minute_count
        max_minute = top_minute
        max_guard = guard


result = int(max_guard[1:]) * max_minute
print (f"Result = {max_guard} * {max_minute} = {result}")