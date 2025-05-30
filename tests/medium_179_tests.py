from medium_179_canon import Solution as SolutionCanon
from chatgpt_medium_179 import Solution as SolutionChatGPT
from claude_medium_179 import Solution as SolutionClaude
from gemini_medium_179 import Solution as SolutionGemini


def run_basic_tests(solution):
    assert solution.largestNumber([10, 2]) == '210'
    assert solution.largestNumber([3, 30, 34, 5, 9]) == '9534330'

def run_advanced_tests(solution):
    assert solution.largestNumber([57, 79, 87, 61, 72]) == '8779726157'
    assert solution.largestNumber([53, 38, 73, 56, 100]) == '73565338100'
    assert solution.largestNumber([89, 75, 87, 84]) == '89878475'
    assert solution.largestNumber([27, 12, 14, 37, 76, 71, 9, 26]) == '976713727261412'
    assert solution.largestNumber([47, 14, 98, 27, 23, 32]) == '984732272314'
    assert solution.largestNumber([36, 86, 37]) == '863736'
    assert solution.largestNumber([9, 100, 15, 93, 27]) == '9932715100'
    assert solution.largestNumber([40, 1, 61, 77, 51, 6, 99]) == '997766151401'
    assert solution.largestNumber([86, 10, 96, 87, 15, 22, 47, 88]) == '9688878647221510'
    assert solution.largestNumber([12, 6]) == '612'
    assert solution.largestNumber([60, 89, 52]) == '896052'
    assert solution.largestNumber([47, 89, 5, 72]) == '8972547'
    assert solution.largestNumber([44, 36, 11, 34, 54, 66]) == '665444363411'
    assert solution.largestNumber([81, 7, 39]) == '81739'
    assert solution.largestNumber([79, 33, 66, 34, 28]) == '7966343328'
    assert solution.largestNumber([48, 98, 73]) == '987348'
    assert solution.largestNumber([81, 94, 53, 89, 20, 74, 44]) == '94898174534420'
    assert solution.largestNumber([9, 61, 67, 84]) == '9846761'
    assert solution.largestNumber([5, 52, 22, 19, 78, 79, 75, 85, 66, 87]) == '8785797875665522219'
    assert solution.largestNumber([25]) == '25'
    assert solution.largestNumber([95, 6, 30, 2, 68, 49, 87, 25, 5]) == '958768654930252'
    assert solution.largestNumber([50, 56]) == '5650'
    assert solution.largestNumber([81, 61, 57, 74, 67, 56, 68, 35, 76]) == '817674686761575635'
    assert solution.largestNumber([73, 3, 90]) == '90733'
    assert solution.largestNumber([35, 96, 62, 3, 46, 11, 2, 69, 60, 58]) == '966962605846353211'
    assert solution.largestNumber([54, 94, 9, 28, 82, 95, 18, 8]) == '99594882542818'
    assert solution.largestNumber([26, 90, 80, 43, 62, 58, 61, 1, 47, 2]) == '908062615847432621'
    assert solution.largestNumber([7, 69, 62, 81, 98, 36, 99, 79, 60]) == '99988179769626036'
    assert solution.largestNumber([64, 34, 38, 91, 94, 44, 71, 50, 53, 73]) == '94917371645350443834'
    assert solution.largestNumber([47, 19, 92, 40, 100]) == '92474019100'
    assert solution.largestNumber([68]) == '68'
    assert solution.largestNumber([70, 40, 36]) == '704036'
    assert solution.largestNumber([56, 24, 87, 54]) == '87565424'
    assert solution.largestNumber([55, 50, 62, 33, 85, 17, 35, 86, 56, 13]) == '86856256555035331713'
    assert solution.largestNumber([2, 94, 62, 36, 81, 97, 6, 82]) == '97948281662362'
    assert solution.largestNumber([39, 88, 55, 76, 29, 21, 56]) == '88765655392921'
    assert solution.largestNumber([66, 90, 55, 88, 29, 99]) == '999088665529'
    assert solution.largestNumber([67]) == '67'
    assert solution.largestNumber([54, 69, 79]) == '796954'
    assert solution.largestNumber([29, 51, 92, 48]) == '92514829'
    assert solution.largestNumber([55, 45, 39, 34, 92, 17, 70]) == '92705545393417'
    assert solution.largestNumber([50, 7, 93, 23, 25, 94]) == '94937502523'
    assert solution.largestNumber([100]) == '100'
    assert solution.largestNumber([98, 20, 40, 7, 53, 13, 15, 70, 50, 81]) == '9881770535040201513'
    assert solution.largestNumber([23, 4, 30, 64, 46, 39, 44, 71, 7, 80]) == '807716446444393023'
    assert solution.largestNumber([37, 38, 44, 85]) == '85443837'
    assert solution.largestNumber([13, 6, 34, 87]) == '8763413'
    assert solution.largestNumber([46, 18, 60, 27]) == '60462718'
    assert solution.largestNumber([78, 62, 61, 69, 35, 22, 93, 38]) == '9378696261383522'
    assert solution.largestNumber([61, 49, 11, 8, 68]) == '868614911'
    assert solution.largestNumber([14, 55, 75, 39]) == '75553914'
    assert solution.largestNumber([36, 33, 71, 22, 40]) == '7140363322'
    assert solution.largestNumber([21, 48, 23]) == '482321'
    assert solution.largestNumber([100, 87, 76, 96, 74, 83, 52, 4]) == '9687837674524100'
    assert solution.largestNumber([45]) == '45'
    assert solution.largestNumber([12, 11, 85, 18, 45, 9, 90, 29, 95]) == '99590854529181211'
    assert solution.largestNumber([26]) == '26'
    assert solution.largestNumber([65, 100, 91, 90, 7, 89, 67, 5]) == '919089767655100'
    assert solution.largestNumber([37, 99, 48, 63, 49, 18, 11]) == '99634948371811'
    assert solution.largestNumber([73]) == '73'
    assert solution.largestNumber([9, 95, 49, 64, 69, 33, 60]) == '9956964604933'
    assert solution.largestNumber([42, 48, 24, 38, 36]) == '4842383624'
    assert solution.largestNumber([88, 97, 56, 74]) == '97887456'
    assert solution.largestNumber([32, 57, 75, 18, 28, 3, 8, 47]) == '87557473322818'
    assert solution.largestNumber([4, 31, 64, 22, 48, 35, 87]) == '8764484353122'
    assert solution.largestNumber([8]) == '8'
    assert solution.largestNumber([31, 96, 48]) == '964831'
    assert solution.largestNumber([99, 49, 5]) == '99549'
    assert solution.largestNumber([67, 30, 33, 80]) == '80673330'
    assert solution.largestNumber([11, 90, 22, 79, 46, 62, 28, 27]) == '9079624628272211'
    assert solution.largestNumber([46, 76, 93, 24, 10, 91, 74, 84, 39]) == '939184767446392410'
    assert solution.largestNumber([49]) == '49'
    assert solution.largestNumber([23, 95, 32]) == '953223'
    assert solution.largestNumber([73, 15, 67, 26, 35, 28]) == '736735282615'
    assert solution.largestNumber([74, 21, 83, 73, 88]) == '8883747321'
    assert solution.largestNumber([79, 51, 49]) == '795149'
    assert solution.largestNumber([37, 91, 11, 92, 43, 95, 26, 39, 81]) == '959291814339372611'
    assert solution.largestNumber([7, 79, 93, 68, 90, 1]) == '9390797681'
    assert solution.largestNumber([55, 83, 56, 38, 7, 73, 43, 6, 36, 75]) == '837757365655433836'
    assert solution.largestNumber([21, 10, 28, 15]) == '28211510'
    assert solution.largestNumber([14, 22, 64, 87, 43, 1, 11, 57]) == '876457432214111'
    assert solution.largestNumber([88]) == '88'
    assert solution.largestNumber([60, 91, 1, 36, 9, 45, 21, 76, 85]) == '9918576604536211'
    assert solution.largestNumber([62, 71, 37, 95, 29, 19, 27, 2, 24]) == '95716237292724219'
    assert solution.largestNumber([28, 57]) == '5728'
    assert solution.largestNumber([13, 10, 99, 62, 60, 47, 91, 28]) == '9991626047281310'
    assert solution.largestNumber([44, 77, 16, 17, 71]) == '7771441716'
    assert solution.largestNumber([92, 70, 41, 85, 81, 97]) == '979285817041'
    assert solution.largestNumber([2, 99, 94, 24, 76]) == '999476242'
    assert solution.largestNumber([33, 96, 20, 8, 37, 81, 27, 53]) == '968815337332720'
    assert solution.largestNumber([54, 84]) == '8454'
    assert solution.largestNumber([86, 58, 25, 20, 45, 3, 56, 47, 40, 79]) == '8679585647454032520'
    assert solution.largestNumber([47, 89, 65, 14, 94, 70, 54]) == '94897065544714'
    assert solution.largestNumber([48, 87, 81]) == '878148'
    assert solution.largestNumber([98, 50, 23, 72, 42, 88, 2]) == '9888725042232'
    assert solution.largestNumber([11, 23]) == '2311'
    assert solution.largestNumber([13, 54, 90, 70, 35, 14, 55, 68]) == '9070685554351413'
    assert solution.largestNumber([10, 8, 60, 70, 35]) == '870603510'
    assert solution.largestNumber([56, 40, 89]) == '895640'
    assert solution.largestNumber([19]) == '19'

def run_timed_tests(solution):
    assert solution.largestNumber([57, 79, 87, 61, 72]) == '8779726157'
    assert solution.largestNumber([53, 38, 73, 56, 100]) == '73565338100'
    assert solution.largestNumber([89, 75, 87, 84]) == '89878475'
    assert solution.largestNumber([27, 12, 14, 37, 76, 71, 9, 26]) == '976713727261412'
    assert solution.largestNumber([47, 14, 98, 27, 23, 32]) == '984732272314'
    assert solution.largestNumber([36, 86, 37]) == '863736'
    assert solution.largestNumber([9, 100, 15, 93, 27]) == '9932715100'
    assert solution.largestNumber([40, 1, 61, 77, 51, 6, 99]) == '997766151401'
    assert solution.largestNumber([86, 10, 96, 87, 15, 22, 47, 88]) == '9688878647221510'
    assert solution.largestNumber([12, 6]) == '612'
        

def save_output(output: str):
    with open('../times.csv', 'a') as f:
        f.write(f'{output}\n')

if __name__ == '__main__':
    import sys
    problem_id = 179
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

        output += f'medium_179,{sys.argv[2]},'
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