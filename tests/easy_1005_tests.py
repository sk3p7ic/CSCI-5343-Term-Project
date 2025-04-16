from easy_1005_canon import Solution as SolutionCanon
from chatgpt_easy_1005 import Solution as SolutionChatGPT
from claude_easy_1005 import Solution as SolutionClaude
from gemini_easy_1005 import Solution as SolutionGemini


def run_basic_tests(solution):
    
    assert solution.largestSumAfterKNegations([4,2,3], 1) == 5
    assert solution.largestSumAfterKNegations([3,-1,0,2], 3) == 6
    assert solution.largestSumAfterKNegations([2,-3,-1,5,-4], 2) == 13

def run_advanced_tests(solution):
    assert solution.largestSumAfterKNegations([-25, 64, 53, -59, -31, -75], 92) == 307
    assert solution.largestSumAfterKNegations([23, -77, -29, -8, -31, 24, -58], 18) == 234
    assert solution.largestSumAfterKNegations([-43, -45, -93, 73, -18, 45], 81) == 281
    assert solution.largestSumAfterKNegations([73, -7, 15, 76, 71, 51, -93, -24, 21], 25) == 431
    assert solution.largestSumAfterKNegations([66, 78], 66) == 144
    assert solution.largestSumAfterKNegations([73, 10, -39, 0, -1, -94, -73], 27) == 290
    assert solution.largestSumAfterKNegations([-3, -72, -66, -18, 5, -81], 76) == 239
    assert solution.largestSumAfterKNegations([49, 19, 14, -40, -66, 72, -61, 20], 88) == 313
    assert solution.largestSumAfterKNegations([86, -43, 78, -7, -51, -67, -68], 6) == 386
    assert solution.largestSumAfterKNegations([-89, 67, -36, -28], 66) == 164
    assert solution.largestSumAfterKNegations([-25], 16) == -25
    assert solution.largestSumAfterKNegations([85, -63, 88, -84, -6, 84], 58) == 398
    assert solution.largestSumAfterKNegations([-93, -84, 4], 35) == 173
    assert solution.largestSumAfterKNegations([74, 55, 16, 88, -76, -60, -33, 75], 100) == 445
    assert solution.largestSumAfterKNegations([-24, 93, -77, -20, -26, 70], 91) == 270
    assert solution.largestSumAfterKNegations([-81], 65) == 81
    assert solution.largestSumAfterKNegations([3, -72, 53, -89, -97, -65, -5, 8], 3) == 252
    assert solution.largestSumAfterKNegations([-83, -10, -64, 55, 92, -31, -63, -63], 4) == 379
    assert solution.largestSumAfterKNegations([-43, -82, 82, 15, -98, -54, 97, -82], 32) == 523
    assert solution.largestSumAfterKNegations([88, 6, -65], 69) == 159
    assert solution.largestSumAfterKNegations([-49, 24, -28, 56, 9, 54, 88, 79, -3, 21], 30) == 405
    assert solution.largestSumAfterKNegations([-25, 43, 55, 39, -89, -15, -5, 58, 41], 85) == 360
    assert solution.largestSumAfterKNegations([30, 87, 75, -68, 6, 42, -68], 31) == 364
    assert solution.largestSumAfterKNegations([-25, 55, 89, -12, -61, 20, 90], 38) == 328
    assert solution.largestSumAfterKNegations([-59, 47, -75, 95, 61, -92], 94) == 335
    assert solution.largestSumAfterKNegations([88, 20, 73, 85, -8, -86], 82) == 360
    assert solution.largestSumAfterKNegations([-6, 72, 54, 60, 92], 68) == 272
    assert solution.largestSumAfterKNegations([-92, 50, -83, -55], 55) == 280
    assert solution.largestSumAfterKNegations([8, 41, 12], 79) == 45
    assert solution.largestSumAfterKNegations([-32, -14, -45, -77, 98, 80, -47, 91, -4, 12], 79) == 492
    assert solution.largestSumAfterKNegations([82, 70, -22], 35) == 174
    assert solution.largestSumAfterKNegations([96, 100, -77, 26, -53, 23, -47, -86], 72) == 508
    assert solution.largestSumAfterKNegations([78, 60, -55, 4, -26, -11, -100, 37, -20], 80) == 383
    assert solution.largestSumAfterKNegations([-90, -1, -31, 41, 99, 57], 82) == 317
    assert solution.largestSumAfterKNegations([-68, 70, 91, -3, 73, -83, 44, -88], 25) == 514
    assert solution.largestSumAfterKNegations([5, -1, 57, 94, -93, 5, 75], 37) == 328
    assert solution.largestSumAfterKNegations([80, 62, 74, -82, -67], 60) == 365
    assert solution.largestSumAfterKNegations([-42, -21, -85, 98, -20, 54, -97, 47], 75) == 464
    assert solution.largestSumAfterKNegations([62, 71, 39, 23, -62], 55) == 257
    assert solution.largestSumAfterKNegations([56, 62, -53, 58, -100, 12], 30) == 341
    assert solution.largestSumAfterKNegations([62, -1, 0, 72, 75], 19) == 210
    assert solution.largestSumAfterKNegations([-46, -7, 79, -89, 7, 83, 19], 28) == 316
    assert solution.largestSumAfterKNegations([-43, 89, -12, -78, 30, -87, 43], 41) == 358
    assert solution.largestSumAfterKNegations([31, -28, 32, 15, 17, 60], 87) == 183
    assert solution.largestSumAfterKNegations([23, -70, 32, -48], 35) == 127
    assert solution.largestSumAfterKNegations([70], 101) == -70
    assert solution.largestSumAfterKNegations([-37, -8, -84, 37, 26], 95) == 192
    assert solution.largestSumAfterKNegations([-26, 50, -55, -37, -43, -75, 0, -38, 27], 94) == 351
    assert solution.largestSumAfterKNegations([-80, -42, 31, -57, 53, -77, -53], 85) == 393
    assert solution.largestSumAfterKNegations([24, 40, -84, -95, 13, -68, -10, 69], 94) == 403
    assert solution.largestSumAfterKNegations([94, -31, 96, 7, -22, 19, 52, -90], 12) == 397
    assert solution.largestSumAfterKNegations([17, -18, -62], 4) == 97
    assert solution.largestSumAfterKNegations([-53, 62, -26, 42, 11], 19) == 172
    assert solution.largestSumAfterKNegations([84, 1, -91, -52, -21, -6, 34, -44], 37) == 333
    assert solution.largestSumAfterKNegations([50, -88, -20, -24, 34, 62, 53, -28, 27], 2) == 298
    assert solution.largestSumAfterKNegations([-36], 30) == -36
    assert solution.largestSumAfterKNegations([62, 95, -61, -44, 46, 81, 96, -2, -93, 17], 15) == 593
    assert solution.largestSumAfterKNegations([58, -64, 18, -35, 42], 55) == 181
    assert solution.largestSumAfterKNegations([-55, 83, 50], 15) == 188
    assert solution.largestSumAfterKNegations([65], 70) == 65
    assert solution.largestSumAfterKNegations([-71, -30, -73, -91, -83, -73, -89, -66, -89, -53], 46) == 718
    assert solution.largestSumAfterKNegations([-69, 20, -85], 90) == 174
    assert solution.largestSumAfterKNegations([25, -54, 15, -23, 100, -76], 9) == 293
    assert solution.largestSumAfterKNegations([-11], 24) == -11
    assert solution.largestSumAfterKNegations([-32, 49, -62, -21, 50, -55], 93) == 227
    assert solution.largestSumAfterKNegations([45, -66, 80], 89) == 191
    assert solution.largestSumAfterKNegations([-65], 98) == -65
    assert solution.largestSumAfterKNegations([-47, 41], 38) == 6
    assert solution.largestSumAfterKNegations([-46, 13, 69, 27, -54, -41, 24, -21], 95) == 269
    assert solution.largestSumAfterKNegations([80, 97, 79, -81, 5], 9) == 342
    assert solution.largestSumAfterKNegations([-75, 26, -92], 16) == 193
    assert solution.largestSumAfterKNegations([-74, 19, 71, 73, 16, -79, -43], 15) == 375
    assert solution.largestSumAfterKNegations([-56, -3, -90, 7, -59, 83, 27, 34], 6) == 359
    assert solution.largestSumAfterKNegations([90, -95, 73, -49, 51], 21) == 260
    assert solution.largestSumAfterKNegations([-34, -99], 64) == 133
    assert solution.largestSumAfterKNegations([-89], 28) == -89
    assert solution.largestSumAfterKNegations([55, 99, -45, -38, 65, 37], 65) == 265
    assert solution.largestSumAfterKNegations([-52, -98, 64], 10) == 214
    assert solution.largestSumAfterKNegations([68, 24, -61, -31, -4], 50) == 180
    assert solution.largestSumAfterKNegations([-37, -23, -76, 88], 59) == 224
    assert solution.largestSumAfterKNegations([35, -32, -73, -3, -5, 57, 96], 95) == 295
    assert solution.largestSumAfterKNegations([-24, -52, -45], 23) == 121
    assert solution.largestSumAfterKNegations([-39], 74) == -39
    assert solution.largestSumAfterKNegations([42, -40], 14) == 2
    assert solution.largestSumAfterKNegations([-9, -14, -72, 50], 52) == 127
    assert solution.largestSumAfterKNegations([-65, 52, 65, -76, 30, 26, -64, -34, -15, -69], 57) == 466
    assert solution.largestSumAfterKNegations([-21, -52, -47, 45, 38, -82, -17, -65, -66], 17) == 433
    assert solution.largestSumAfterKNegations([81], 18) == 81
    assert solution.largestSumAfterKNegations([-74, -59, -52, -95, 37, -98, -69, -66, -2, -14], 57) == 566
    assert solution.largestSumAfterKNegations([-75], 77) == 75
    assert solution.largestSumAfterKNegations([85, 16, 64, 26, -66, 86], 58) == 311
    assert solution.largestSumAfterKNegations([-97, -67, -30, -33, -22, -63, -49], 26) == 317
    assert solution.largestSumAfterKNegations([87, -28, 73, -64, -17, 26, 20, -43], 12) == 358
    assert solution.largestSumAfterKNegations([-5, -50, 74, -56, -95, 81, -86, -61, -31], 85) == 539
    assert solution.largestSumAfterKNegations([78], 5) == -78
    assert solution.largestSumAfterKNegations([76, -35, -33, 2, -16, -20], 90) == 182
    assert solution.largestSumAfterKNegations([-41, -80, -56, -29, -61, 92], 78) == 301
    assert solution.largestSumAfterKNegations([-5, 28], 71) == 33
    assert solution.largestSumAfterKNegations([14, 49, 0, 18], 3) == 81
    assert solution.largestSumAfterKNegations([-14], 94) == -14
        

if __name__ == '__main__':
    import sys
    problem_id = 1005
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

        print(f'easy_1005,{sys.argv[2]},', end='')
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