from easy_605_canon import Solution as SolutionCanon

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
