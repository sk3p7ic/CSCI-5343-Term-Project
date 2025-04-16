from easy_409_canon import Solution as SolutionCanon
from chatgpt_easy_409 import Solution as SolutionChatGPT
from claude_easy_409 import Solution as SolutionClaude
from gemini_easy_409 import Solution as SolutionGemini


def run_basic_tests(solution):
    
    assert solution.longestPalindrome("abccccdd") == 7
    assert solution.longestPalindrome("a") == 1

def run_advanced_tests(solution):
    assert solution.longestPalindrome("GxyDLlAh") == 1
    assert solution.longestPalindrome("HcEbNV") == 1
    assert solution.longestPalindrome("DNQeW") == 1
    assert solution.longestPalindrome("Rm") == 1
    assert solution.longestPalindrome("aMOqIUDZZ") == 3
    assert solution.longestPalindrome("WHtu") == 1
    assert solution.longestPalindrome("IKOqqJaucR") == 3
    assert solution.longestPalindrome("ig") == 1
    assert solution.longestPalindrome("LeUzsYoEbT") == 1
    assert solution.longestPalindrome("XgZSa") == 1
    assert solution.longestPalindrome("YVxpSr") == 1
    assert solution.longestPalindrome("uTSVyofy") == 3
    assert solution.longestPalindrome("oENUy") == 1
    assert solution.longestPalindrome("f") == 1
    assert solution.longestPalindrome("E") == 1
    assert solution.longestPalindrome("fzNDsJ") == 1
    assert solution.longestPalindrome("mN") == 1
    assert solution.longestPalindrome("rI") == 1
    assert solution.longestPalindrome("oBbosiCYs") == 5
    assert solution.longestPalindrome("pK") == 1
    assert solution.longestPalindrome("dNw") == 1
    assert solution.longestPalindrome("pdGJJclhF") == 3
    assert solution.longestPalindrome("hLfgZ") == 1
    assert solution.longestPalindrome("sVKmuaeuQG") == 3
    assert solution.longestPalindrome("suYnZmKrt") == 1
    assert solution.longestPalindrome("WAG") == 1
    assert solution.longestPalindrome("kG") == 1
    assert solution.longestPalindrome("ih") == 1
    assert solution.longestPalindrome("iB") == 1
    assert solution.longestPalindrome("gpu") == 1
    assert solution.longestPalindrome("mVQsrMf") == 1
    assert solution.longestPalindrome("Ld") == 1
    assert solution.longestPalindrome("gRu") == 1
    assert solution.longestPalindrome("utBH") == 1
    assert solution.longestPalindrome("gLcMUCH") == 1
    assert solution.longestPalindrome("QuuAaPQJ") == 5
    assert solution.longestPalindrome("nWqtUfCs") == 1
    assert solution.longestPalindrome("NNrGZ") == 3
    assert solution.longestPalindrome("YeBA") == 1
    assert solution.longestPalindrome("B") == 1
    assert solution.longestPalindrome("g") == 1
    assert solution.longestPalindrome("csCBgple") == 1
    assert solution.longestPalindrome("ruKYUiZyF") == 1
    assert solution.longestPalindrome("Mct") == 1
    assert solution.longestPalindrome("UtJbblK") == 3
    assert solution.longestPalindrome("PNDtlcAPLM") == 3
    assert solution.longestPalindrome("wbgB") == 1
    assert solution.longestPalindrome("F") == 1
    assert solution.longestPalindrome("FvFi") == 3
    assert solution.longestPalindrome("esERdj") == 1
    assert solution.longestPalindrome("cAxNAht") == 3
    assert solution.longestPalindrome("dgBRVk") == 1
    assert solution.longestPalindrome("vaGRLv") == 3
    assert solution.longestPalindrome("vZp") == 1
    assert solution.longestPalindrome("vkfXfx") == 3
    assert solution.longestPalindrome("vwuHH") == 3
    assert solution.longestPalindrome("ZYfi") == 1
    assert solution.longestPalindrome("T") == 1
    assert solution.longestPalindrome("IzdYDFaQV") == 1
    assert solution.longestPalindrome("ZKSocSBIHS") == 3
    assert solution.longestPalindrome("r") == 1
    assert solution.longestPalindrome("RIM") == 1
    assert solution.longestPalindrome("hwtyCpSr") == 1
    assert solution.longestPalindrome("B") == 1
    assert solution.longestPalindrome("ngF") == 1
    assert solution.longestPalindrome("KBiuCkFQJ") == 1
    assert solution.longestPalindrome("ESginoagsp") == 3
    assert solution.longestPalindrome("x") == 1
    assert solution.longestPalindrome("UGeMpu") == 1
    assert solution.longestPalindrome("oM") == 1
    assert solution.longestPalindrome("zhAzOTU") == 3
    assert solution.longestPalindrome("rm") == 1
    assert solution.longestPalindrome("W") == 1
    assert solution.longestPalindrome("wTf") == 1
    assert solution.longestPalindrome("Uh") == 1
    assert solution.longestPalindrome("NVMTWj") == 1
    assert solution.longestPalindrome("xllqx") == 5
    assert solution.longestPalindrome("mSYqucQZ") == 1
    assert solution.longestPalindrome("nc") == 1
    assert solution.longestPalindrome("NmEdWL") == 1
    assert solution.longestPalindrome("ji") == 1
    assert solution.longestPalindrome("mTng") == 1
    assert solution.longestPalindrome("MWB") == 1
    assert solution.longestPalindrome("p") == 1
    assert solution.longestPalindrome("lOZdZD") == 3
    assert solution.longestPalindrome("ZRPmTOObzh") == 3
    assert solution.longestPalindrome("iD") == 1
    assert solution.longestPalindrome("eaARO") == 1
    assert solution.longestPalindrome("GoGSCG") == 3
    assert solution.longestPalindrome("Hki") == 1
    assert solution.longestPalindrome("YQjMohunH") == 1
    assert solution.longestPalindrome("mXaURIS") == 1
    assert solution.longestPalindrome("v") == 1
    assert solution.longestPalindrome("iTTzsg") == 3
    assert solution.longestPalindrome("QAC") == 1
    assert solution.longestPalindrome("cCW") == 1
    assert solution.longestPalindrome("SyR") == 1
    assert solution.longestPalindrome("uCKQvx") == 1
    assert solution.longestPalindrome("UVtYfIQsyU") == 3
    assert solution.longestPalindrome("VAGueWdib") == 1
        

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

        print(f'easy_409,{sys.argv[2]},', end='')
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