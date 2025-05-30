from hard_44_canon import Solution as SolutionCanon
from chatgpt_hard_44 import Solution as SolutionChatGPT
from claude_hard_44 import Solution as SolutionClaude
from gemini_hard_44 import Solution as SolutionGemini


def run_basic_tests(solution):
    assert solution.isMatch("aa", "a") == False
    assert solution.isMatch("aa", "*") == True
    assert solution.isMatch("cb", "?a") == False

def run_advanced_tests(solution):
    assert solution.isMatch('glqoboilgm', '*zxmbgclk?') == False
    assert solution.isMatch('dbejmku', 'nsqsrthmm') == False
    assert solution.isMatch('wiu', 'zqosvkd') == False
    assert solution.isMatch('nxm', 'g*uen*yhlf') == False
    assert solution.isMatch('aatvjfjypr', 'yzon') == False
    assert solution.isMatch('hn', 'pbszl') == False
    assert solution.isMatch('', 'mwgftzk') == False
    assert solution.isMatch('', 'j') == False
    assert solution.isMatch('bvvu', 'pq') == False
    assert solution.isMatch('tntpvuc', 'ofp') == False
    assert solution.isMatch('yombpvdga', '') == False
    assert solution.isMatch('pck', 'tfy') == False
    assert solution.isMatch('wu', 'flky?ku') == False
    assert solution.isMatch('tiwmflztu', '') == False
    assert solution.isMatch('gzf', 'zmcdrgub') == False
    assert solution.isMatch('zvpn', 'apm*rlzls') == False
    assert solution.isMatch('v', 'bxvvfmhi') == False
    assert solution.isMatch('quripsushf', '?anrxx?rzt') == False
    assert solution.isMatch('ajsbadaz', 'cd*xpyc') == False
    assert solution.isMatch('at', 'gyagj') == False
    assert solution.isMatch('xh', 'ywouud') == False
    assert solution.isMatch('', 'heabt*o') == False
    assert solution.isMatch('tagqirv', 'r') == False
    assert solution.isMatch('xwswwc', 'n') == False
    assert solution.isMatch('dntgqaxiy', 'xthy') == False
    assert solution.isMatch('', 'z*?dyl??h') == False
    assert solution.isMatch('vuubt', 'hmvcyq') == False
    assert solution.isMatch('hzpmpnts', 'gdmqvc') == False
    assert solution.isMatch('qlnryoasm', 'ojybjc') == False
    assert solution.isMatch('', 'igl') == False
    assert solution.isMatch('qmanxflqa', 'qz*ak') == False
    assert solution.isMatch('gwnsi', 'bh') == False
    assert solution.isMatch('vtsx', 's') == False
    assert solution.isMatch('elka', 'oyqwsya?nc') == False
    assert solution.isMatch('aywph', 'hvjco*ooj') == False
    assert solution.isMatch('lhhqfyleof', 'jserusl') == False
    assert solution.isMatch('gxxq', 't') == False
    assert solution.isMatch('ltic', 'po') == False
    assert solution.isMatch('mmy', 'iednsof') == False
    assert solution.isMatch('isa', 'rh') == False
    assert solution.isMatch('xded', 'ajeydqvsw') == False
    assert solution.isMatch('', 'ka?hxpi') == False
    assert solution.isMatch('zkvs', 'bijz') == False
    assert solution.isMatch('sab', '*w') == False
    assert solution.isMatch('abuzmjce', 'da?nylbzw') == False
    assert solution.isMatch('giexqyfzrz', '') == False
    assert solution.isMatch('yelyefnvz', 'lbd') == False
    assert solution.isMatch('rxjmzn', 'fuptqfz') == False
    assert solution.isMatch('elxdyl', 'skf') == False
    assert solution.isMatch('vacs', 'lt*tkqbbi') == False
    assert solution.isMatch('iopjugxeg', 'nicgiiuu') == False
    assert solution.isMatch('bpuats', 'yqtqrxwx') == False
    assert solution.isMatch('wux', 'bzbjsvg') == False
    assert solution.isMatch('peiqscq', 'somg?fygyy') == False
    assert solution.isMatch('xbgvb', 'xdo*w') == False
    assert solution.isMatch('', 'tvsk') == False
    assert solution.isMatch('fw', 'xbodjk?gu') == False
    assert solution.isMatch('drxglpztn', 'ek') == False
    assert solution.isMatch('oasafmqzbe', 'w') == False
    assert solution.isMatch('iifmrfmwhk', 'ititc?pih') == False
    assert solution.isMatch('miphzxiu', '') == False
    assert solution.isMatch('t', 'rjvaatluzq') == False
    assert solution.isMatch('xdypmetoa', 'pkvztsq') == False
    assert solution.isMatch('jezmohr', 'niy') == False
    assert solution.isMatch('wvy', 'tdacmjej') == False
    assert solution.isMatch('iagppvu', 'bfjdig') == False
    assert solution.isMatch('w', 'ylpb') == False
    assert solution.isMatch('ibz', 'lplb?jnjb') == False
    assert solution.isMatch('', 'rh*rai') == False
    assert solution.isMatch('dmvx', 'bomgkfqvq') == False
    assert solution.isMatch('wyrtgpnooh', '?xpxcipge?') == False
    assert solution.isMatch('vwbcphmqc', 'jstiys') == False
    assert solution.isMatch('', 'd?nvguvn') == False
    assert solution.isMatch('', 'tghbtjggt?') == False
    assert solution.isMatch('vii', 'ktd') == False
    assert solution.isMatch('', 'w') == False
    assert solution.isMatch('yfnqjmn', 'fky') == False
    assert solution.isMatch('mnzyfjfr', 'cbrj*ontw') == False
    assert solution.isMatch('doqxgde', 'qxkxzqko') == False
    assert solution.isMatch('bokggceiz', 'gjwhobq*wx') == False
    assert solution.isMatch('semps', 'lkno') == False
    assert solution.isMatch('wrudqho', 'd') == False
    assert solution.isMatch('mfqkzeq', 'xk') == False
    assert solution.isMatch('wcy', 'thmg') == False
    assert solution.isMatch('cpnfk', 'f*gujidvz') == False
    assert solution.isMatch('cxzglh', 'j') == False
    assert solution.isMatch('bdrfvh', 'bllzmmwjkm') == False
    assert solution.isMatch('kepgbho', 'xwwwdde') == False
    assert solution.isMatch('sdeuxn', 'f') == False
    assert solution.isMatch('amtyuiiz', 'hqbeg') == False
    assert solution.isMatch('mlqm', 'k*trsvsp') == False
    assert solution.isMatch('bzjpw', 'zpoahkjcp') == False
    assert solution.isMatch('ixnxxwskfc', 'wfhmzgkr') == False
    assert solution.isMatch('deslfhyaf', 'czfphiqxn') == False
    assert solution.isMatch('xbinzrjol', 'jhrgit') == False
    assert solution.isMatch('nnmemht', '?t') == False
    assert solution.isMatch('wc', 'jr') == False
    assert solution.isMatch('bvpkm', 'cpsrhmsioi') == False
    assert solution.isMatch('vbavikffbu', 'sd*') == False
    assert solution.isMatch('rzv', 'hfvhzxdbx') == False

def run_timed_tests(solution):
    assert solution.isMatch('glqoboilgm', '*zxmbgclk?') == False
    assert solution.isMatch('dbejmku', 'nsqsrthmm') == False
    assert solution.isMatch('wiu', 'zqosvkd') == False
    assert solution.isMatch('nxm', 'g*uen*yhlf') == False
    assert solution.isMatch('aatvjfjypr', 'yzon') == False
    assert solution.isMatch('hn', 'pbszl') == False
    assert solution.isMatch('', 'mwgftzk') == False
    assert solution.isMatch('', 'j') == False
    assert solution.isMatch('bvvu', 'pq') == False
    assert solution.isMatch('tntpvuc', 'ofp') == False
        

def save_output(output: str):
    with open('../times.csv', 'a') as f:
        f.write(f'{output}\n')

if __name__ == '__main__':
    import sys
    problem_id = 44
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

        output += f'hard_44,{sys.argv[2]},'
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