from easy_942_canon import Solution as SolutionCanon
from chatgpt_easy_942 import Solution as SolutionChatGPT
from claude_easy_942 import Solution as SolutionClaude
from gemini_easy_942 import Solution as SolutionGemini


def run_basic_tests(solution):
    assert solution.diStringMatch("IDID") == [0, 4, 1, 3, 2]
    assert solution.diStringMatch("III") == [0, 1, 2, 3]
    assert solution.diStringMatch("DDI") == [3, 2, 0, 1]

def run_advanced_tests(solution):
    assert solution.diStringMatch("IDI") == [0, 3, 1, 2]
    assert solution.diStringMatch("DIDDIIII") == [8, 0, 7, 6, 1, 2, 3, 4, 5]
    assert solution.diStringMatch("IIII") == [0, 1, 2, 3, 4]
    assert solution.diStringMatch("IIIDI") == [0, 1, 2, 5, 3, 4]
    assert solution.diStringMatch("DII") == [3, 0, 1, 2]
    assert solution.diStringMatch("I") == [0, 1]
    assert solution.diStringMatch("DIIIDIDD") == [8, 0, 1, 2, 7, 3, 6, 5, 4]
    assert solution.diStringMatch("IIDII") == [0, 1, 5, 2, 3, 4]
    assert solution.diStringMatch("IIIDDID") == [0, 1, 2, 7, 6, 3, 5, 4]
    assert solution.diStringMatch("IDIDID") == [0, 6, 1, 5, 2, 4, 3]
    assert solution.diStringMatch("DDDIDDDI") == [8, 7, 6, 0, 5, 4, 3, 1, 2]
    assert solution.diStringMatch("IDIIIID") == [0, 7, 1, 2, 3, 4, 6, 5]
    assert solution.diStringMatch("IDDDD") == [0, 5, 4, 3, 2, 1]
    assert solution.diStringMatch("DIDDD") == [5, 0, 4, 3, 2, 1]
    assert solution.diStringMatch("DDIDIIID") == [8, 7, 0, 6, 1, 2, 3, 5, 4]
    assert solution.diStringMatch("DDDD") == [4, 3, 2, 1, 0]
    assert solution.diStringMatch("IDIDDDDIDD") == [0, 10, 1, 9, 8, 7, 6, 2, 5, 4, 3]
    assert solution.diStringMatch("DIDIDDDIID") == [10, 0, 9, 1, 8, 7, 6, 2, 3, 5, 4]
    assert solution.diStringMatch("IIDIDIDD") == [0, 1, 8, 2, 7, 3, 6, 5, 4]
    assert solution.diStringMatch("DID") == [3, 0, 2, 1]
    assert solution.diStringMatch("IDIDID") == [0, 6, 1, 5, 2, 4, 3]
    assert solution.diStringMatch("DIIIDIDD") == [8, 0, 1, 2, 7, 3, 6, 5, 4]
    assert solution.diStringMatch("DDDDDDIDD") == [9, 8, 7, 6, 5, 4, 0, 3, 2, 1]
    assert solution.diStringMatch("DDDDI") == [5, 4, 3, 2, 0, 1]
    assert solution.diStringMatch("DDIIID") == [6, 5, 0, 1, 2, 4, 3]
    assert solution.diStringMatch("IID") == [0, 1, 3, 2]
    assert solution.diStringMatch("IDDDIDI") == [0, 7, 6, 5, 1, 4, 2, 3]
    assert solution.diStringMatch("DIIDIDII") == [8, 0, 1, 7, 2, 6, 3, 4, 5]
    assert solution.diStringMatch("IIIDDDIID") == [0, 1, 2, 9, 8, 7, 3, 4, 6, 5]
    assert solution.diStringMatch("IIDII") == [0, 1, 5, 2, 3, 4]
    assert solution.diStringMatch("DDIIDD") == [6, 5, 0, 1, 4, 3, 2]
    assert solution.diStringMatch("DII") == [3, 0, 1, 2]
    assert solution.diStringMatch("IDIDIDIID") == [0, 9, 1, 8, 2, 7, 3, 4, 6, 5]
    assert solution.diStringMatch("IIIDIDID") == [0, 1, 2, 8, 3, 7, 4, 6, 5]
    assert solution.diStringMatch("DIDDIIDDI") == [9, 0, 8, 7, 1, 2, 6, 5, 3, 4]
    assert solution.diStringMatch("IDDDIID") == [0, 7, 6, 5, 1, 2, 4, 3]
    assert solution.diStringMatch("IIDDDID") == [0, 1, 7, 6, 5, 2, 4, 3]
    assert solution.diStringMatch("D") == [1, 0]
    assert solution.diStringMatch("DII") == [3, 0, 1, 2]
    assert solution.diStringMatch("D") == [1, 0]
    assert solution.diStringMatch("D") == [1, 0]
    assert solution.diStringMatch("DD") == [2, 1, 0]
    assert solution.diStringMatch("IIIIIID") == [0, 1, 2, 3, 4, 5, 7, 6]
    assert solution.diStringMatch("DIIID") == [5, 0, 1, 2, 4, 3]
    assert solution.diStringMatch("DIIIID") == [6, 0, 1, 2, 3, 5, 4]
    assert solution.diStringMatch("DIDIIIID") == [8, 0, 7, 1, 2, 3, 4, 6, 5]
    assert solution.diStringMatch("DD") == [2, 1, 0]
    assert solution.diStringMatch("IDIID") == [0, 5, 1, 2, 4, 3]
    assert solution.diStringMatch("IIDI") == [0, 1, 4, 2, 3]
    assert solution.diStringMatch("IIDIDI") == [0, 1, 6, 2, 5, 3, 4]
    assert solution.diStringMatch("IIIIDIIIDD") == [0, 1, 2, 3, 10, 4, 5, 6, 9, 8, 7]
    assert solution.diStringMatch("DIDDI") == [5, 0, 4, 3, 1, 2]
    assert solution.diStringMatch("IDIDID") == [0, 6, 1, 5, 2, 4, 3]
    assert solution.diStringMatch("DIIDDIDD") == [8, 0, 1, 7, 6, 2, 5, 4, 3]
    assert solution.diStringMatch("DDIIIIDID") == [9, 8, 0, 1, 2, 3, 7, 4, 6, 5]
    assert solution.diStringMatch("DDD") == [3, 2, 1, 0]
    assert solution.diStringMatch("DIIIIIDII") == [9, 0, 1, 2, 3, 4, 8, 5, 6, 7]
    assert solution.diStringMatch("IIDDI") == [0, 1, 5, 4, 2, 3]
    assert solution.diStringMatch("IIDDIIIII") == [0, 1, 9, 8, 2, 3, 4, 5, 6, 7]
    assert solution.diStringMatch("II") == [0, 1, 2]
    assert solution.diStringMatch("D") == [1, 0]
    assert solution.diStringMatch("DDIDIIDIID") == [10, 9, 0, 8, 1, 2, 7, 3, 4, 6, 5]
    assert solution.diStringMatch("IIIIIIDID") == [0, 1, 2, 3, 4, 5, 9, 6, 8, 7]
    assert solution.diStringMatch("IDDIDDIIII") == [0, 10, 9, 1, 8, 7, 2, 3, 4, 5, 6]
    assert solution.diStringMatch("DDDDDDID") == [8, 7, 6, 5, 4, 3, 0, 2, 1]
    assert solution.diStringMatch("IDIIDIDDII") == [0, 10, 1, 2, 9, 3, 8, 7, 4, 5, 6]
    assert solution.diStringMatch("DDIIDDDDI") == [9, 8, 0, 1, 7, 6, 5, 4, 2, 3]
    assert solution.diStringMatch("IIIDDDID") == [0, 1, 2, 8, 7, 6, 3, 5, 4]
    assert solution.diStringMatch("IIIDI") == [0, 1, 2, 5, 3, 4]
    assert solution.diStringMatch("IDII") == [0, 4, 1, 2, 3]
    assert solution.diStringMatch("IIIID") == [0, 1, 2, 3, 5, 4]
    assert solution.diStringMatch("IIDIDIDDID") == [0, 1, 10, 2, 9, 3, 8, 7, 4, 6, 5]
    assert solution.diStringMatch("D") == [1, 0]
    assert solution.diStringMatch("DDIDDIDI") == [8, 7, 0, 6, 5, 1, 4, 2, 3]
    assert solution.diStringMatch("DDDIIDI") == [7, 6, 5, 0, 1, 4, 2, 3]
    assert solution.diStringMatch("DDDIDI") == [6, 5, 4, 0, 3, 1, 2]
    assert solution.diStringMatch("I") == [0, 1]
    assert solution.diStringMatch("DDDIDII") == [7, 6, 5, 0, 4, 1, 2, 3]
    assert solution.diStringMatch("IDIIDD") == [0, 6, 1, 2, 5, 4, 3]
    assert solution.diStringMatch("DIID") == [4, 0, 1, 3, 2]
    assert solution.diStringMatch("IID") == [0, 1, 3, 2]
    assert solution.diStringMatch("IIIIIII") == [0, 1, 2, 3, 4, 5, 6, 7]
    assert solution.diStringMatch("III") == [0, 1, 2, 3]
    assert solution.diStringMatch("IDIDDIDI") == [0, 8, 1, 7, 6, 2, 5, 3, 4]
    assert solution.diStringMatch("IDII") == [0, 4, 1, 2, 3]
    assert solution.diStringMatch("DDIII") == [5, 4, 0, 1, 2, 3]
    assert solution.diStringMatch("DI") == [2, 0, 1]
    assert solution.diStringMatch("IDIDDDII") == [0, 8, 1, 7, 6, 5, 2, 3, 4]
    assert solution.diStringMatch("DDDID") == [5, 4, 3, 0, 2, 1]
    assert solution.diStringMatch("D") == [1, 0]
    assert solution.diStringMatch("II") == [0, 1, 2]
    assert solution.diStringMatch("ID") == [0, 2, 1]
    assert solution.diStringMatch("IDIIDDDIID") == [0, 10, 1, 2, 9, 8, 7, 3, 4, 6, 5]
    assert solution.diStringMatch("IDIDI") == [0, 5, 1, 4, 2, 3]
    assert solution.diStringMatch("DD") == [2, 1, 0]
    assert solution.diStringMatch("IIDDI") == [0, 1, 5, 4, 2, 3]
    assert solution.diStringMatch("IDDIDDDII") == [0, 9, 8, 1, 7, 6, 5, 2, 3, 4]
    assert solution.diStringMatch("D") == [1, 0]
    assert solution.diStringMatch("III") == [0, 1, 2, 3]
    assert solution.diStringMatch("DIDIDI") == [6, 0, 5, 1, 4, 2, 3]

def run_timed_tests(solution):
    assert solution.diStringMatch("IDI") == [0, 3, 1, 2]
    assert solution.diStringMatch("DIDDIIII") == [8, 0, 7, 6, 1, 2, 3, 4, 5]
    assert solution.diStringMatch("IIII") == [0, 1, 2, 3, 4]
    assert solution.diStringMatch("IIIDI") == [0, 1, 2, 5, 3, 4]
    assert solution.diStringMatch("DII") == [3, 0, 1, 2]
    assert solution.diStringMatch("I") == [0, 1]
    assert solution.diStringMatch("DIIIDIDD") == [8, 0, 1, 2, 7, 3, 6, 5, 4]
    assert solution.diStringMatch("IIDII") == [0, 1, 5, 2, 3, 4]
    assert solution.diStringMatch("IIIDDID") == [0, 1, 2, 7, 6, 3, 5, 4]
    assert solution.diStringMatch("IDIDID") == [0, 6, 1, 5, 2, 4, 3]
        

def save_output(output: str):
    with open('../times.csv', 'a') as f:
        f.write(f'{output}\n')

if __name__ == '__main__':
    import sys
    problem_id = 942
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

        output += f'easy_942,{sys.argv[2]},'
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