from easy_1013_canon import Solution as SolutionCanon

def run_basic_tests(solution):
    
    assert solution.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]) == True
    assert solution.canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]) == False
    assert solution.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]) == True
    


def run_advanced_tests(solution):
    assert solution.canThreePartsEqualSum([21, 91, 16, 58, 73, 50, 24, 85]) == False
    assert solution.canThreePartsEqualSum([58, 80, 50, 31, 18, 75, 68, 15]) == False
    assert solution.canThreePartsEqualSum([34, 11, 3, 65]) == False
    assert solution.canThreePartsEqualSum([1, 39, 71, 42, 15, 59, 92, 47, 95]) == False
    assert solution.canThreePartsEqualSum([55, 26, 33, 52, 50, 39, 75, 16, 82, 22]) == False
    assert solution.canThreePartsEqualSum([87, 47, 22, 52, 37]) == False
    assert solution.canThreePartsEqualSum([32, 34, 13, 87, 6, 15, 21]) == False
    assert solution.canThreePartsEqualSum([56, 15, 60, 85, 99, 18, 75]) == False
    assert solution.canThreePartsEqualSum([78, 50, 67, 25, 42, 38, 39, 97, 28]) == False
    assert solution.canThreePartsEqualSum([22, 63, 75, 55, 12, 26, 87, 67, 11, 47]) == False
    assert solution.canThreePartsEqualSum([62, 87, 36]) == False
    assert solution.canThreePartsEqualSum([20, 91, 99]) == False
    assert solution.canThreePartsEqualSum([76, 61, 23, 87, 72]) == False
    assert solution.canThreePartsEqualSum([88, 52, 66, 67]) == False
    assert solution.canThreePartsEqualSum([98, 97, 6, 64, 33]) == False
    assert solution.canThreePartsEqualSum([100, 96, 34, 75, 2, 46, 23, 45, 57]) == False
    assert solution.canThreePartsEqualSum([71, 7, 74, 76, 55, 80, 13]) == False
    assert solution.canThreePartsEqualSum([1, 67, 2]) == False
    assert solution.canThreePartsEqualSum([29, 90, 62, 13, 95, 49]) == False
    assert solution.canThreePartsEqualSum([73, 57, 76]) == False
    assert solution.canThreePartsEqualSum([8, 5, 68, 55]) == False
    assert solution.canThreePartsEqualSum([33, 20, 99, 28, 63, 29]) == False
    assert solution.canThreePartsEqualSum([68, 30, 21]) == False
    assert solution.canThreePartsEqualSum([11, 68, 48, 15, 58, 36, 84, 80]) == False
    assert solution.canThreePartsEqualSum([55, 66, 99, 84, 46, 74]) == False
    assert solution.canThreePartsEqualSum([28, 97, 68, 98, 77, 72, 89]) == False
    assert solution.canThreePartsEqualSum([9, 37, 45, 69, 32, 40]) == False
    assert solution.canThreePartsEqualSum([94, 34, 31, 80, 56]) == False
    assert solution.canThreePartsEqualSum([30, 85, 72, 70, 29, 25, 56]) == False
    assert solution.canThreePartsEqualSum([52, 62, 98, 80, 83, 39, 25, 100, 21, 55]) == False
    assert solution.canThreePartsEqualSum([47, 69, 37, 41, 13]) == False
    assert solution.canThreePartsEqualSum([58, 24, 90]) == False
    assert solution.canThreePartsEqualSum([17, 85, 52, 80, 39, 96, 40, 78, 81]) == False
    assert solution.canThreePartsEqualSum([47, 62, 2, 95, 90, 33, 42, 12, 22]) == False
    assert solution.canThreePartsEqualSum([19, 94, 3, 27, 53, 36, 2]) == False
    assert solution.canThreePartsEqualSum([12, 59, 54, 2, 56]) == False
    assert solution.canThreePartsEqualSum([69, 58, 35, 27, 38, 53]) == False
    assert solution.canThreePartsEqualSum([20, 68, 72, 54, 81, 48, 77, 11, 21, 71]) == False
    assert solution.canThreePartsEqualSum([99, 7, 17, 90, 22, 84, 11, 70]) == False
    assert solution.canThreePartsEqualSum([34, 6, 54, 58, 19, 72, 52, 60, 70, 11]) == False
    assert solution.canThreePartsEqualSum([57, 4, 97, 11]) == False
    assert solution.canThreePartsEqualSum([12, 22, 87, 51, 57, 65, 98, 45, 42]) == False
    assert solution.canThreePartsEqualSum([13, 54, 28, 38, 37, 67, 59, 21, 52]) == False
    assert solution.canThreePartsEqualSum([12, 46, 13, 6, 83]) == False
    assert solution.canThreePartsEqualSum([99, 41, 6]) == False
    assert solution.canThreePartsEqualSum([57, 16, 82, 59, 37, 36, 24, 35]) == False
    assert solution.canThreePartsEqualSum([66, 18, 61, 70, 22]) == False
    assert solution.canThreePartsEqualSum([34, 16, 75, 94, 52]) == False
    assert solution.canThreePartsEqualSum([68, 34, 91, 19, 48, 89, 42, 75, 15]) == False
    assert solution.canThreePartsEqualSum([36, 11, 62, 90, 58, 100, 85, 68, 22]) == False
    assert solution.canThreePartsEqualSum([76, 68, 39, 24, 79, 16, 6]) == False
    assert solution.canThreePartsEqualSum([74, 46, 90, 31, 1, 5, 29]) == False
    assert solution.canThreePartsEqualSum([28, 71, 89, 68, 8, 57]) == False
    assert solution.canThreePartsEqualSum([84, 82, 6, 75, 96]) == False
    assert solution.canThreePartsEqualSum([15, 31, 57, 45, 3, 68, 97, 72, 64, 59]) == False
    assert solution.canThreePartsEqualSum([34, 47, 56]) == False
    assert solution.canThreePartsEqualSum([33, 83, 68, 98]) == False
    assert solution.canThreePartsEqualSum([24, 46, 39, 8, 58, 89, 98]) == False
    assert solution.canThreePartsEqualSum([88, 44, 16, 52, 67]) == False
    assert solution.canThreePartsEqualSum([18, 11, 22]) == False
    assert solution.canThreePartsEqualSum([39, 35, 64, 27, 85, 89, 86, 44, 46]) == False
    assert solution.canThreePartsEqualSum([96, 24, 72, 63, 41]) == False
    assert solution.canThreePartsEqualSum([50, 20, 45, 99, 15, 23, 57, 71]) == False
    assert solution.canThreePartsEqualSum([69, 29, 22, 70, 23, 73, 33, 65, 54]) == False
    assert solution.canThreePartsEqualSum([19, 17, 81, 24, 15, 32]) == False
    assert solution.canThreePartsEqualSum([15, 76, 1, 34, 67, 65, 63, 86, 88]) == False
    assert solution.canThreePartsEqualSum([35, 92, 88, 94, 70, 22, 90, 42, 3, 4]) == False
    assert solution.canThreePartsEqualSum([97, 58, 27, 20, 13, 62]) == False
    assert solution.canThreePartsEqualSum([51, 72, 99]) == False
    assert solution.canThreePartsEqualSum([87, 95, 25, 34, 48, 33, 26, 45, 62, 79]) == False
    assert solution.canThreePartsEqualSum([1, 55, 47, 81, 77, 70, 57, 13, 71, 5]) == False
    assert solution.canThreePartsEqualSum([86, 61, 44, 33, 54, 42, 40, 10]) == False
    assert solution.canThreePartsEqualSum([63, 21, 45, 32, 3, 37, 66, 97]) == False
    assert solution.canThreePartsEqualSum([80, 82, 90, 22, 94, 74, 9, 21]) == False
    assert solution.canThreePartsEqualSum([37, 22, 74, 39, 49, 10, 69, 45, 85, 100]) == False
    assert solution.canThreePartsEqualSum([68, 36, 78, 96, 34, 29, 69, 85]) == False
    assert solution.canThreePartsEqualSum([17, 47, 90, 94, 25, 95, 4, 10, 18]) == False
    assert solution.canThreePartsEqualSum([47, 72, 88, 61, 18, 20, 64, 99]) == False
    assert solution.canThreePartsEqualSum([39, 86, 84, 74, 90, 70, 69, 96, 1]) == False
    assert solution.canThreePartsEqualSum([16, 24, 51, 63, 97, 42, 39, 58]) == False
    assert solution.canThreePartsEqualSum([53, 5, 73, 12, 38, 72, 18]) == False
    assert solution.canThreePartsEqualSum([94, 44, 68, 48, 2, 27, 84, 67, 77]) == False
    assert solution.canThreePartsEqualSum([27, 46, 54, 1, 24, 11]) == False
    assert solution.canThreePartsEqualSum([23, 70, 91, 80, 27]) == False
    assert solution.canThreePartsEqualSum([45, 28, 46, 35, 25, 30, 41, 14, 99]) == False
    assert solution.canThreePartsEqualSum([14, 25, 3, 96]) == False
    assert solution.canThreePartsEqualSum([56, 70, 18, 17, 6]) == False
    assert solution.canThreePartsEqualSum([31, 66, 62, 59, 45]) == False
    assert solution.canThreePartsEqualSum([71, 69, 96, 86, 1]) == False
    assert solution.canThreePartsEqualSum([61, 66, 45, 14, 75, 86, 48, 69, 62]) == False
    assert solution.canThreePartsEqualSum([100, 53, 82, 12, 65, 6, 64, 52, 92, 14]) == False
    assert solution.canThreePartsEqualSum([67, 2, 55, 90, 20, 65, 23, 69]) == False
    assert solution.canThreePartsEqualSum([72, 11, 60, 30, 52, 62, 66, 76]) == False
    assert solution.canThreePartsEqualSum([48, 88, 68, 53, 54, 45, 13, 6]) == False
    assert solution.canThreePartsEqualSum([46, 69, 38]) == False
    assert solution.canThreePartsEqualSum([1, 7, 74, 2]) == False
    assert solution.canThreePartsEqualSum([86, 58, 4, 65, 13, 43, 31, 34, 28, 88]) == False
    assert solution.canThreePartsEqualSum([50, 94, 87, 66, 72, 92, 7, 95, 17, 41]) == False
    assert solution.canThreePartsEqualSum([66, 96, 44, 91, 6]) == False
    assert solution.canThreePartsEqualSum([8, 25, 64, 85]) == False

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
