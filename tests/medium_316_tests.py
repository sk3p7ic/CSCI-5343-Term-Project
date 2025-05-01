from medium_316_canon import Solution as SolutionCanon
from chatgpt_medium_316 import Solution as SolutionChatGPT
from claude_medium_316 import Solution as SolutionClaude
from gemini_medium_316 import Solution as SolutionGemini


def run_basic_tests(solution):
    assert solution.removeDuplicateLetters("bcabc") == "abc"
    assert solution.removeDuplicateLetters("cbacdcbc") == "acdb"

def run_advanced_tests(solution):
    assert solution.removeDuplicateLetters('ubcjtlppya') == 'ubcjtlpya'
    assert solution.removeDuplicateLetters('lr') == 'lr'
    assert solution.removeDuplicateLetters('uckut') == 'ckut'
    assert solution.removeDuplicateLetters('kqyz') == 'kqyz'
    assert solution.removeDuplicateLetters('mxflghr') == 'mxflghr'
    assert solution.removeDuplicateLetters('wvpbwarj') == 'vpbwarj'
    assert solution.removeDuplicateLetters('tpuntljsc') == 'puntljsc'
    assert solution.removeDuplicateLetters('fe') == 'fe'
    assert solution.removeDuplicateLetters('nbcdpcwk') == 'nbcdpwk'
    assert solution.removeDuplicateLetters('wdzbrbfp') == 'wdzbrfp'
    assert solution.removeDuplicateLetters('fmab') == 'fmab'
    assert solution.removeDuplicateLetters('zseli') == 'zseli'
    assert solution.removeDuplicateLetters('carbyalga') == 'carbylg'
    assert solution.removeDuplicateLetters('fvvtekodlx') == 'fvtekodlx'
    assert solution.removeDuplicateLetters('pafjoblbj') == 'pafjobl'
    assert solution.removeDuplicateLetters('qlvzsxlru') == 'qlvzsxru'
    assert solution.removeDuplicateLetters('v') == 'v'
    assert solution.removeDuplicateLetters('rjf') == 'rjf'
    assert solution.removeDuplicateLetters('jdlqltudh') == 'jdlqtuh'
    assert solution.removeDuplicateLetters('e') == 'e'
    assert solution.removeDuplicateLetters('boncju') == 'boncju'
    assert solution.removeDuplicateLetters('spkcjxowuu') == 'spkcjxowu'
    assert solution.removeDuplicateLetters('fkdtt') == 'fkdt'
    assert solution.removeDuplicateLetters('yq') == 'yq'
    assert solution.removeDuplicateLetters('gbmwxct') == 'gbmwxct'
    assert solution.removeDuplicateLetters('bnezkclhb') == 'bnezkclh'
    assert solution.removeDuplicateLetters('adctio') == 'adctio'
    assert solution.removeDuplicateLetters('cacpxw') == 'acpxw'
    assert solution.removeDuplicateLetters('wyidkxvd') == 'wyidkxv'
    assert solution.removeDuplicateLetters('dito') == 'dito'
    assert solution.removeDuplicateLetters('kpfft') == 'kpft'
    assert solution.removeDuplicateLetters('rzxztgwr') == 'rxztgw'
    assert solution.removeDuplicateLetters('vsknjprjep') == 'vsknjpre'
    assert solution.removeDuplicateLetters('rai') == 'rai'
    assert solution.removeDuplicateLetters('murqjmhplt') == 'murqjhplt'
    assert solution.removeDuplicateLetters('goifvub') == 'goifvub'
    assert solution.removeDuplicateLetters('uf') == 'uf'
    assert solution.removeDuplicateLetters('rnbipy') == 'rnbipy'
    assert solution.removeDuplicateLetters('n') == 'n'
    assert solution.removeDuplicateLetters('xnef') == 'xnef'
    assert solution.removeDuplicateLetters('axmxurtq') == 'amxurtq'
    assert solution.removeDuplicateLetters('dvwn') == 'dvwn'
    assert solution.removeDuplicateLetters('s') == 's'
    assert solution.removeDuplicateLetters('qbl') == 'qbl'
    assert solution.removeDuplicateLetters('fndtiiprh') == 'fndtiprh'
    assert solution.removeDuplicateLetters('kiitn') == 'kitn'
    assert solution.removeDuplicateLetters('gzdjjo') == 'gzdjo'
    assert solution.removeDuplicateLetters('tlvtnf') == 'lvtnf'
    assert solution.removeDuplicateLetters('ohcudd') == 'ohcud'
    assert solution.removeDuplicateLetters('clo') == 'clo'
    assert solution.removeDuplicateLetters('hjhwwq') == 'hjwq'
    assert solution.removeDuplicateLetters('vxtasmjrx') == 'vtasmjrx'
    assert solution.removeDuplicateLetters('zlcyuqxdn') == 'zlcyuqxdn'
    assert solution.removeDuplicateLetters('jiavamiir') == 'javmir'
    assert solution.removeDuplicateLetters('uqmznfx') == 'uqmznfx'
    assert solution.removeDuplicateLetters('jedbpzpoh') == 'jedbpzoh'
    assert solution.removeDuplicateLetters('vekdvsqv') == 'ekdsqv'
    assert solution.removeDuplicateLetters('w') == 'w'
    assert solution.removeDuplicateLetters('rrlukmwad') == 'rlukmwad'
    assert solution.removeDuplicateLetters('osg') == 'osg'
    assert solution.removeDuplicateLetters('qaxcrf') == 'qaxcrf'
    assert solution.removeDuplicateLetters('uepi') == 'uepi'
    assert solution.removeDuplicateLetters('efuchmeqb') == 'efuchmqb'
    assert solution.removeDuplicateLetters('xlwttha') == 'xlwtha'
    assert solution.removeDuplicateLetters('vy') == 'vy'
    assert solution.removeDuplicateLetters('gs') == 'gs'
    assert solution.removeDuplicateLetters('igensi') == 'gensi'
    assert solution.removeDuplicateLetters('yp') == 'yp'
    assert solution.removeDuplicateLetters('wtnaaijalq') == 'wtnaijlq'
    assert solution.removeDuplicateLetters('rrnnsc') == 'rnsc'
    assert solution.removeDuplicateLetters('qhfjrfsvj') == 'qhfjrsv'
    assert solution.removeDuplicateLetters('vh') == 'vh'
    assert solution.removeDuplicateLetters('wy') == 'wy'
    assert solution.removeDuplicateLetters('xrfegls') == 'xrfegls'
    assert solution.removeDuplicateLetters('gkxhoobl') == 'gkxhobl'
    assert solution.removeDuplicateLetters('qjkykkwav') == 'qjkywav'
    assert solution.removeDuplicateLetters('asfd') == 'asfd'
    assert solution.removeDuplicateLetters('rqyyzbug') == 'rqyzbug'
    assert solution.removeDuplicateLetters('gm') == 'gm'
    assert solution.removeDuplicateLetters('cgargnrbft') == 'cagnrbft'
    assert solution.removeDuplicateLetters('tpigylwnsk') == 'tpigylwnsk'
    assert solution.removeDuplicateLetters('bhybdmzfp') == 'bhydmzfp'
    assert solution.removeDuplicateLetters('hpfmostmnc') == 'hpfmostnc'
    assert solution.removeDuplicateLetters('rjeh') == 'rjeh'
    assert solution.removeDuplicateLetters('hxxzls') == 'hxzls'
    assert solution.removeDuplicateLetters('wcnwpans') == 'cnwpas'
    assert solution.removeDuplicateLetters('h') == 'h'
    assert solution.removeDuplicateLetters('ejzwbrjgrp') == 'ejzwbgrp'
    assert solution.removeDuplicateLetters('wszlail') == 'wszail'
    assert solution.removeDuplicateLetters('gixwhxv') == 'giwhxv'
    assert solution.removeDuplicateLetters('yufpxvgmw') == 'yufpxvgmw'
    assert solution.removeDuplicateLetters('mbndpai') == 'mbndpai'
    assert solution.removeDuplicateLetters('dptel') == 'dptel'
    assert solution.removeDuplicateLetters('xb') == 'xb'
    assert solution.removeDuplicateLetters('ldclc') == 'dcl'
    assert solution.removeDuplicateLetters('pyhep') == 'pyhe'
    assert solution.removeDuplicateLetters('io') == 'io'
    assert solution.removeDuplicateLetters('wtgyjqfqor') == 'wtgyjfqor'
    assert solution.removeDuplicateLetters('a') == 'a'
    assert solution.removeDuplicateLetters('lds') == 'lds'

def run_timed_tests(solution):
    assert solution.removeDuplicateLetters('ubcjtlppya') == 'ubcjtlpya'
    assert solution.removeDuplicateLetters('lr') == 'lr'
    assert solution.removeDuplicateLetters('uckut') == 'ckut'
    assert solution.removeDuplicateLetters('kqyz') == 'kqyz'
    assert solution.removeDuplicateLetters('mxflghr') == 'mxflghr'
    assert solution.removeDuplicateLetters('wvpbwarj') == 'vpbwarj'
    assert solution.removeDuplicateLetters('tpuntljsc') == 'puntljsc'
    assert solution.removeDuplicateLetters('fe') == 'fe'
    assert solution.removeDuplicateLetters('nbcdpcwk') == 'nbcdpwk'
    assert solution.removeDuplicateLetters('wdzbrbfp') == 'wdzbrfp'
        

def save_output(output: str):
    with open('../times.csv', 'a') as f:
        f.write(f'{output}\n')

if __name__ == '__main__':
    import sys
    problem_id = 316
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

        output += f'medium_316,{sys.argv[2]},'
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