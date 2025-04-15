from dataclasses import dataclass
import json

# Read dataset JSON file
with open('./dataset_with_difficulty_and_algorithm.json', 'r') as dfile:
    data = json.load(dfile)

paradigms = set([d for ds in map(lambda d: d['algorithms'], data) for d in ds])
print(f'Dataset paradigms: {paradigms}')

PARADIGM = 'greedy'
print(f'Using paradigm: {PARADIGM}')


@dataclass
class TestSet:
    basic: list[str]
    advanced: list[str]

    def __repr__(self):
        basics = '\n'.join([f'    {b}' for b in self.basic])
        advs = '\n'.join([f'    {a}' for a in self.advanced])
        return f'''
def run_basic_tests(solution):
{basics}

def run_advanced_tests(solution):
{advs}
        '''


@dataclass
class Problem:
    idx: int
    name: str
    desc: str
    solu: str
    tests: TestSet
    diff: str

    def __repr__(self):
        return f'''
from {self.diff.lower()}_{self.idx}_canon import Solution as SolutionCanon

{self.tests}

if __name__ == '__main__':
    import sys
    if sys.argv[1] == 'test':
        canon = SolutionCanon()
        run_basic_tests(canon)
        run_advanced_tests(canon)
    if sys.argv[1] == 'time':
        import time, statistics
        canon_times = []

        canon = SolutionCanon()
        for _ in range(int(sys.argv[2])):
            start = time.time()
            run_basic_tests(canon)
            run_advanced_tests(canon)
            end = time.time()
            canon_times.append(end - start)

        canon_avg = statistics.mean(canon_times)
        print(f'Canonical Average Time: {{canon_avg:.4E}}')
'''.strip()

    def getSoluString(self) -> str:
        return f'''
from typing import *
from collections import *
from itertools import *
from functools import *
from operator import *
from bisect import *
from heapq import *
from math import *

{self.solu}
        '''.strip()


problems = {
    'Easy': [],
    'Medium': [],
    'Hard': []
}

for diff in problems.keys():
    def is_relevant(d: any) -> bool:
        return d['difficulty'] == diff and PARADIGM in d['algorithms']
    for d in filter(is_relevant, data):
        def test_filter(t: str) -> bool:
            return 'Solution' not in t
        tests = TestSet(list(filter(test_filter,
                                    d['small_test_cases'].splitlines())),
                        list(filter(test_filter,
                                    d['test_case'].splitlines())))
        problem = Problem(int(d['problem_idx']), d['task_name'],
                          d['markdown_description'], d['canonical_solution'],
                          tests, diff)
        problems[diff].append(problem)

print('Problem counts:')
for diff, probs in problems.items():
    print(f'    N {diff}: {len(probs)}')

EASY = problems['Easy'][:10]
MEDIUM = problems['Medium'][:10]
HARD = problems['Hard'][:10]


def getNames(ps: list[Problem]) -> list[str]:
    return [p.name for p in ps]


print(f'Selected Easy Problems: {getNames(EASY)}')
print(f'Selected Medium Problems: {getNames(MEDIUM)}')
print(f'Selected Hard Problems: {getNames(HARD)}')


def write_problems(diff: str, ps: list[Problem]):
    for p in ps:
        with open(f'./tests/{diff.lower()}_{p.idx}_tests.py', 'w') as f:
            f.write(repr(p))
        with open(f'./tests/{diff.lower()}_{p.idx}_canon.py', 'w') as f:
            f.write(p.getSoluString())
        with open(f'./prompts/{diff.lower()}_{p.idx}.md', 'w') as f:
            f.write(p.desc)


write_problems('Easy', EASY)
write_problems('Medium', MEDIUM)
write_problems('Hard', HARD)
