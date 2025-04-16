from medium_376_canon import Solution as SolutionCanon
from chatgpt_medium_376 import Solution as SolutionChatGPT
from claude_medium_376 import Solution as SolutionClaude
from gemini_medium_376 import Solution as SolutionGemini


def run_basic_tests(solution):
    
    assert solution.wiggleMaxLength([1, 7, 4, 9, 2, 5]) == 6
    assert solution.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]) == 7
    assert solution.wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2

def run_advanced_tests(solution):
    assert solution.wiggleMaxLength([71, 24, 67, 64, 85, 65, 39, 68, 29, 80]) == 9
    assert solution.wiggleMaxLength([10, 57, 95, 53, 3, 2, 36]) == 4
    assert solution.wiggleMaxLength([23, 38, 64, 36, 27, 35, 53]) == 4
    assert solution.wiggleMaxLength([100, 1, 31, 40, 96, 5, 86, 73, 33, 9]) == 6
    assert solution.wiggleMaxLength([11, 29, 4, 39]) == 4
    assert solution.wiggleMaxLength([4, 89, 68]) == 3
    assert solution.wiggleMaxLength([48, 79, 37, 33, 30]) == 3
    assert solution.wiggleMaxLength([24, 27, 2, 36, 14, 81, 16, 98]) == 8
    assert solution.wiggleMaxLength([41, 47, 38, 79, 25, 60, 95, 88, 91]) == 8
    assert solution.wiggleMaxLength([44, 31, 39, 79, 51, 55]) == 5
    assert solution.wiggleMaxLength([76, 23, 59, 98, 30, 39, 66, 64, 56, 27]) == 6
    assert solution.wiggleMaxLength([14, 25, 59, 10, 68, 78, 47]) == 5
    assert solution.wiggleMaxLength([63, 80, 72, 25, 92, 38, 1, 15, 28]) == 6
    assert solution.wiggleMaxLength([45, 31, 47]) == 3
    assert solution.wiggleMaxLength([59, 88, 91, 5]) == 3
    assert solution.wiggleMaxLength([14, 94, 100, 10, 4, 50, 49, 41, 2]) == 5
    assert solution.wiggleMaxLength([27, 31, 22]) == 3
    assert solution.wiggleMaxLength([41, 88, 59]) == 3
    assert solution.wiggleMaxLength([6, 1, 88, 75, 65, 40]) == 4
    assert solution.wiggleMaxLength([11, 53, 30]) == 3
    assert solution.wiggleMaxLength([28, 85, 84, 68]) == 3
    assert solution.wiggleMaxLength([95, 23, 99, 43]) == 4
    assert solution.wiggleMaxLength([42, 64, 68, 26, 84, 71, 37, 12, 100, 77]) == 7
    assert solution.wiggleMaxLength([86, 39, 56, 75, 74, 6]) == 4
    assert solution.wiggleMaxLength([39, 45, 69, 6]) == 3
    assert solution.wiggleMaxLength([79, 57, 62, 29, 22, 52, 99, 14, 1]) == 6
    assert solution.wiggleMaxLength([22, 67, 40, 66, 23, 30, 56, 31, 88, 32]) == 9
    assert solution.wiggleMaxLength([57, 9, 42, 65]) == 3
    assert solution.wiggleMaxLength([36, 7, 51, 11]) == 4
    assert solution.wiggleMaxLength([35, 21, 99, 61, 4]) == 4
    assert solution.wiggleMaxLength([18, 76, 26, 52, 80, 21, 63, 14, 29, 22]) == 9
    assert solution.wiggleMaxLength([55, 16]) == 2
    assert solution.wiggleMaxLength([88, 61, 81]) == 3
    assert solution.wiggleMaxLength([75, 56, 11, 85, 38, 13, 81, 35]) == 6
    assert solution.wiggleMaxLength([30, 15, 69, 4, 56]) == 5
    assert solution.wiggleMaxLength([65, 76, 43, 57, 55, 26, 13, 74, 53]) == 7
    assert solution.wiggleMaxLength([93, 94]) == 2
    assert solution.wiggleMaxLength([62, 82, 40, 13, 72, 77, 68, 71, 86, 23]) == 7
    assert solution.wiggleMaxLength([60, 86, 95, 70, 48, 67, 20, 55]) == 6
    assert solution.wiggleMaxLength([83, 39, 18, 50, 13]) == 4
    assert solution.wiggleMaxLength([6, 26, 75, 15, 18, 94, 3, 35, 39]) == 6
    assert solution.wiggleMaxLength([60, 32, 61, 23, 76, 12, 62]) == 7
    assert solution.wiggleMaxLength([84, 44, 81, 29, 98, 80, 85, 41]) == 8
    assert solution.wiggleMaxLength([4, 75, 94, 58, 57, 78, 65, 14, 95]) == 6
    assert solution.wiggleMaxLength([23, 16, 53, 74, 64, 8, 90]) == 5
    assert solution.wiggleMaxLength([99, 21, 86, 10, 67, 57, 95, 69]) == 8
    assert solution.wiggleMaxLength([39, 52, 60, 77, 26, 97, 51, 50, 20, 5]) == 5
    assert solution.wiggleMaxLength([43, 68, 85, 25, 98, 34, 74, 40]) == 7
    assert solution.wiggleMaxLength([47, 48, 19, 71, 76, 32, 26]) == 5
    assert solution.wiggleMaxLength([32, 39, 64, 23, 15, 17]) == 4
    assert solution.wiggleMaxLength([90, 77]) == 2
    assert solution.wiggleMaxLength([88, 35, 16, 60, 96]) == 3
    assert solution.wiggleMaxLength([45, 9, 31, 84, 1, 49, 4, 25]) == 7
    assert solution.wiggleMaxLength([7, 32, 15, 34, 99, 20, 77, 72, 47, 16]) == 7
    assert solution.wiggleMaxLength([79, 53, 7, 19, 94, 39, 11]) == 4
    assert solution.wiggleMaxLength([36, 92, 50, 44]) == 3
    assert solution.wiggleMaxLength([22, 62]) == 2
    assert solution.wiggleMaxLength([35, 38, 73, 69]) == 3
    assert solution.wiggleMaxLength([72, 67, 65, 88, 17]) == 4
    assert solution.wiggleMaxLength([23, 64, 91, 5, 72]) == 4
    assert solution.wiggleMaxLength([69, 19, 81, 96, 51]) == 4
    assert solution.wiggleMaxLength([24, 57]) == 2
    assert solution.wiggleMaxLength([65, 90]) == 2
    assert solution.wiggleMaxLength([99, 12, 64, 33, 60, 83, 65]) == 6
    assert solution.wiggleMaxLength([40, 55, 35, 60, 64, 37, 20]) == 5
    assert solution.wiggleMaxLength([9, 28, 56, 22]) == 3
    assert solution.wiggleMaxLength([42, 29, 34, 44]) == 3
    assert solution.wiggleMaxLength([23, 97, 64, 84, 47, 81, 69, 85]) == 8
    assert solution.wiggleMaxLength([67, 86, 46, 88, 70, 31]) == 5
    assert solution.wiggleMaxLength([87, 7, 39, 54, 95, 97, 36, 69, 8, 70]) == 7
    assert solution.wiggleMaxLength([66, 34, 60]) == 3
    assert solution.wiggleMaxLength([100, 66, 38, 50, 86, 23, 7]) == 4
    assert solution.wiggleMaxLength([82, 90, 71, 29, 44]) == 4
    assert solution.wiggleMaxLength([78, 38, 28]) == 2
    assert solution.wiggleMaxLength([75, 22, 16, 27, 86, 57, 26]) == 4
    assert solution.wiggleMaxLength([16, 22, 31, 28, 23]) == 3
    assert solution.wiggleMaxLength([97, 8, 50, 63, 57]) == 4
    assert solution.wiggleMaxLength([47, 76, 74, 65, 44, 52]) == 4
    assert solution.wiggleMaxLength([4, 70, 69, 55, 59]) == 4
    assert solution.wiggleMaxLength([67, 88, 91, 2, 98]) == 4
    assert solution.wiggleMaxLength([94, 83, 37, 26, 22]) == 2
    assert solution.wiggleMaxLength([19, 34]) == 2
    assert solution.wiggleMaxLength([70, 12, 73, 94, 60, 45, 36, 33, 72]) == 5
    assert solution.wiggleMaxLength([51, 33, 42, 43]) == 3
    assert solution.wiggleMaxLength([58, 53, 8, 56, 81, 18, 29, 84, 14, 5]) == 6
    assert solution.wiggleMaxLength([19, 61, 24, 72, 14, 43, 84, 2, 11]) == 8
    assert solution.wiggleMaxLength([32, 86, 31, 26, 38, 40, 54, 28, 93]) == 6
    assert solution.wiggleMaxLength([68, 98, 16, 8, 57, 4, 49, 41, 54, 81]) == 8
    assert solution.wiggleMaxLength([21, 76, 49]) == 3
    assert solution.wiggleMaxLength([14, 33, 22, 15, 6]) == 3
    assert solution.wiggleMaxLength([49, 79, 100, 33, 67, 11]) == 5
    assert solution.wiggleMaxLength([90, 59, 71]) == 3
    assert solution.wiggleMaxLength([2, 96, 14, 100, 54, 77, 1, 55, 47, 74]) == 10
    assert solution.wiggleMaxLength([67, 12]) == 2
    assert solution.wiggleMaxLength([53, 29, 96, 58]) == 4
    assert solution.wiggleMaxLength([32, 95, 96]) == 2
    assert solution.wiggleMaxLength([91, 73, 83, 70, 63, 26, 49, 100, 64, 46]) == 6
    assert solution.wiggleMaxLength([68, 57, 58, 2, 36, 22, 88, 25, 9, 38]) == 9
    assert solution.wiggleMaxLength([96, 17, 94, 99, 39]) == 4
    assert solution.wiggleMaxLength([52, 39, 43, 22]) == 4
        

if __name__ == '__main__':
    import sys
    problem_id = 376
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

        print(f'medium_376,{sys.argv[2]},', end='')
        if problem_id == 527 and sys.argv[2] == 'claude':
            print('-- NR --')
            sys.exit(0)

        try:
            for _ in range(int(sys.argv[3])):
                start = time.time()
                run_basic_tests(solver)
                run_advanced_tests(solver)
                end = time.time()
                times.append(end - start)
        except AssertionError as err:
            print(f'Assertion Failed: {err}', file=sys.stderr)
            print('-- IR --')
            sys.exit(0)

        avg_time = statistics.mean(times)
        print(f'{avg_time:.4E}')