with open('./times.csv', 'r') as f:
    data = f.readlines()
    data = [list(map(lambda x: x.strip(), ln.split(','))) for ln in data]
    data = [(d[0], d[1], d[2]) for d in data]

results = {
    'easy': {},
    'medium': {},
    'hard': {}
}

for (fullname, writer, time) in data:
    diff, idx = fullname.split('_')
    res = results[diff].get(idx, {})
    res[writer] = time
    results[diff][idx] = res

for difficulty, problems in results.items():
    print(difficulty)
    for idx, times in problems.items():
        for writer, time in times.items():
            print(f'{idx:8s} {writer:8s} {time}')
    print('\n\n')