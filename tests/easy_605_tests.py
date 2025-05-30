from easy_605_canon import Solution as SolutionCanon
from chatgpt_easy_605 import Solution as SolutionChatGPT
from claude_easy_605 import Solution as SolutionClaude
from gemini_easy_605 import Solution as SolutionGemini


def run_basic_tests(solution):
    assert solution.canPlaceFlowers([1,0,0,0,1], 1) == True
    assert solution.canPlaceFlowers([1,0,0,0,1], 2) == False

def run_advanced_tests(solution):
    assert solution.canPlaceFlowers([0, 0, 1, 0, 1, 0, 0], 3) == False
    assert solution.canPlaceFlowers([1, 1, 1, 1, 1, 1, 0], 1) == False
    assert solution.canPlaceFlowers([0], 0) == True
    assert solution.canPlaceFlowers([1, 1, 0, 1], 0) == True
    assert solution.canPlaceFlowers([0, 1, 0, 0, 1, 0, 0, 0, 1], 4) == False
    assert solution.canPlaceFlowers([0, 1, 0, 0, 0], 4) == False
    assert solution.canPlaceFlowers([0], 0) == True
    assert solution.canPlaceFlowers([0, 0, 1, 1, 1], 0) == True
    assert solution.canPlaceFlowers([1, 0, 1, 1, 1, 0, 1, 0, 1, 1], 7) == False
    assert solution.canPlaceFlowers([1, 1, 0, 0, 0], 3) == False
    assert solution.canPlaceFlowers([1, 1, 0, 1, 0], 0) == True
    assert solution.canPlaceFlowers([0, 0], 1) == True
    assert solution.canPlaceFlowers([1, 1, 0], 2) == False
    assert solution.canPlaceFlowers([1], 0) == True
    assert solution.canPlaceFlowers([0, 1, 1, 1, 1, 0, 1, 0, 0, 1], 3) == False
    assert solution.canPlaceFlowers([1, 1, 0, 1, 0, 1, 0, 0, 0, 1], 7) == False
    assert solution.canPlaceFlowers([0, 1, 0, 0, 0, 1], 6) == False
    assert solution.canPlaceFlowers([0, 1, 0, 1, 1, 1, 1, 1], 2) == False
    assert solution.canPlaceFlowers([0, 0, 0, 1, 0, 0, 0, 1, 1, 1], 8) == False
    assert solution.canPlaceFlowers([0, 1, 0, 1, 1, 1, 0, 0], 1) == True
    assert solution.canPlaceFlowers([0, 1, 1, 0, 0], 5) == False
    assert solution.canPlaceFlowers([1, 1, 0, 1, 0, 1], 0) == True
    assert solution.canPlaceFlowers([1, 0, 1, 0, 1, 0, 0], 7) == False
    assert solution.canPlaceFlowers([0, 0], 2) == False
    assert solution.canPlaceFlowers([0, 1, 1], 2) == False
    assert solution.canPlaceFlowers([1, 0], 0) == True
    assert solution.canPlaceFlowers([0], 1) == True
    assert solution.canPlaceFlowers([1, 1, 0, 1, 0, 1], 5) == False
    assert solution.canPlaceFlowers([0, 0, 1, 1, 1], 1) == True
    assert solution.canPlaceFlowers([1, 0, 0], 1) == True
    assert solution.canPlaceFlowers([0, 0], 0) == True
    assert solution.canPlaceFlowers([0, 0, 0, 1, 1, 1, 1, 0, 0], 3) == False
    assert solution.canPlaceFlowers([1, 1, 0, 1, 1], 5) == False
    assert solution.canPlaceFlowers([1, 0, 1, 1, 0, 1, 0, 1, 1, 1], 10) == False
    assert solution.canPlaceFlowers([1], 1) == False
    assert solution.canPlaceFlowers([1, 0, 1, 1, 1, 1, 1, 0], 8) == False
    assert solution.canPlaceFlowers([1, 0, 0, 1, 0, 1, 0, 0, 0], 4) == False
    assert solution.canPlaceFlowers([0, 0, 1, 0, 0, 0, 1, 1, 0, 0], 10) == False
    assert solution.canPlaceFlowers([0, 0, 1, 0, 1, 0, 0, 1, 1], 6) == False
    assert solution.canPlaceFlowers([0, 1, 1, 0], 3) == False
    assert solution.canPlaceFlowers([1], 1) == False
    assert solution.canPlaceFlowers([0, 1], 1) == False
    assert solution.canPlaceFlowers([1, 0, 0, 0, 0, 0, 1, 0, 1], 0) == True
    assert solution.canPlaceFlowers([0, 0, 1], 0) == True
    assert solution.canPlaceFlowers([1], 1) == False
    assert solution.canPlaceFlowers([1, 1, 1, 0, 0, 1, 0], 0) == True
    assert solution.canPlaceFlowers([1, 0, 1, 0], 1) == False
    assert solution.canPlaceFlowers([1, 1, 0], 1) == False
    assert solution.canPlaceFlowers([0, 1, 1], 3) == False
    assert solution.canPlaceFlowers([1, 1, 0, 1, 0, 0, 0, 1, 1, 1], 6) == False
    assert solution.canPlaceFlowers([0, 0, 0, 0, 1, 1, 1], 1) == True
    assert solution.canPlaceFlowers([1], 1) == False
    assert solution.canPlaceFlowers([1, 0], 1) == False
    assert solution.canPlaceFlowers([0, 1], 0) == True
    assert solution.canPlaceFlowers([1, 0, 1, 1, 0], 2) == False
    assert solution.canPlaceFlowers([0, 1, 0, 1, 1, 1, 0], 6) == False
    assert solution.canPlaceFlowers([1, 1, 0], 0) == True
    assert solution.canPlaceFlowers([0, 1, 1, 0, 0, 1, 0, 1, 0], 7) == False
    assert solution.canPlaceFlowers([0], 1) == True
    assert solution.canPlaceFlowers([1, 0, 1, 1, 0, 0, 1, 0], 3) == False
    assert solution.canPlaceFlowers([1, 1, 0, 0, 0, 0, 0, 0, 0, 1], 3) == True
    assert solution.canPlaceFlowers([0, 1, 1, 1], 1) == False
    assert solution.canPlaceFlowers([0, 1, 1, 0, 0, 1, 1, 1, 1, 0], 8) == False
    assert solution.canPlaceFlowers([1, 1, 1, 1, 0, 1, 0, 1, 1, 1], 0) == True
    assert solution.canPlaceFlowers([0, 0, 1, 0, 1, 0], 0) == True
    assert solution.canPlaceFlowers([0, 0], 2) == False
    assert solution.canPlaceFlowers([0, 0, 1, 1, 1, 1, 0, 1, 0, 0], 3) == False
    assert solution.canPlaceFlowers([1, 1, 0, 0, 1, 0, 0, 0, 0, 0], 9) == False
    assert solution.canPlaceFlowers([0, 1, 1, 1, 0, 1], 6) == False
    assert solution.canPlaceFlowers([0, 1, 1, 0, 1, 1, 1], 3) == False
    assert solution.canPlaceFlowers([0, 1, 0, 1, 1, 1], 2) == False
    assert solution.canPlaceFlowers([0, 1, 1, 0, 1, 0], 6) == False
    assert solution.canPlaceFlowers([1, 0, 1, 0, 1, 0, 1, 1], 2) == False
    assert solution.canPlaceFlowers([0, 1, 0, 0, 1], 0) == True
    assert solution.canPlaceFlowers([1, 1], 2) == False
    assert solution.canPlaceFlowers([0, 0, 0, 0, 0, 1, 0, 1], 5) == False
    assert solution.canPlaceFlowers([0, 0, 0, 1, 1, 1, 1, 0, 1], 1) == True
    assert solution.canPlaceFlowers([0], 0) == True
    assert solution.canPlaceFlowers([1, 0, 0, 1, 0, 1], 4) == False
    assert solution.canPlaceFlowers([0, 1, 1, 0, 0, 1], 6) == False
    assert solution.canPlaceFlowers([1, 1, 1, 1, 1], 5) == False
    assert solution.canPlaceFlowers([0], 1) == True
    assert solution.canPlaceFlowers([1, 0, 1], 1) == False
    assert solution.canPlaceFlowers([0, 1, 1, 1, 1, 1, 1, 1, 0], 1) == False
    assert solution.canPlaceFlowers([0, 0, 0, 0, 1, 1, 1, 0, 1], 0) == True
    assert solution.canPlaceFlowers([1, 0, 1, 1, 1, 0, 1, 0, 0, 0], 6) == False
    assert solution.canPlaceFlowers([1, 1, 0, 1], 1) == False
    assert solution.canPlaceFlowers([0, 0], 0) == True
    assert solution.canPlaceFlowers([1, 1], 1) == False
    assert solution.canPlaceFlowers([1], 0) == True
    assert solution.canPlaceFlowers([0, 1, 0, 1, 1, 1, 1, 0], 2) == False
    assert solution.canPlaceFlowers([1, 0, 1, 0], 2) == False
    assert solution.canPlaceFlowers([0, 1], 0) == True
    assert solution.canPlaceFlowers([0, 0, 0, 1, 1, 0, 0], 7) == False
    assert solution.canPlaceFlowers([0, 0, 0, 1], 4) == False
    assert solution.canPlaceFlowers([1, 1, 0, 0, 0, 1, 0], 3) == False
    assert solution.canPlaceFlowers([1, 0, 0, 1, 1, 1], 6) == False
    assert solution.canPlaceFlowers([1, 0, 0, 1, 1, 0, 1, 0, 1, 1], 3) == False
    assert solution.canPlaceFlowers([0, 0], 0) == True
    assert solution.canPlaceFlowers([0, 1, 1, 1, 1, 1, 1, 1, 0, 1], 4) == False

def run_timed_tests(solution):
    assert solution.canPlaceFlowers([0, 0, 1, 0, 1, 0, 0], 3) == False
    assert solution.canPlaceFlowers([1, 1, 1, 1, 1, 1, 0], 1) == False
    assert solution.canPlaceFlowers([0], 0) == True
    assert solution.canPlaceFlowers([1, 1, 0, 1], 0) == True
    assert solution.canPlaceFlowers([0, 1, 0, 0, 1, 0, 0, 0, 1], 4) == False
    assert solution.canPlaceFlowers([0, 1, 0, 0, 0], 4) == False
    assert solution.canPlaceFlowers([0], 0) == True
    assert solution.canPlaceFlowers([0, 0, 1, 1, 1], 0) == True
    assert solution.canPlaceFlowers([1, 0, 1, 1, 1, 0, 1, 0, 1, 1], 7) == False
    assert solution.canPlaceFlowers([1, 1, 0, 0, 0], 3) == False
        

def save_output(output: str):
    with open('../times.csv', 'a') as f:
        f.write(f'{output}\n')

if __name__ == '__main__':
    import sys
    problem_id = 605
    output = ''
    if sys.argv[1] == 'test':
        solvers = [SolutionCanon()]
        if len(sys.argv) == 3 and sys.argv[2] == 'all':
            solvers.extend([SolutionChatGPT(), SolutionGemini(), SolutionClaude()])
        for solver in solvers:
            run_basic_tests(solver)
            run_advanced_tests(solver)
    elif sys.argv[1] == 'time':
        import time, statistics
        solver = {
            'canon': SolutionCanon,
            'chatgpt': SolutionChatGPT,
            'claude': SolutionClaude,
            'gemini': SolutionGemini,
        }[sys.argv[2]]()
        times = []

        output += f'easy_605,{sys.argv[2]},'
        if problem_id == 527 and sys.argv[2] == 'claude':
            output += '-- NR --,'
            save_output(output)
            sys.exit(0)

        try:
            for _ in range(int(sys.argv[3])):
                start = time.perf_counter_ns()
                run_timed_tests(solver)
                end = time.perf_counter_ns()
                times.append(end - start)
        except AssertionError as err:
            print(f'Assertion Failed: {err}', file=sys.stderr)
            output += '-- IR --,'
            save_output(output)
            sys.exit(0)

        avg_time = statistics.mean(times)
        total_time = sum(times)
        output += f'{avg_time:.4E},{total_time:.4E}'
        save_output(output)