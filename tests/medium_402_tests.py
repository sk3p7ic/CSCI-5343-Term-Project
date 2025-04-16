from medium_402_canon import Solution as SolutionCanon
from chatgpt_medium_402 import Solution as SolutionChatGPT
from claude_medium_402 import Solution as SolutionClaude
from gemini_medium_402 import Solution as SolutionGemini


def run_basic_tests(solution):
    
    assert solution.removeKdigits("1432219", 3) == "1219"
    assert solution.removeKdigits("10200", 1) == "200"
    assert solution.removeKdigits("10", 2) == "0"

def run_advanced_tests(solution):
    assert solution.removeKdigits('3448', 1) == '344'
    assert solution.removeKdigits('777462', 5) == '2'
    assert solution.removeKdigits('878869', 2) == '7869'
    assert solution.removeKdigits('9482', 2) == '42'
    assert solution.removeKdigits('4', 1) == '0'
    assert solution.removeKdigits('96', 2) == '0'
    assert solution.removeKdigits('487148', 1) == '47148'
    assert solution.removeKdigits('939', 2) == '3'
    assert solution.removeKdigits('69', 2) == '0'
    assert solution.removeKdigits('19615', 4) == '1'
    assert solution.removeKdigits('2', 1) == '0'
    assert solution.removeKdigits('660', 2) == '0'
    assert solution.removeKdigits('67', 1) == '6'
    assert solution.removeKdigits('844', 3) == '0'
    assert solution.removeKdigits('201', 3) == '0'
    assert solution.removeKdigits('476490', 4) == '40'
    assert solution.removeKdigits('55914', 3) == '14'
    assert solution.removeKdigits('53', 2) == '0'
    assert solution.removeKdigits('126', 1) == '12'
    assert solution.removeKdigits('8', 1) == '0'
    assert solution.removeKdigits('99669', 1) == '9669'
    assert solution.removeKdigits('0', 1) == '0'
    assert solution.removeKdigits('0412', 1) == '12'
    assert solution.removeKdigits('63', 1) == '3'
    assert solution.removeKdigits('29839', 2) == '239'
    assert solution.removeKdigits('028', 2) == '0'
    assert solution.removeKdigits('3', 1) == '0'
    assert solution.removeKdigits('428', 3) == '0'
    assert solution.removeKdigits('8830', 3) == '0'
    assert solution.removeKdigits('4621', 3) == '1'
    assert solution.removeKdigits('9', 1) == '0'
    assert solution.removeKdigits('8396', 4) == '0'
    assert solution.removeKdigits('377', 2) == '3'
    assert solution.removeKdigits('792', 1) == '72'
    assert solution.removeKdigits('4832', 1) == '432'
    assert solution.removeKdigits('04', 2) == '0'
    assert solution.removeKdigits('559', 3) == '0'
    assert solution.removeKdigits('14948', 1) == '1448'
    assert solution.removeKdigits('5', 1) == '0'
    assert solution.removeKdigits('76452', 2) == '452'
    assert solution.removeKdigits('889', 2) == '8'
    assert solution.removeKdigits('4884', 1) == '484'
    assert solution.removeKdigits('875', 2) == '5'
    assert solution.removeKdigits('929974', 6) == '0'
    assert solution.removeKdigits('0785', 4) == '0'
    assert solution.removeKdigits('688', 3) == '0'
    assert solution.removeKdigits('9900', 1) == '900'
    assert solution.removeKdigits('8', 1) == '0'
    assert solution.removeKdigits('12486', 2) == '124'
    assert solution.removeKdigits('4424', 4) == '0'
    assert solution.removeKdigits('0', 1) == '0'
    assert solution.removeKdigits('774132', 5) == '1'
    assert solution.removeKdigits('903', 1) == '3'
    assert solution.removeKdigits('1157', 1) == '115'
    assert solution.removeKdigits('70127', 2) == '12'
    assert solution.removeKdigits('001374', 4) == '0'
    assert solution.removeKdigits('0767', 3) == '0'
    assert solution.removeKdigits('58257', 2) == '257'
    assert solution.removeKdigits('464666', 5) == '4'
    assert solution.removeKdigits('2144', 4) == '0'
    assert solution.removeKdigits('4', 1) == '0'
    assert solution.removeKdigits('75042', 2) == '42'
    assert solution.removeKdigits('24', 2) == '0'
    assert solution.removeKdigits('197283', 1) == '17283'
    assert solution.removeKdigits('108863', 2) == '863'
    assert solution.removeKdigits('463205', 3) == '205'
    assert solution.removeKdigits('41754', 4) == '1'
    assert solution.removeKdigits('3', 1) == '0'
    assert solution.removeKdigits('967', 3) == '0'
    assert solution.removeKdigits('75440', 4) == '0'
    assert solution.removeKdigits('7', 1) == '0'
    assert solution.removeKdigits('797976', 3) == '776'
    assert solution.removeKdigits('6', 1) == '0'
    assert solution.removeKdigits('0', 1) == '0'
    assert solution.removeKdigits('0389', 1) == '38'
    assert solution.removeKdigits('80', 2) == '0'
    assert solution.removeKdigits('198346', 5) == '1'
    assert solution.removeKdigits('199', 2) == '1'
    assert solution.removeKdigits('8718', 2) == '18'
    assert solution.removeKdigits('3', 1) == '0'
    assert solution.removeKdigits('41283', 4) == '1'
    assert solution.removeKdigits('6237', 4) == '0'
    assert solution.removeKdigits('7', 1) == '0'
    assert solution.removeKdigits('59615', 2) == '515'
    assert solution.removeKdigits('4', 1) == '0'
    assert solution.removeKdigits('269391', 6) == '0'
    assert solution.removeKdigits('6', 1) == '0'
    assert solution.removeKdigits('300764', 4) == '0'
    assert solution.removeKdigits('142', 2) == '1'
    assert solution.removeKdigits('3565', 4) == '0'
    assert solution.removeKdigits('603023', 1) == '3023'
    assert solution.removeKdigits('348742', 4) == '32'
    assert solution.removeKdigits('830', 3) == '0'
    assert solution.removeKdigits('74', 1) == '4'
    assert solution.removeKdigits('8903', 3) == '0'
    assert solution.removeKdigits('4429', 1) == '429'
    assert solution.removeKdigits('9', 1) == '0'
    assert solution.removeKdigits('84', 1) == '4'
    assert solution.removeKdigits('9000', 4) == '0'
    assert solution.removeKdigits('788', 1) == '78'
        

if __name__ == '__main__':
    import sys
    problem_id = 402
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

        print(f'medium_402,{sys.argv[2]},', end='')
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