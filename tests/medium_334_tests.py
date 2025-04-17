from medium_334_canon import Solution as SolutionCanon
from chatgpt_medium_334 import Solution as SolutionChatGPT
from claude_medium_334 import Solution as SolutionClaude
from gemini_medium_334 import Solution as SolutionGemini


def run_basic_tests(solution):
    
    assert solution.increasingTriplet([1,2,3,4,5]) == True
    assert solution.increasingTriplet([5,4,3,2,1]) == False
    assert solution.increasingTriplet([2,1,5,0,4,6]) == True

def run_advanced_tests(solution):
    assert solution.increasingTriplet([71, 63, 86]) == False
    assert solution.increasingTriplet([16, 23, 13, 86]) == True
    assert solution.increasingTriplet([74, 86, 49, 61, 3, 39, 45, 20, 73, 75]) == True
    assert solution.increasingTriplet([56, 61, 80, 38, 40, 20, 62, 72, 51]) == True
    assert solution.increasingTriplet([60, 100, 7, 2, 90, 21, 22]) == True
    assert solution.increasingTriplet([58, 77, 50, 17, 62, 67, 13, 40, 53]) == True
    assert solution.increasingTriplet([21, 4, 14, 76, 94]) == True
    assert solution.increasingTriplet([78, 36, 35]) == False
    assert solution.increasingTriplet([62, 25, 17, 52, 97, 91, 85]) == True
    assert solution.increasingTriplet([20, 19, 4]) == False
    assert solution.increasingTriplet([7, 48, 91, 65, 86, 80, 1, 56]) == True
    assert solution.increasingTriplet([32, 76, 85, 36, 75, 64, 50]) == True
    assert solution.increasingTriplet([44, 16, 84, 74, 81, 6]) == True
    assert solution.increasingTriplet([46, 99, 68, 9]) == False
    assert solution.increasingTriplet([78, 51, 53, 82, 45, 88, 90, 66]) == True
    assert solution.increasingTriplet([14, 36, 50, 15, 55, 52, 6]) == True
    assert solution.increasingTriplet([82, 5, 90, 94, 81, 67, 42, 36, 46, 73]) == True
    assert solution.increasingTriplet([59, 83, 13, 32, 26]) == False
    assert solution.increasingTriplet([14, 20, 43, 71, 93, 39, 81, 54, 61, 44]) == True
    assert solution.increasingTriplet([50, 93, 1, 57, 12, 60, 43]) == True
    assert solution.increasingTriplet([28, 18, 11, 10, 34, 3, 9, 48, 68, 97]) == True
    assert solution.increasingTriplet([68, 4, 47, 37]) == False
    assert solution.increasingTriplet([62, 1, 11, 71, 7, 38]) == True
    assert solution.increasingTriplet([2, 91, 80, 97]) == True
    assert solution.increasingTriplet([36, 67, 93, 78, 3, 94, 46, 76, 60, 41]) == True
    assert solution.increasingTriplet([59, 72, 71, 24, 35]) == False
    assert solution.increasingTriplet([58, 19, 57, 32]) == False
    assert solution.increasingTriplet([89, 31, 13, 92, 42, 73, 97, 46]) == True
    assert solution.increasingTriplet([39, 24, 80, 11]) == False
    assert solution.increasingTriplet([29, 71, 45, 32, 6]) == False
    assert solution.increasingTriplet([98, 11, 42, 24, 77, 38]) == True
    assert solution.increasingTriplet([71, 44, 90, 13, 18, 34]) == True
    assert solution.increasingTriplet([71, 92, 97, 2]) == True
    assert solution.increasingTriplet([88, 96, 47, 25, 71, 15, 43, 7, 85, 64]) == True
    assert solution.increasingTriplet([87, 60, 39, 44, 26, 80]) == True
    assert solution.increasingTriplet([81, 50, 38, 64]) == False
    assert solution.increasingTriplet([47, 53, 4, 7, 3, 5, 22, 78, 44, 18]) == True
    assert solution.increasingTriplet([99, 2, 62, 52, 72, 1, 76]) == True
    assert solution.increasingTriplet([20, 54, 91, 41, 100, 52]) == True
    assert solution.increasingTriplet([75, 4, 84, 66, 72, 42, 34, 61, 22]) == True
    assert solution.increasingTriplet([2, 42, 14, 90, 60, 70]) == True
    assert solution.increasingTriplet([84, 76, 27, 23, 12, 52, 36, 47, 45]) == True
    assert solution.increasingTriplet([91, 36, 85]) == False
    assert solution.increasingTriplet([68, 55, 29, 93, 20, 33, 24, 40, 16, 76]) == True
    assert solution.increasingTriplet([3, 54, 1, 6, 88, 58, 62, 12, 11, 5]) == True
    assert solution.increasingTriplet([42, 63, 12]) == False
    assert solution.increasingTriplet([84, 38, 9, 5, 67]) == False
    assert solution.increasingTriplet([15, 27, 1, 13, 73, 64, 55, 43]) == True
    assert solution.increasingTriplet([91, 3, 76, 30, 33, 54]) == True
    assert solution.increasingTriplet([27, 81, 62, 95, 72, 79, 55, 97, 30]) == True
    assert solution.increasingTriplet([66, 73, 45, 28, 9, 57, 52, 55, 40, 23]) == True
    assert solution.increasingTriplet([83, 98, 42, 86, 8, 31, 92, 85, 13, 15]) == True
    assert solution.increasingTriplet([36, 6, 19, 30, 13, 54, 1, 29, 41, 21]) == True
    assert solution.increasingTriplet([82, 67, 69, 1, 93]) == True
    assert solution.increasingTriplet([20, 4, 71, 31]) == False
    assert solution.increasingTriplet([36, 50, 91, 86, 29, 3, 2, 40]) == True
    assert solution.increasingTriplet([22, 60, 76, 55, 12, 4, 44, 94, 81]) == True
    assert solution.increasingTriplet([81, 52, 75]) == False
    assert solution.increasingTriplet([23, 6, 18, 15, 73, 67, 79, 35, 83]) == True
    assert solution.increasingTriplet([10, 6, 63, 59, 48, 29, 70]) == True
    assert solution.increasingTriplet([67, 84, 28, 10, 87, 30, 33]) == True
    assert solution.increasingTriplet([6, 55, 79, 60, 47]) == True
    assert solution.increasingTriplet([2, 12, 52, 29, 65, 66]) == True
    assert solution.increasingTriplet([99, 35, 3, 19, 20, 76]) == True
    assert solution.increasingTriplet([6, 88, 98]) == True
    assert solution.increasingTriplet([44, 42, 29]) == False
    assert solution.increasingTriplet([88, 10, 72, 71, 82, 99, 76]) == True
    assert solution.increasingTriplet([48, 50, 28, 36, 47, 40, 22, 93]) == True
    assert solution.increasingTriplet([90, 86, 28, 8, 82, 48, 62, 11, 38]) == True
    assert solution.increasingTriplet([81, 100, 3]) == False
    assert solution.increasingTriplet([7, 22, 87, 77]) == True
    assert solution.increasingTriplet([79, 43, 47]) == False
    assert solution.increasingTriplet([75, 44, 74, 100, 96, 28, 7, 3]) == True
    assert solution.increasingTriplet([96, 78, 66, 35, 52, 72, 82]) == True
    assert solution.increasingTriplet([14, 32, 16, 63]) == True
    assert solution.increasingTriplet([45, 36, 16, 64, 70, 98, 73, 66, 1, 46]) == True
    assert solution.increasingTriplet([81, 44, 54, 22, 84, 24]) == True
    assert solution.increasingTriplet([50, 64, 44, 20, 17, 12, 91, 53, 26]) == True
    assert solution.increasingTriplet([48, 53, 38, 80, 69, 68, 70]) == True
    assert solution.increasingTriplet([1, 78, 76, 30, 99, 95, 13, 9, 73]) == True
    assert solution.increasingTriplet([52, 74, 85, 26, 99]) == True
    assert solution.increasingTriplet([82, 79, 62, 83, 31, 84, 70]) == True
    assert solution.increasingTriplet([14, 38, 40, 12, 97, 90, 67, 59]) == True
    assert solution.increasingTriplet([36, 99, 82, 94, 61, 63, 70, 64, 17]) == True
    assert solution.increasingTriplet([86, 67, 87, 1]) == False
    assert solution.increasingTriplet([45, 18, 17, 94, 75, 88]) == True
    assert solution.increasingTriplet([22, 10, 17, 94, 38, 58]) == True
    assert solution.increasingTriplet([56, 63, 24, 49, 11, 79, 97, 20]) == True
    assert solution.increasingTriplet([1, 93, 65, 98, 61, 76, 27, 78, 10, 56]) == True
    assert solution.increasingTriplet([72, 8, 46, 30, 43, 97, 39]) == True
    assert solution.increasingTriplet([11, 68, 6]) == False
    assert solution.increasingTriplet([20, 71, 39, 4, 62, 33, 85, 97, 82, 78]) == True
    assert solution.increasingTriplet([74, 97, 33, 41, 55, 35, 25, 20, 44]) == True
    assert solution.increasingTriplet([86, 82, 63, 9, 32, 80, 94]) == True
    assert solution.increasingTriplet([84, 15, 86, 81, 2, 97, 87]) == True
    assert solution.increasingTriplet([28, 47, 58, 16, 95, 60, 98, 71]) == True
    assert solution.increasingTriplet([17, 94, 40, 63, 12, 29, 98, 77, 65, 64]) == True
    assert solution.increasingTriplet([15, 70, 5, 95]) == True
    assert solution.increasingTriplet([9, 31, 4, 85, 93, 83, 92]) == True
    assert solution.increasingTriplet([80, 20, 59, 34, 97, 19, 35, 72, 93]) == True

def run_timed_tests(solution):
    assert solution.increasingTriplet([71, 63, 86]) == False
    assert solution.increasingTriplet([16, 23, 13, 86]) == True
    assert solution.increasingTriplet([74, 86, 49, 61, 3, 39, 45, 20, 73, 75]) == True
    assert solution.increasingTriplet([56, 61, 80, 38, 40, 20, 62, 72, 51]) == True
    assert solution.increasingTriplet([60, 100, 7, 2, 90, 21, 22]) == True
    assert solution.increasingTriplet([58, 77, 50, 17, 62, 67, 13, 40, 53]) == True
    assert solution.increasingTriplet([21, 4, 14, 76, 94]) == True
    assert solution.increasingTriplet([78, 36, 35]) == False
    assert solution.increasingTriplet([62, 25, 17, 52, 97, 91, 85]) == True
    assert solution.increasingTriplet([20, 19, 4]) == False
        

if __name__ == '__main__':
    import sys
    problem_id = 334
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

        print(f'medium_334,{sys.argv[2]},', end='')
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
            print(f'Assertion Failed: {err}', file=sys.stderr)
            print('-- IR --')
            sys.exit(0)

        avg_time = statistics.mean(times)
        print(f'{avg_time:.4E}')