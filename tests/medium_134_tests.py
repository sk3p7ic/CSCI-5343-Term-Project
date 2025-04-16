from medium_134_canon import Solution as SolutionCanon
from chatgpt_medium_134 import Solution as SolutionChatGPT
from claude_medium_134 import Solution as SolutionClaude
from gemini_medium_134 import Solution as SolutionGemini


def run_basic_tests(solution):
    
    assert solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert solution.canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1

def run_advanced_tests(solution):
    assert solution.canCompleteCircuit([69, 80, 53, 31, 63, 99, 40, 45, 46], [42, 80, 50, 5, 46, 94, 99, 41, 45]) == 8
    assert solution.canCompleteCircuit([59, 49, 36, 84, 16, 14, 1, 40, 98], [9, 66, 19, 28, 53, 27, 5, 6, 18]) == 8
    assert solution.canCompleteCircuit([77, 6, 75], [36, 35, 66]) == 2
    assert solution.canCompleteCircuit([13, 26], [53, 44]) == -1
    assert solution.canCompleteCircuit([36, 81, 74, 88, 50, 37], [29, 65, 77, 59, 21, 92]) == 3
    assert solution.canCompleteCircuit([71, 19, 12, 61, 10, 68, 50], [56, 87, 78, 71, 57, 10, 21]) == -1
    assert solution.canCompleteCircuit([5, 24, 84], [3, 56, 60]) == -1
    assert solution.canCompleteCircuit([80, 35, 41, 100], [12, 98, 31, 80]) == 3
    assert solution.canCompleteCircuit([62, 87, 42, 7], [66, 93, 17, 6]) == 2
    assert solution.canCompleteCircuit([12, 36], [24, 46]) == -1
    assert solution.canCompleteCircuit([65, 76], [93, 26]) == 1
    assert solution.canCompleteCircuit([13, 93, 71, 17, 60, 11, 4, 54, 96, 5], [24, 73, 25, 97, 81, 51, 100, 78, 90, 98]) == -1
    assert solution.canCompleteCircuit([67, 52, 2, 33, 6, 86, 39, 74, 19, 15], [55, 27, 90, 52, 93, 21, 77, 33, 76, 99]) == -1
    assert solution.canCompleteCircuit([30, 7, 34, 45, 72, 25, 58], [4, 14, 45, 22, 64, 31, 33]) == 6
    assert solution.canCompleteCircuit([95, 6, 70, 72, 45, 33, 28, 19, 92], [74, 65, 30, 23, 41, 72, 27, 10, 46]) == 8
    assert solution.canCompleteCircuit([31, 16, 57], [10, 41, 13]) == 2
    assert solution.canCompleteCircuit([17, 37, 88, 79, 54, 43, 92, 52, 42, 75], [3, 91, 57, 74, 76, 77, 56, 58, 69, 72]) == -1
    assert solution.canCompleteCircuit([25, 38], [17, 16]) == 1
    assert solution.canCompleteCircuit([52, 74, 97], [43, 15, 6]) == 2
    assert solution.canCompleteCircuit([9, 1, 12, 42, 10, 23], [15, 42, 26, 58, 37, 65]) == -1
    assert solution.canCompleteCircuit([41, 97, 14, 87, 25, 28, 19, 51, 34, 73], [33, 56, 65, 7, 5, 36, 83, 24, 8, 28]) == 9
    assert solution.canCompleteCircuit([17, 83, 100, 1, 95, 91, 60, 2, 98], [95, 84, 13, 17, 68, 51, 63, 15, 72]) == 2
    assert solution.canCompleteCircuit([4, 8, 81, 63, 47, 68, 83, 67, 48, 78], [49, 97, 41, 62, 44, 55, 46, 33, 22, 5]) == 6
    assert solution.canCompleteCircuit([48, 85, 90, 1, 45, 34, 57, 25, 96, 5], [80, 17, 7, 72, 26, 37, 24, 99, 21, 76]) == 1
    assert solution.canCompleteCircuit([31, 55, 81, 51, 73, 10, 3], [44, 82, 72, 39, 14, 4, 95]) == -1
    assert solution.canCompleteCircuit([87, 44], [30, 7]) == 1
    assert solution.canCompleteCircuit([83, 41, 38, 5, 33, 26, 52, 27, 1, 21], [64, 65, 60, 68, 53, 2, 51, 18, 56, 43]) == -1
    assert solution.canCompleteCircuit([28, 40, 93, 63], [31, 8, 25, 98]) == 2
    assert solution.canCompleteCircuit([39, 62, 51, 67, 23, 48, 79], [64, 94, 68, 75, 17, 53, 25]) == -1
    assert solution.canCompleteCircuit([62, 77, 31, 35, 63, 40, 32, 58, 61], [95, 29, 76, 48, 38, 17, 2, 49, 75]) == 5
    assert solution.canCompleteCircuit([80, 19, 7, 97, 60, 62], [22, 24, 47, 76, 77, 98]) == -1
    assert solution.canCompleteCircuit([43, 72, 100, 83, 88, 24, 8, 22], [38, 5, 33, 68, 30, 25, 7, 12]) == 7
    assert solution.canCompleteCircuit([94, 60, 39, 22, 69, 7, 81], [68, 22, 52, 15, 3, 88, 62]) == 6
    assert solution.canCompleteCircuit([63, 95, 76, 30, 92, 86, 36, 89], [75, 82, 29, 74, 91, 73, 3, 42]) == 7
    assert solution.canCompleteCircuit([86, 27, 16], [90, 22, 34]) == -1
    assert solution.canCompleteCircuit([15, 12, 44, 78, 59, 54, 6, 90], [60, 65, 89, 27, 39, 46, 56, 58]) == -1
    assert solution.canCompleteCircuit([91, 84, 40, 69, 48, 74, 29], [41, 86, 8, 6, 87, 47, 30]) == 5
    assert solution.canCompleteCircuit([57, 27], [30, 18]) == 1
    assert solution.canCompleteCircuit([20, 11, 98, 71], [100, 78, 39, 13]) == -1
    assert solution.canCompleteCircuit([76, 65, 10], [78, 55, 14]) == 1
    assert solution.canCompleteCircuit([34, 41, 100, 67, 42, 40, 48, 52], [79, 77, 25, 63, 36, 56, 64, 23]) == 2
    assert solution.canCompleteCircuit([53, 25, 82, 39], [45, 36, 32, 26]) == 3
    assert solution.canCompleteCircuit([99, 65, 3, 9, 97, 93], [81, 9, 78, 20, 67, 85]) == 4
    assert solution.canCompleteCircuit([23, 51, 66, 92, 85, 10], [92, 64, 59, 4, 57, 35]) == 3
    assert solution.canCompleteCircuit([51, 49, 48, 10, 66, 9], [74, 52, 71, 38, 18, 61]) == -1
    assert solution.canCompleteCircuit([91, 54, 70, 20, 38, 21], [97, 83, 40, 28, 14, 41]) == -1
    assert solution.canCompleteCircuit([11, 78, 17], [70, 60, 39]) == -1
    assert solution.canCompleteCircuit([90, 20, 43, 53, 75, 42, 29, 97, 13], [78, 56, 63, 8, 98, 54, 51, 35, 92]) == -1
    assert solution.canCompleteCircuit([100, 15, 13, 9, 40, 28, 52, 8, 21], [89, 39, 76, 8, 21, 100, 64, 11, 43]) == -1
    assert solution.canCompleteCircuit([50, 95, 84], [18, 20, 95]) == 1
    assert solution.canCompleteCircuit([84, 1, 58], [7, 67, 18]) == 2
    assert solution.canCompleteCircuit([79, 51, 36, 42, 37], [98, 82, 58, 88, 38]) == -1
    assert solution.canCompleteCircuit([100, 2, 60, 9, 33, 16], [4, 27, 78, 99, 11, 16]) == -1
    assert solution.canCompleteCircuit([24, 97, 21, 50, 94, 59, 86], [53, 99, 67, 41, 74, 96, 95]) == -1
    assert solution.canCompleteCircuit([93, 7, 74, 11, 39, 82], [96, 3, 58, 54, 41, 40]) == 5
    assert solution.canCompleteCircuit([45, 56, 69, 47, 28, 89, 1], [34, 12, 14, 89, 31, 73, 5]) == 5
    assert solution.canCompleteCircuit([49, 31, 50, 56, 40, 22], [65, 55, 60, 19, 63, 68]) == -1
    assert solution.canCompleteCircuit([92, 20, 40, 58, 73, 16, 34], [88, 79, 61, 44, 35, 52, 30]) == -1
    assert solution.canCompleteCircuit([38, 90, 57, 44, 62], [13, 82, 78, 92, 9]) == 4
    assert solution.canCompleteCircuit([67, 15, 74, 5, 28, 20, 46, 11, 48, 49], [20, 93, 41, 72, 53, 100, 59, 75, 8, 49]) == -1
    assert solution.canCompleteCircuit([93, 13, 66, 10, 86, 97, 55, 58], [25, 100, 51, 45, 87, 27, 12, 88]) == 5
    assert solution.canCompleteCircuit([32, 99, 50, 71, 52, 61, 55, 14], [20, 98, 90, 97, 42, 3, 85, 92]) == -1
    assert solution.canCompleteCircuit([82, 83, 54, 96, 65, 30, 9], [62, 85, 64, 49, 38, 39, 25]) == 4
    assert solution.canCompleteCircuit([59, 75, 28], [75, 40, 64]) == -1
    assert solution.canCompleteCircuit([7, 89, 2], [53, 42, 41]) == -1
    assert solution.canCompleteCircuit([6, 29, 77], [44, 41, 14]) == 2
    assert solution.canCompleteCircuit([7, 85, 27, 62, 94, 15, 46], [30, 75, 82, 99, 68, 53, 70]) == -1
    assert solution.canCompleteCircuit([81, 99], [74, 87]) == 1
    assert solution.canCompleteCircuit([18, 38, 90, 4, 20, 99], [17, 84, 32, 15, 79, 91]) == -1
    assert solution.canCompleteCircuit([42, 2, 39, 83, 47, 97, 1, 49, 23, 58], [89, 8, 44, 73, 90, 50, 14, 41, 74, 11]) == -1
    assert solution.canCompleteCircuit([71, 42, 12, 16, 3], [45, 46, 60, 33, 94]) == -1
    assert solution.canCompleteCircuit([3, 57, 70, 19, 75, 77, 55], [55, 2, 20, 21, 81, 71, 61]) == 1
    assert solution.canCompleteCircuit([25, 71, 62, 78, 52, 23, 2, 79, 40, 5], [23, 77, 31, 62, 57, 76, 51, 69, 9, 71]) == -1
    assert solution.canCompleteCircuit([60, 88, 22, 25, 96, 89, 62], [74, 70, 44, 2, 19, 1, 35]) == 6
    assert solution.canCompleteCircuit([13, 15, 2, 80, 16, 6, 46, 25, 11, 30], [57, 44, 47, 90, 84, 85, 75, 7, 35, 73]) == -1
    assert solution.canCompleteCircuit([55, 37, 5, 86, 60, 78], [95, 56, 27, 30, 96, 75]) == -1
    assert solution.canCompleteCircuit([37, 15, 80], [88, 84, 68]) == -1
    assert solution.canCompleteCircuit([22, 74, 66, 94, 69], [92, 43, 10, 28, 35]) == 3
    assert solution.canCompleteCircuit([82, 43, 57, 7, 88, 46, 66], [90, 50, 46, 74, 91, 67, 38]) == -1
    assert solution.canCompleteCircuit([24, 18, 65], [25, 35, 19]) == 2
    assert solution.canCompleteCircuit([68, 66, 23, 99, 65, 69, 83, 73], [69, 98, 19, 24, 60, 33, 96, 34]) == 7
    assert solution.canCompleteCircuit([41, 23, 89], [65, 77, 100]) == -1
    assert solution.canCompleteCircuit([53, 69, 81, 42, 17, 85], [9, 8, 50, 16, 91, 73]) == 5
    assert solution.canCompleteCircuit([86, 6, 7, 96, 2, 98, 56], [30, 44, 61, 73, 53, 2, 29]) == 5
    assert solution.canCompleteCircuit([57, 24], [93, 65]) == -1
    assert solution.canCompleteCircuit([6, 27, 70, 37, 77, 60], [17, 45, 47, 31, 29, 33]) == 4
    assert solution.canCompleteCircuit([62, 74, 14, 90], [15, 51, 43, 62]) == 3
    assert solution.canCompleteCircuit([25, 10, 29, 22, 28], [86, 72, 96, 78, 100]) == -1
    assert solution.canCompleteCircuit([27, 21, 16, 100, 78, 98, 71, 14, 13], [18, 17, 59, 31, 66, 19, 63, 48, 58]) == 3
    assert solution.canCompleteCircuit([9, 7, 90, 91, 94, 18, 31], [75, 43, 50, 73, 7, 38, 34]) == 2
    assert solution.canCompleteCircuit([63, 24, 42], [58, 8, 64]) == -1
    assert solution.canCompleteCircuit([28, 41, 23], [99, 33, 94]) == -1
    assert solution.canCompleteCircuit([2, 46, 23], [92, 55, 43]) == -1
    assert solution.canCompleteCircuit([55, 76], [41, 16]) == 1
    assert solution.canCompleteCircuit([60, 20, 82, 23], [16, 41, 38, 4]) == 3
    assert solution.canCompleteCircuit([71, 36], [33, 90]) == -1
    assert solution.canCompleteCircuit([42, 88, 48, 41, 45, 28], [38, 62, 28, 5, 78, 39]) == 2
    assert solution.canCompleteCircuit([59, 29, 85, 84, 13, 88, 64, 39, 56], [100, 13, 58, 91, 64, 45, 22, 43, 25]) == 6
    assert solution.canCompleteCircuit([73, 78], [30, 91]) == 0
    assert solution.canCompleteCircuit([60, 95, 87, 78, 8, 50, 34, 2, 1, 72], [92, 47, 42, 73, 57, 77, 49, 34, 55, 19]) == -1
        

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

        print(f'medium_134,{sys.argv[2]},', end='')
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