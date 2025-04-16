from hard_321_canon import Solution as SolutionCanon
from chatgpt_hard_321 import Solution as SolutionChatGPT
from claude_hard_321 import Solution as SolutionClaude
from gemini_hard_321 import Solution as SolutionGemini


def run_basic_tests(solution):
    
    assert solution.maxNumber([3,4,6,5], [9,1,2,5,8,3], 5) == [9,8,6,5,3]
    assert solution.maxNumber([6,7], [6,0,4], 5) == [6,7,6,0,4]
    assert solution.maxNumber([3,9], [8,9], 3) == [9,8,9]

def run_advanced_tests(solution):
    assert solution.maxNumber([6, 0, 4, 7], [6, 8], 5) == [8, 6, 0, 4, 7]
    assert solution.maxNumber([8, 3, 9, 7, 6, 0, 5, 2, 4, 1], [0, 4, 9, 7, 6, 1], 7) == [9, 9, 7, 7, 6, 6, 5]
    assert solution.maxNumber([9, 5, 3, 7, 8, 2, 4], [1, 5, 6, 2, 9, 8, 7], 7) == [9, 9, 8, 8, 7, 2, 4]
    assert solution.maxNumber([5], [9, 2, 7, 0, 8, 1, 5, 6, 3, 4], 2) == [9, 8]
    assert solution.maxNumber([5, 4, 1, 6, 7, 0, 9], [6, 8, 7, 0, 4, 5, 9, 3, 2], 10) == [9, 6, 8, 7, 0, 4, 5, 9, 3, 2]
    assert solution.maxNumber([3, 8, 5, 1, 0], [4, 0, 2, 1], 3) == [8, 5, 4]
    assert solution.maxNumber([0, 8, 3, 2, 5], [4, 1], 1) == [8]
    assert solution.maxNumber([0, 3, 5, 8, 7, 1], [8, 7, 2, 9, 5, 6, 4, 0, 3, 1], 5) == [9, 8, 7, 6, 4]
    assert solution.maxNumber([0, 3, 8, 7], [1], 2) == [8, 7]
    assert solution.maxNumber([7, 9, 6, 2, 5, 1, 0, 4], [1, 8, 0], 5) == [9, 8, 6, 5, 4]
    assert solution.maxNumber([1, 0, 2], [9, 7, 5, 1, 8, 3, 6, 2], 7) == [9, 8, 6, 2, 1, 0, 2]
    assert solution.maxNumber([6, 8, 4, 9, 7, 3, 2, 0, 5], [9, 2, 0, 1, 7, 5, 3, 8], 17) == [9, 6, 8, 4, 9, 7, 3, 2, 2, 0, 5, 0, 1, 7, 5, 3, 8]
    assert solution.maxNumber([5, 8, 6], [4, 0, 3, 6, 7, 5, 2, 9, 1, 8], 6) == [9, 5, 8, 6, 1, 8]
    assert solution.maxNumber([6, 1, 7], [2, 6], 5) == [6, 2, 6, 1, 7]
    assert solution.maxNumber([0, 2, 7, 6, 8, 5], [6, 0, 8, 3, 4, 2, 5, 7, 1, 9], 4) == [9, 7, 8, 5]
    assert solution.maxNumber([9, 3, 6, 8, 4, 1], [1, 2, 4, 3], 8) == [9, 8, 4, 1, 2, 4, 3, 1]
    assert solution.maxNumber([6, 1, 3, 5], [8, 7, 3], 4) == [8, 7, 6, 5]
    assert solution.maxNumber([6, 2, 9, 0, 7, 8, 3], [0, 4, 6, 9, 7, 3], 7) == [9, 9, 7, 8, 7, 3, 3]
    assert solution.maxNumber([9, 5, 3, 1, 8], [7, 4, 8, 9, 2, 1], 2) == [9, 9]
    assert solution.maxNumber([4, 3, 8, 5], [2, 0], 4) == [8, 5, 2, 0]
    assert solution.maxNumber([2, 3, 4, 5, 1, 7, 9, 6, 0], [7, 4, 2, 3, 1, 5, 8, 6, 9, 0], 4) == [9, 9, 6, 0]
    assert solution.maxNumber([0, 7, 8, 6], [5, 3, 8], 6) == [7, 8, 6, 5, 3, 8]
    assert solution.maxNumber([9, 2, 5, 4, 6, 1, 7, 8, 3, 0], [0, 3], 1) == [9]
    assert solution.maxNumber([6, 9, 4], [5, 2, 9, 4, 0, 3, 8, 6], 8) == [9, 9, 4, 4, 0, 3, 8, 6]
    assert solution.maxNumber([0, 3, 8, 4, 2, 6, 9, 5], [3, 4, 2, 8, 0, 5, 1, 9], 12) == [8, 6, 9, 5, 3, 4, 2, 8, 0, 5, 1, 9]
    assert solution.maxNumber([4, 7, 9, 2, 0, 1, 3], [4, 0, 8, 7, 3, 9, 1, 6, 2], 6) == [9, 9, 6, 2, 3, 2]
    assert solution.maxNumber([2, 7, 3], [7, 2, 6, 8], 7) == [7, 2, 7, 3, 2, 6, 8]
    assert solution.maxNumber([1, 0, 5, 8, 6, 3, 4], [7, 5, 2, 0], 1) == [8]
    assert solution.maxNumber([6, 7, 1], [7, 1, 3, 4], 1) == [7]
    assert solution.maxNumber([3, 1, 8], [5, 1, 9, 7, 3], 2) == [9, 8]
    assert solution.maxNumber([4, 2, 1, 7], [3, 5, 8, 1, 6], 6) == [8, 6, 4, 2, 1, 7]
    assert solution.maxNumber([7, 0, 1, 3, 5, 6, 9, 2, 4, 8], [1, 3, 6, 8, 0, 9, 7], 6) == [9, 9, 7, 2, 4, 8]
    assert solution.maxNumber([7, 3, 1, 2, 9, 5, 6, 4, 8, 0], [8, 4, 5, 1], 7) == [9, 8, 8, 4, 5, 1, 0]
    assert solution.maxNumber([6, 0], [4, 6, 3, 1, 8, 7, 9, 0, 5, 2], 5) == [9, 6, 5, 2, 0]
    assert solution.maxNumber([1, 3, 2, 0, 5, 8, 6, 7, 9], [4, 1, 5, 9, 3, 0, 2, 7], 11) == [9, 7, 1, 3, 2, 0, 5, 8, 6, 7, 9]
    assert solution.maxNumber([0], [7, 0, 6, 9, 2, 8, 1, 3, 4, 5], 9) == [7, 9, 2, 8, 1, 3, 4, 5, 0]
    assert solution.maxNumber([9, 7, 5, 6, 1, 3, 8, 2, 4, 0], [5, 6, 1, 7, 3], 7) == [9, 8, 7, 3, 2, 4, 0]
    assert solution.maxNumber([2], [8, 1, 4, 0, 9, 6, 7, 3, 5, 2], 9) == [8, 4, 9, 6, 7, 3, 5, 2, 2]
    assert solution.maxNumber([2, 9, 4, 0, 3, 8, 1, 7, 5], [9, 8, 6, 0], 3) == [9, 9, 8]
    assert solution.maxNumber([7, 9, 6, 5, 3], [8, 1, 3, 0, 2], 1) == [9]
    assert solution.maxNumber([6, 5, 8, 7, 2, 4, 3, 1, 9], [2, 1, 5, 4, 6, 8, 9], 8) == [9, 8, 7, 2, 4, 3, 1, 9]
    assert solution.maxNumber([2, 3, 7, 4, 8, 0, 6, 1], [7, 0, 8, 1, 3, 2, 4, 5], 3) == [8, 8, 6]
    assert solution.maxNumber([6], [0, 5, 1, 4, 3, 8, 6, 2, 9], 5) == [8, 6, 6, 2, 9]
    assert solution.maxNumber([5, 2], [2], 3) == [5, 2, 2]
    assert solution.maxNumber([0], [3, 8, 5, 0, 4, 6, 7, 1], 8) == [8, 5, 0, 4, 6, 7, 1, 0]
    assert solution.maxNumber([6, 8, 2, 5, 9, 1, 4, 0, 3, 7], [7], 3) == [9, 7, 7]
    assert solution.maxNumber([2, 4, 6, 3, 1], [5, 3], 1) == [6]
    assert solution.maxNumber([3, 7, 6, 5], [1, 8, 3, 4, 2, 6, 9], 3) == [9, 7, 6]
    assert solution.maxNumber([6, 0, 1, 4, 9, 2], [8, 6, 9, 0, 5, 2], 9) == [9, 6, 5, 2, 0, 1, 4, 9, 2]
    assert solution.maxNumber([4], [8, 6, 7, 3, 5, 9, 2, 4], 6) == [8, 7, 9, 4, 2, 4]
    assert solution.maxNumber([6, 7, 8, 0, 4, 1, 3, 5], [1, 9, 3], 1) == [9]
    assert solution.maxNumber([8, 4, 6, 0, 9, 5, 3, 2, 1, 7], [1], 2) == [9, 7]
    assert solution.maxNumber([5, 0, 6], [8, 0, 3, 9], 5) == [8, 9, 5, 0, 6]
    assert solution.maxNumber([7, 3, 4, 6, 9, 8, 1, 2], [8, 6, 2, 4, 9, 5, 0, 7], 7) == [9, 9, 8, 5, 7, 1, 2]
    assert solution.maxNumber([9, 6, 5, 7], [6, 9, 8], 4) == [9, 9, 8, 7]
    assert solution.maxNumber([2, 5, 6, 0, 8, 4, 3, 7, 1], [0, 8], 1) == [8]
    assert solution.maxNumber([8, 0, 2], [5, 8, 7, 6, 3, 1, 4], 4) == [8, 8, 7, 6]
    assert solution.maxNumber([0, 4, 5, 7, 6, 2, 9, 3, 8], [7, 4, 6, 5, 3, 0, 1, 8, 2, 9], 1) == [9]
    assert solution.maxNumber([7, 3, 8, 4, 0, 2], [5, 1, 3, 7, 2, 0, 9], 10) == [8, 5, 4, 3, 7, 2, 0, 9, 0, 2]
    assert solution.maxNumber([1, 6, 5, 2, 0, 8, 4], [3, 4, 2], 9) == [6, 5, 3, 4, 2, 2, 0, 8, 4]
    assert solution.maxNumber([9, 2, 4, 0], [6, 2, 1], 3) == [9, 6, 4]
    assert solution.maxNumber([7, 2, 9, 3, 4, 6, 5, 0, 1], [2, 7, 5, 4, 9, 1, 3, 6, 0], 5) == [9, 9, 6, 6, 5]
    assert solution.maxNumber([3, 4], [5], 1) == [5]
    assert solution.maxNumber([3, 5, 0, 2, 6, 4, 8, 7, 9, 1], [1, 3, 6, 9, 7, 5, 2, 8, 0, 4], 19) == [5, 1, 3, 6, 9, 7, 5, 2, 8, 0, 4, 0, 2, 6, 4, 8, 7, 9, 1]
    assert solution.maxNumber([4, 1, 9, 8, 0], [5, 3, 7, 4, 9, 1, 0, 8, 2], 5) == [9, 9, 8, 8, 2]
    assert solution.maxNumber([1, 5], [4, 6, 8, 1, 9, 0, 5, 7, 3, 2], 12) == [4, 6, 8, 1, 9, 1, 5, 0, 5, 7, 3, 2]
    assert solution.maxNumber([1, 4, 0, 5, 6], [7, 1, 6], 8) == [7, 1, 6, 1, 4, 0, 5, 6]
    assert solution.maxNumber([6, 7, 4, 5, 3, 8, 9, 1], [4, 5, 2, 6, 7], 1) == [9]
    assert solution.maxNumber([4, 7, 0], [3], 2) == [7, 3]
    assert solution.maxNumber([6, 7, 4, 8, 3, 5, 2], [7], 7) == [7, 7, 4, 8, 3, 5, 2]
    assert solution.maxNumber([7, 0, 2, 8, 3, 4], [4, 8], 4) == [8, 8, 3, 4]
    assert solution.maxNumber([2, 3, 5, 4], [9, 5, 2], 1) == [9]
    assert solution.maxNumber([9, 1, 3, 0, 8, 7, 6, 5, 4, 2], [5, 6, 2, 9, 0, 1, 3, 7, 8], 10) == [9, 9, 8, 7, 8, 7, 6, 5, 4, 2]
    assert solution.maxNumber([8, 6, 9, 7, 3, 4, 1, 0, 5, 2], [6, 7, 4], 13) == [8, 6, 9, 7, 6, 7, 4, 3, 4, 1, 0, 5, 2]
    assert solution.maxNumber([9, 1, 5, 0, 6, 7], [7, 4, 6, 0, 1, 8, 2, 5, 9, 3], 13) == [9, 7, 6, 8, 2, 5, 9, 3, 1, 5, 0, 6, 7]
    assert solution.maxNumber([4], [2, 0, 7], 2) == [7, 4]
    assert solution.maxNumber([9, 8], [8, 7, 1, 3, 0, 4, 6, 5], 10) == [9, 8, 8, 7, 1, 3, 0, 4, 6, 5]
    assert solution.maxNumber([4, 7, 2, 1], [1], 3) == [7, 2, 1]
    assert solution.maxNumber([9], [4], 1) == [9]
    assert solution.maxNumber([1], [2, 1, 8, 4, 9], 2) == [9, 1]
    assert solution.maxNumber([7, 2, 8, 9, 6, 1], [4, 5, 0, 6, 3, 7, 1, 2, 8], 6) == [9, 7, 6, 2, 8, 1]
    assert solution.maxNumber([0, 4, 7, 6, 9, 5, 8, 3], [7], 5) == [9, 7, 5, 8, 3]
    assert solution.maxNumber([8, 3, 7, 0, 9, 4, 6, 2, 5], [6, 7, 5, 0, 9, 4, 1, 2, 8, 3], 5) == [9, 9, 8, 6, 5]
    assert solution.maxNumber([5, 3, 1, 0], [1, 0, 6, 2, 3, 5, 7, 8, 9], 10) == [6, 5, 3, 5, 7, 8, 9, 3, 1, 0]
    assert solution.maxNumber([0, 1, 8, 5, 7, 3], [0, 5, 1], 9) == [0, 5, 1, 0, 1, 8, 5, 7, 3]
    assert solution.maxNumber([5, 1, 7, 3, 4, 2, 9], [5, 9, 6, 2, 8], 2) == [9, 9]
    assert solution.maxNumber([3, 9], [5], 2) == [9, 5]
    assert solution.maxNumber([9, 1, 6, 5, 8, 2, 4, 0, 3, 7], [6, 3, 7, 4], 9) == [9, 8, 7, 4, 2, 4, 0, 3, 7]
    assert solution.maxNumber([3, 8, 4, 2, 1, 5, 0], [5, 0, 9, 6, 4, 3, 8, 2, 1], 16) == [5, 3, 8, 4, 2, 1, 5, 0, 9, 6, 4, 3, 8, 2, 1, 0]
    assert solution.maxNumber([4], [4], 1) == [4]
    assert solution.maxNumber([0, 6, 9, 5, 1, 3], [3, 5, 9, 6, 4, 2, 0, 7], 14) == [3, 5, 9, 6, 4, 2, 0, 7, 0, 6, 9, 5, 1, 3]
    assert solution.maxNumber([3], [5, 3, 1], 1) == [5]
    assert solution.maxNumber([6, 0, 7, 4], [7], 3) == [7, 7, 4]
    assert solution.maxNumber([6, 4, 2, 8], [4], 3) == [6, 8, 4]
    assert solution.maxNumber([3, 4, 7, 8, 1, 2, 0, 9, 5], [5, 6, 9], 5) == [9, 8, 2, 9, 5]
    assert solution.maxNumber([5], [8, 9, 3], 2) == [9, 5]
    assert solution.maxNumber([1, 3, 9, 4, 0, 5], [1, 0, 3, 7, 5, 9], 3) == [9, 9, 5]
    assert solution.maxNumber([2], [9, 4, 7, 8, 3, 0, 2, 6, 5, 1], 2) == [9, 8]
    assert solution.maxNumber([3, 6, 2], [7, 9, 3, 1, 6, 0], 1) == [9]
    assert solution.maxNumber([3], [9], 1) == [9]
        

if __name__ == '__main__':
    import sys
    if sys.argv[1] == 'test':
        solvers = [SolutionCanon()]
        if len(sys.argv) == 3 and sys.argv[2] == 'all':
            solvers.extend([SolutionChatGPT(), SolutionClaude(),
                            SolutionGemini()])
        for solver in solvers:
            run_basic_tests(solver)
            run_advanced_tests(solver)
    elif sys.argv[1] == 'time':
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