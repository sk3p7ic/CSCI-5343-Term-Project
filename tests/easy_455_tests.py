from easy_455_canon import Solution as SolutionCanon
from chatgpt_easy_455 import Solution as SolutionChatGPT
from claude_easy_455 import Solution as SolutionClaude
from gemini_easy_455 import Solution as SolutionGemini


def run_basic_tests(solution):
    
    assert solution.findContentChildren([1,2,3], [1,1]) == 1
    assert solution.findContentChildren([1,2], [1,2,3]) == 2

def run_advanced_tests(solution):
    assert solution.findContentChildren([42], [44, 48, 80, 98]) == 1
    assert solution.findContentChildren([11, 25, 38, 49, 86, 97, 99], []) == 0
    assert solution.findContentChildren([13], [4, 25, 36, 47, 59]) == 1
    assert solution.findContentChildren([15, 23, 27, 60, 81, 82, 95], [15]) == 1
    assert solution.findContentChildren([36, 47, 52, 56, 91, 94, 100], [65, 99, 100]) == 3
    assert solution.findContentChildren([13, 15, 46, 69, 88, 89], [2, 13, 21, 28, 62, 71, 78, 82, 100]) == 5
    assert solution.findContentChildren([3, 48, 77], []) == 0
    assert solution.findContentChildren([12, 17, 86, 89], [46]) == 1
    assert solution.findContentChildren([15, 32, 34, 57, 62, 64, 78], [2, 10, 36, 40, 56, 72, 86]) == 5
    assert solution.findContentChildren([7, 40, 43, 48, 57, 61, 72, 90, 94], []) == 0
    assert solution.findContentChildren([1, 21, 31, 32, 50, 62, 66, 83, 100], [93]) == 1
    assert solution.findContentChildren([6, 9, 10, 22, 25, 45, 59, 61, 83], [36, 50, 51, 67, 78]) == 5
    assert solution.findContentChildren([11, 24, 41, 57, 67, 76, 86, 90, 96], [7]) == 0
    assert solution.findContentChildren([2, 20, 24, 36, 38, 68, 87, 89, 94, 99], []) == 0
    assert solution.findContentChildren([2, 19, 26, 33, 60, 62, 64, 81], [5, 29, 54, 63, 69, 91]) == 6
    assert solution.findContentChildren([17, 59, 64, 72, 76], [91]) == 1
    assert solution.findContentChildren([71], [7, 13, 92]) == 1
    assert solution.findContentChildren([1, 39, 45, 67, 72], [8, 16, 18, 23, 27, 38, 60, 70, 81]) == 4
    assert solution.findContentChildren([22, 56], [1, 40, 50, 67, 94]) == 2
    assert solution.findContentChildren([40, 42, 43, 59, 71, 90, 99], [6, 8, 20, 40, 66, 67, 70, 77, 81, 92]) == 6
    assert solution.findContentChildren([37], [5, 6, 63, 74, 96, 98]) == 1
    assert solution.findContentChildren([19], [47]) == 1
    assert solution.findContentChildren([7, 12, 19, 47, 53, 63, 78, 92, 97], [13, 16, 20, 26, 27, 28, 46, 56, 69, 71]) == 6
    assert solution.findContentChildren([2, 11, 29, 38, 52, 66, 76, 90, 93, 95], [13, 20, 42, 64, 81, 87, 99]) == 7
    assert solution.findContentChildren([77], []) == 0
    assert solution.findContentChildren([52, 83], [11, 33, 53, 61]) == 1
    assert solution.findContentChildren([28, 44, 72, 90, 94], [8, 15, 16, 84, 97]) == 2
    assert solution.findContentChildren([10], [28, 48, 65, 73, 81, 83, 91, 92]) == 1
    assert solution.findContentChildren([15, 21], []) == 0
    assert solution.findContentChildren([6, 8, 9, 16, 17, 25, 28, 41, 53], [11, 43]) == 2
    assert solution.findContentChildren([7, 81], [3, 6, 32, 34, 37, 43, 67, 70, 82, 98]) == 2
    assert solution.findContentChildren([55], [8, 26, 48, 53, 56, 68, 77, 99]) == 1
    assert solution.findContentChildren([18, 53, 65, 74, 78, 80, 93], [67, 69, 71, 72, 94]) == 4
    assert solution.findContentChildren([25, 35, 79], [33, 34, 70, 100]) == 3
    assert solution.findContentChildren([27, 32, 45, 57, 64, 65, 87, 95], [2, 7, 51, 93, 98]) == 3
    assert solution.findContentChildren([3, 18, 33, 85], [30, 37]) == 2
    assert solution.findContentChildren([37, 62], [20, 22, 26, 74, 91, 100]) == 2
    assert solution.findContentChildren([2, 8, 11, 25, 72, 82, 84], [3, 4, 17, 52, 90, 95]) == 5
    assert solution.findContentChildren([90], [1, 2, 20, 31, 57, 62, 89, 99]) == 1
    assert solution.findContentChildren([13, 22, 25, 59, 62, 66, 72, 75, 90], [15, 26, 48, 60, 63, 67, 87, 92]) == 8
    assert solution.findContentChildren([10, 21, 27, 50, 52, 54, 75, 78, 87], [5, 26, 44, 49, 59, 97]) == 5
    assert solution.findContentChildren([51, 60, 66, 91], [44, 45, 74, 85, 93, 99]) == 4
    assert solution.findContentChildren([9, 18, 24, 49, 53, 61, 63, 84, 95], [16]) == 1
    assert solution.findContentChildren([40, 93], [58, 59, 66]) == 1
    assert solution.findContentChildren([6, 8, 9, 48, 56, 63, 75, 79, 81], [32, 52, 57]) == 3
    assert solution.findContentChildren([23, 40, 43, 58, 80, 89], [4, 8, 10, 18, 86, 90]) == 2
    assert solution.findContentChildren([7, 15, 23, 45, 47, 48, 50, 62, 77], [10, 20, 25]) == 3
    assert solution.findContentChildren([28], [20]) == 0
    assert solution.findContentChildren([15, 16, 44, 45, 47, 56, 94, 96, 97], [20, 32, 35, 90]) == 3
    assert solution.findContentChildren([10, 24, 55, 65, 72, 74, 86, 90, 92, 93], [2, 9, 10, 24, 53, 55, 85]) == 4
    assert solution.findContentChildren([13, 34, 65, 85], [3, 15, 23, 37, 51, 58, 76, 85, 94]) == 4
    assert solution.findContentChildren([9, 10, 25, 37, 50, 77, 87, 92, 95, 96], []) == 0
    assert solution.findContentChildren([42, 88, 92], [40, 63, 71, 89, 91, 93, 99, 100]) == 3
    assert solution.findContentChildren([15, 22, 27, 36, 53, 66, 80, 97], [12, 44, 88]) == 2
    assert solution.findContentChildren([17, 27, 61, 65, 78, 93], [50, 83]) == 2
    assert solution.findContentChildren([18, 28, 32, 55, 88, 92, 99], []) == 0
    assert solution.findContentChildren([2, 29, 41, 56, 63, 72], [1, 2, 6, 20, 22, 24, 26, 46, 61, 66]) == 4
    assert solution.findContentChildren([26, 27, 36, 43, 70, 85, 91, 93], [23, 30, 31, 39, 42, 47, 57, 65, 70, 97]) == 6
    assert solution.findContentChildren([7, 25], [34, 35, 38, 49, 67, 98]) == 2
    assert solution.findContentChildren([11, 25, 31, 33, 44, 55, 57, 60, 68], [13, 17, 82, 99]) == 3
    assert solution.findContentChildren([38, 45, 65, 71], [10, 28, 40, 42, 54, 57, 64, 65, 66, 79]) == 4
    assert solution.findContentChildren([7, 19, 33, 35, 36, 89], [5, 48, 65]) == 2
    assert solution.findContentChildren([59], [54, 64, 89]) == 1
    assert solution.findContentChildren([2, 15, 27, 91], []) == 0
    assert solution.findContentChildren([4, 23, 26, 30, 65, 66, 69, 80, 86], [37, 42, 94]) == 3
    assert solution.findContentChildren([15, 26, 45, 86, 91], [34, 57]) == 2
    assert solution.findContentChildren([31, 53, 63, 80, 96, 100], [21, 91]) == 1
    assert solution.findContentChildren([8, 17, 20, 35, 37, 43, 72], []) == 0
    assert solution.findContentChildren([12, 40, 44, 60, 64, 66, 67, 69, 74], [42, 47, 79, 100]) == 4
    assert solution.findContentChildren([21, 38], [26, 44, 75, 85, 86]) == 2
    assert solution.findContentChildren([11, 18, 39, 50, 60, 71, 72, 88, 92, 96], [18, 23, 45, 56, 57, 87]) == 5
    assert solution.findContentChildren([17, 43, 47, 49, 52, 64, 73, 79], [21, 46, 59, 61, 77, 95]) == 6
    assert solution.findContentChildren([12, 29, 48, 63, 82, 84, 85, 98], [53, 95, 100]) == 3
    assert solution.findContentChildren([6, 25, 52, 81, 87, 92], [20, 21, 97]) == 2
    assert solution.findContentChildren([12, 16, 37, 47, 50, 58, 65, 73, 79, 82], [9, 17, 19, 23, 52, 66, 86, 88]) == 6
    assert solution.findContentChildren([3, 16, 25, 30, 32, 65, 66, 80, 85, 96], [15, 21, 25, 46, 85]) == 5
    assert solution.findContentChildren([15, 16, 28, 59, 73, 89, 98], [14, 15, 52, 68]) == 3
    assert solution.findContentChildren([26, 55], [3, 11, 23, 24, 34, 49, 60, 87]) == 2
    assert solution.findContentChildren([14, 59, 72, 80], [34]) == 1
    assert solution.findContentChildren([20, 98], [5, 35, 43, 59, 65, 86, 87]) == 1
    assert solution.findContentChildren([28, 94], [13]) == 0
    assert solution.findContentChildren([15, 24, 30, 53, 60, 61, 63, 93], [99]) == 1
    assert solution.findContentChildren([21, 22, 32, 33, 46, 58, 63, 87], [8, 23, 73, 74, 80, 90]) == 5
    assert solution.findContentChildren([7, 43, 58, 66, 67, 80, 95, 97], [70, 79]) == 2
    assert solution.findContentChildren([58, 61, 73, 77, 81], [5, 21, 27, 35, 42, 56, 84, 96]) == 2
    assert solution.findContentChildren([8, 10, 13, 51, 59, 77, 86, 92], [1, 9, 21, 48]) == 3
    assert solution.findContentChildren([1, 5, 6, 9, 29, 42, 94], [23, 32, 48, 51, 58, 62, 89]) == 6
    assert solution.findContentChildren([36, 59, 63], [72, 85, 99]) == 3
    assert solution.findContentChildren([27], [26, 52]) == 1
    assert solution.findContentChildren([2, 11, 13, 33, 38, 42, 52, 60], [9]) == 1
    assert solution.findContentChildren([1, 5, 15, 30, 38, 52, 54, 70], [32, 55, 59, 89]) == 4
    assert solution.findContentChildren([12, 34, 52, 54, 62, 73, 80, 86, 94, 95], [35, 46, 87]) == 3
    assert solution.findContentChildren([6, 13, 19, 39, 50, 66, 84, 87], [59, 67, 95, 96]) == 4
    assert solution.findContentChildren([30, 74], [5, 25, 52, 60, 69, 77, 95, 96]) == 2
    assert solution.findContentChildren([23, 24, 64, 71, 86], []) == 0
    assert solution.findContentChildren([10, 18, 21, 57, 61, 88], [19, 21, 23, 44, 50, 60, 98]) == 5
    assert solution.findContentChildren([88], [13, 25, 29, 45, 57, 95]) == 1
    assert solution.findContentChildren([16, 23, 24, 35, 37, 46, 59, 97], [19, 66, 97, 99]) == 4
    assert solution.findContentChildren([4, 6, 10, 20, 23, 56, 57, 80], [8, 15, 37, 45, 69]) == 5
    assert solution.findContentChildren([8, 81, 93, 96], []) == 0
        

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
        solver = {
            'canon': SolutionCanon,
            'chatgpt': SolutionChatGPT,
            'claude': SolutionClaude,
            'gemini': SolutionGemini,
        }[sys.argv[2]]()
        times = []

        print(f'easy_455,{sys.argv[2]},', end='')
        try:
            for _ in range(int(sys.argv[3])):
                start = time.time()
                run_basic_tests(solver)
                run_advanced_tests(solver)
                end = time.time()
                times.append(end - start)
        except AssertionError as err:
            print(f'Assertion Failed: {err}', file=sys.stderr)
            print('------')

        avg_time = statistics.mean(times)
        print(f'{avg_time:.4E}')