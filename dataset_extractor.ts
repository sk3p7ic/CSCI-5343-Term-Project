import dataset from './dataset_with_difficulty_and_algorithm.json' with { 'type': 'json' };

const paradigms = new Set(dataset.map(d => d.algorithms).flat());
console.log('Dataset paradigms:', paradigms, '\n');

type Difficulty = "Easy" | "Medium" | "Hard";
const difficulties: Difficulty[] = ["Easy", "Medium", "Hard"];

type Problem = {
    idx: number;
    name: number;
    desc: number;
    solu: string;
    tests: {
        basic: string[];
        advanced: string[];
    }
};

const paradigm = 'greedy'
console.log('Using paradigm:', paradigm);
const problems: Map<Difficulty, Problem[]> = new Map(difficulties.map((diff) => {
    const ps: Problem[] = dataset.filter(d => d.algorithms.includes(paradigm))
        .filter(d => d.difficulty === diff)
        .map(d => ({
            idx: d.problem_idx,
            name: d.task_name,
            desc: d.markdown_description,
            solu: d.canonical_solution,
            tests: {
                basic: d.small_test_cases.split('\n').filter(t => !t.includes('Solution')),
                advanced: d.test_case.split('\n').filter(t => !t.includes('Solution'))
            }
        }));
    return [diff, ps];
}));

console.log('Problem Counts:')
console.log('  N Easy:', problems.get('Easy')?.length);
console.log('  N Medium:', problems.get('Medium')?.length);
console.log('  N Hard:', problems.get('Hard')?.length);

const easy = problems.get('Easy')!.slice(0, 10);
const medium = problems.get('Medium')!.slice(0, 10);
const hard = problems.get('Hard')!.slice(0, 10);

const getNames = (ps: Problem[]) => ps.map(p => p.name);
console.log('Selected Easy Problems:', getNames(easy));
console.log('Selected Medium Problems:', getNames(medium));
console.log('Selected Hard Problems:', getNames(hard));

const pythonizeTests = (p: Problem, d: Difficulty): string => `from ${d.toLowerCase()}_${p.idx}_canon import Solution as SolutionCanon

def run_basic_tests(solution):
${p.tests.basic.map(t => `    ${t}`).join('\n')}


def run_advanced_tests(solution):
${p.tests.advanced.map(t => `    ${t}`).join('\n')}

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
        print(f'Canonical Average Time: {canon_avg:.4E}')
`;

const pythonizeSolu = (s: string): string => `from typing import *
from collections import *
from itertools import *
from functools import *
from operator import *
from bisect import *
from heapq import *
from math import *

${s}`;

easy.forEach(p => {
    const testCode = pythonizeTests(p, "Easy");
    Deno.writeTextFileSync(`./tests/easy_${p.idx}_tests.py`, testCode);
    Deno.writeTextFileSync(`./tests/easy_${p.idx}_canon.py`, pythonizeSolu(p.solu));
    Deno.writeTextFileSync(`./prompts/easy_${p.idx}.md`, p.desc);
});
medium.forEach(p => {
    const testCode = pythonizeTests(p, "Medium");
    Deno.writeTextFileSync(`./tests/medium_${p.idx}_tests.py`, testCode);
    Deno.writeTextFileSync(`./tests/medium_${p.idx}_canon.py`, pythonizeSolu(p.solu));
    Deno.writeTextFileSync(`./prompts/medium_${p.idx}.md`, p.desc);
});
hard.forEach(p => {
    const testCode = pythonizeTests(p, "Hard");
    Deno.writeTextFileSync(`./tests/hard_${p.idx}_tests.py`, testCode);
    Deno.writeTextFileSync(`./tests/hard_${p.idx}_canon.py`, pythonizeSolu(p.solu));
    Deno.writeTextFileSync(`./prompts/hard_${p.idx}.md`, p.desc);
});