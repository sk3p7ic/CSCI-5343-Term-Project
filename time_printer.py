import os

# Read the input CSV file to a `list[tuple[str, str, str]]`
with open('./times.csv', 'r') as f:
    data = f.readlines()
    data = [list(map(lambda x: x.strip(), ln.split(','))) for ln in data]
    data = [(d[0], d[1], d[2], d[3]) for d in data[1:]]

# Create the dictionary to store the results
results = {
    'easy': {},
    'medium': {},
    'hard': {}
}

# Store the results into the dictionary
for (diff_idx, author, avg_time, total_time) in data:
    diff, idx = diff_idx.split('_')
    res = results[diff].get(idx, {})
    res[author] = {
        'time_avg': avg_time,
        'time_total': total_time
    }
    results[diff][idx] = res


def calc_mem_usage(chunk: list[str]) -> (float, float):
    prev_time = 0
    prev_mem_mb = 0
    mem_time_mb_s = 0
    max_mem_usage = 0
    for line in chunk:
        parts = line.split()
        mem_in_mb = float(parts[1])
        timestamp = float(parts[2])
        max_mem_usage = max(max_mem_usage, mem_in_mb)
        if prev_time > 0:
            time_interval_s = timestamp - prev_time
            mem_time_mb_s += (prev_mem_mb + mem_in_mb) / 2 * time_interval_s
        prev_time = timestamp
        prev_mem_mb = mem_in_mb
    return mem_time_mb_s, max_mem_usage


for datafile in os.listdir('mem-profiles'):
    with open(f'mem-profiles/{datafile}', 'r') as df:
        mem_data = df.read()
    mem_data = mem_data.split('CMDLINE')[1:]
    diff, idx = datafile.removesuffix('.dat').split('_')
    for chunk in mem_data:
        chunk = chunk.splitlines()
        author = chunk[0].split(' ')[-2]
        chunk = chunk[1:]
        avg_mem, max_mem = calc_mem_usage(chunk)
        results[diff][idx][author]['mem_avg'] = avg_mem
        results[diff][idx][author]['mem_max'] = max_mem

# Write the results in a tabular format to stdout
for difficulty, problems in results.items():
    print(difficulty)
    print(f'{"Prob #":8s} {"Author":8s} {"Avg Time":12s} {"Total Time":12s} {"Avg Mem":12s} {"Max Mem":12s}')
    for idx, times in problems.items():
        for author, stats in times.items():
            avg_time = stats['time_avg']
            total_time = stats['time_total']
            avg_mem = f'{stats["mem_avg"]:.4E}'
            max_mem = f'{stats["mem_max"]:.4E}'
            print(
                f'{idx:8s} {author:8s} {avg_time:12s} {total_time:12s} {avg_mem:12s} {max_mem:12s}')
    print('\n\n')

for difficulty, problems in results.items():
    output = f'{"Prob #":8s}\t{"Author":8s}\t{"Avg Time":12s}\t{"Total Time":12s}\t{"Avg Mem":12s}\t{"Max Mem":12s}\n'
    for idx, times in problems.items():
        for author, stats in times.items():
            avg_time = stats['time_avg']
            total_time = stats['time_total']
            avg_mem = f'{stats["mem_avg"]:.4E}'
            max_mem = f'{stats["mem_max"]:.4E}'
            output += f'{idx:8s}\t{author:8s}\t{avg_time:12s}\t{total_time:12s}\t{avg_mem:12s}\t{max_mem:12s}\n'
    with open(f'{difficulty}_times.csv', 'w') as f:
        f.write(output)
