from dataclasses import dataclass
import json

# Read dataset JSON file
with open('./dataset_with_difficulty_and_algorithm.json', 'r') as dfile:
    data = json.load(dfile)

# Get and list the possible paradigms
paradigms = set([d for ds in map(lambda d: d['algorithms'], data) for d in ds])
print(f'Dataset paradigms: {paradigms}')

# Choose the 'greedy' paradigm
PARADIGM = 'greedy'
print(f'Using paradigm: {PARADIGM}')


@dataclass
class TestSet:
    """Stores a set of tests for a given `Problem`."""
    basic: list[str]
    advanced: list[str]

    def __repr__(self):
        basics = '\n'.join([f'    {b}' for b in self.basic])
        advs = '\n'.join([f'    {a}' for a in self.advanced])
        timed = '\n'.join([f'    {t}' for t in self.advanced[:10]])
        return f'''
def run_basic_tests(solution):
{basics}

def run_advanced_tests(solution):
{advs}

def run_timed_tests(solution):
{timed}
        '''


@dataclass
class Problem:
    """Stores needed information about a problem in the input dataset."""
    idx: int
    name: str
    desc: str
    solu: str
    tests: TestSet
    difficulty: str

    def __repr__(self):
        modname = f'{self.difficulty.lower()}_{self.idx}'
        solvers = ['SolutionChatGPT()', 'SolutionGemini()', 'SolutionClaude()']
        if self.idx == 527:
            solvers.pop()  # Remove Clause (it's broken)
        return f'''
from {modname}_canon import Solution as SolutionCanon
from chatgpt_{modname} import Solution as SolutionChatGPT
from claude_{modname} import Solution as SolutionClaude
from gemini_{modname} import Solution as SolutionGemini

{self.tests}

if __name__ == '__main__':
    import sys
    problem_id = {self.idx}
    if sys.argv[1] == 'test':
        solvers = [SolutionCanon()]
        if len(sys.argv) == 3 and sys.argv[2] == 'all':
            solvers.extend([{', '.join(solvers)}])
        for solver in solvers:
            run_basic_tests(solver)
            run_advanced_tests(solver)
    elif sys.argv[1] == 'time':
        import time, statistics
        solver = {{
            'canon': SolutionCanon,
            'chatgpt': SolutionChatGPT,
            'claude': SolutionClaude,
            'gemini': SolutionGemini,
        }}[sys.argv[2]]()
        times = []

        print(f'{modname},{{sys.argv[2]}},', end='')
        if problem_id == 527 and sys.argv[2] == 'claude':
            print('-- NR --')
            sys.exit(0)

        try:
            for _ in range(int(sys.argv[3])):
                start = time.time()
                run_timed_tests(solver)
                end = time.time()
                times.append(end - start)
        except AssertionError as err:
            print(f'Assertion Failed: {{err}}', file=sys.stderr)
            print('-- IR --')
            sys.exit(0)

        avg_time = statistics.mean(times)
        print(f'{{avg_time:.4E}}')
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

# Gather the problems under the relevant paradigm
for diff in problems.keys():
    def is_relevant(d: any) -> bool:
        return d['difficulty'] == diff and PARADIGM in d['algorithms']
    for d in filter(is_relevant, data):
        def is_test_assertion(t: str) -> bool:
            return 'assert' in t
        tests = TestSet(list(filter(is_test_assertion,
                                    d['small_test_cases'].splitlines())),
                        list(filter(is_test_assertion,
                                    d['test_case'].splitlines())))
        problem = Problem(int(d['problem_idx']), d['task_name'],
                          d['markdown_description'], d['canonical_solution'],
                          tests, diff)
        problems[diff].append(problem)

# List the number of problems in each difficulty
print('Problem counts:')
for diff, probs in problems.items():
    print(f'    N {diff}: {len(probs)}')

# Get the first 10 problems of each difficulty
EASY = problems['Easy'][:10]
MEDIUM = problems['Medium'][:10]
HARD = problems['Hard'][:10]


def getNames(ps: list[Problem]) -> list[str]:
    """Returns a list of problem names from a list of `Problem`s."""
    return [p.name for p in ps]


print(f'Selected Easy Problems: {getNames(EASY)}')
print(f'Selected Medium Problems: {getNames(MEDIUM)}')
print(f'Selected Hard Problems: {getNames(HARD)}')


def write_problems(diff: str, ps: list[Problem]):
    """Writes problems to their own test files and generates the prompts."""
    for p in ps:
        # Write the tests
        with open(f'./tests/{diff.lower()}_{p.idx}_tests.py', 'w') as f:
            f.write(repr(p))
        # Write the human-generated solution
        with open(f'./tests/{diff.lower()}_{p.idx}_canon.py', 'w') as f:
            f.write(p.getSoluString())
        # Write the prompt (problem description)
        with open(f'./prompts/{diff.lower()}_{p.idx}.md', 'w') as f:
            f.write(p.desc)


# Write the problems
write_problems('Easy', EASY)
write_problems('Medium', MEDIUM)
write_problems('Hard', HARD)
