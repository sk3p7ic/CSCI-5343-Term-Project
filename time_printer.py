# Read the input CSV file to a `list[tuple[str, str, str]]`
with open('./times.csv', 'r') as f:
    data = f.readlines()
    data = [list(map(lambda x: x.strip(), ln.split(','))) for ln in data]
    data = [(d[0], d[1], d[2]) for d in data]

# Create the dictionary to store the results
results = {
    'easy': {},
    'medium': {},
    'hard': {}
}

# Store the results into the dictionary
for (diff_idx, author, time) in data:
    diff, idx = diff_idx.split('_')
    res = results[diff].get(idx, {})
    res[author] = time
    results[diff][idx] = res

# Write the results in a tabular format to stdout
for difficulty, problems in results.items():
    print(difficulty)
    for idx, times in problems.items():
        for author, time in times.items():
            print(f'{idx:8s} {author:8s} {time}')
    print('\n\n')