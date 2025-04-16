from hard_358_canon import Solution as SolutionCanon
from chatgpt_hard_358 import Solution as SolutionChatGPT
from claude_hard_358 import Solution as SolutionClaude
from gemini_hard_358 import Solution as SolutionGemini


def run_basic_tests(solution):
    
    assert solution.rearrangeString('aabbcc', 3) == 'abcabc'
    assert solution.rearrangeString('aaabc', 3) == ''
    assert solution.rearrangeString('aaadbbcc', 2) == 'abacabcd'

def run_advanced_tests(solution):
    assert solution.rearrangeString('by', 0) == 'by'
    assert solution.rearrangeString('olu', 1) == 'lou'
    assert solution.rearrangeString('cuigkxmgv', 4) == 'gcikgmuvx'
    assert solution.rearrangeString('kucgbvgnefy', 8) == 'gbcefknugvy'
    assert solution.rearrangeString('znvpkq', 5) == 'knpqvz'
    assert solution.rearrangeString('bq', 2) == 'bq'
    assert solution.rearrangeString('ura', 3) == 'aru'
    assert solution.rearrangeString('ettdnyj', 6) == 'tdejnyt'
    assert solution.rearrangeString('ntxy', 1) == 'ntxy'
    assert solution.rearrangeString('cxruog', 2) == 'cgorux'
    assert solution.rearrangeString('hljbyxsno', 4) == 'bhjlnosxy'
    assert solution.rearrangeString('ayes', 3) == 'aesy'
    assert solution.rearrangeString('mryxn', 1) == 'mnrxy'
    assert solution.rearrangeString('yyubex', 0) == 'ybeuxy'
    assert solution.rearrangeString('cvdymy', 2) == 'ycdmvy'
    assert solution.rearrangeString('krb', 1) == 'bkr'
    assert solution.rearrangeString('sbfmpop', 4) == 'pbfmops'
    assert solution.rearrangeString('tpqikb', 6) == 'bikpqt'
    assert solution.rearrangeString('ahmxrgo', 3) == 'aghmorx'
    assert solution.rearrangeString('l', 1) == 'l'
    assert solution.rearrangeString('wodptubbdr', 2) == 'bdbdoprtuw'
    assert solution.rearrangeString('flvpjh', 0) == 'fhjlpv'
    assert solution.rearrangeString('el', 1) == 'el'
    assert solution.rearrangeString('nzqm', 3) == 'mnqz'
    assert solution.rearrangeString('uytepinc', 2) == 'ceinptuy'
    assert solution.rearrangeString('vwoluyfg', 3) == 'fglouvwy'
    assert solution.rearrangeString('fbqgxhr', 7) == 'bfghqrx'
    assert solution.rearrangeString('ejumpt', 1) == 'ejmptu'
    assert solution.rearrangeString('ilckb', 3) == 'bcikl'
    assert solution.rearrangeString('lrbvydokgtm', 0) == 'bdgklmortvy'
    assert solution.rearrangeString('ylsfsp', 2) == 'sflpsy'
    assert solution.rearrangeString('pfpnuzemd', 5) == 'pdefmnpuz'
    assert solution.rearrangeString('ddkqehwsfkn', 7) == 'dkefhnqdksw'
    assert solution.rearrangeString('pg', 2) == 'gp'
    assert solution.rearrangeString('wqlgijsdegy', 10) == 'gdeijlqswyg'
    assert solution.rearrangeString('xfpm', 2) == 'fmpx'
    assert solution.rearrangeString('bf', 0) == 'bf'
    assert solution.rearrangeString('ummaesl', 6) == 'maelsum'
    assert solution.rearrangeString('xdiu', 3) == 'diux'
    assert solution.rearrangeString('mvqvswttr', 3) == 'tvmqrstvw'
    assert solution.rearrangeString('kqsbgjtn', 1) == 'bgjknqst'
    assert solution.rearrangeString('dovz', 4) == 'dovz'
    assert solution.rearrangeString('pacjjnyuj', 1) == 'jjacjnpuy'
    assert solution.rearrangeString('ug', 1) == 'gu'
    assert solution.rearrangeString('mpgl', 2) == 'glmp'
    assert solution.rearrangeString('ljkt', 3) == 'jklt'
    assert solution.rearrangeString('xe', 2) == 'ex'
    assert solution.rearrangeString('nv', 2) == 'nv'
    assert solution.rearrangeString('eooiker', 3) == 'eoiekor'
    assert solution.rearrangeString('zgysa', 2) == 'agsyz'
    assert solution.rearrangeString('himjqvqdr', 2) == 'qdhijmqrv'
    assert solution.rearrangeString('ttjdsn', 2) == 'tdjnst'
    assert solution.rearrangeString('njx', 1) == 'jnx'
    assert solution.rearrangeString('sdgi', 0) == 'dgis'
    assert solution.rearrangeString('nnbzfvts', 2) == 'nbfnstvz'
    assert solution.rearrangeString('islcueitw', 6) == 'icelstiuw'
    assert solution.rearrangeString('rwz', 2) == 'rwz'
    assert solution.rearrangeString('dxicbulqw', 2) == 'bcdilquwx'
    assert solution.rearrangeString('yrqdkisr', 5) == 'rdikqrsy'
    assert solution.rearrangeString('kf', 2) == 'fk'
    assert solution.rearrangeString('iyac', 0) == 'aciy'
    assert solution.rearrangeString('nytxhzmzn', 0) == 'nzhmntxyz'
    assert solution.rearrangeString('uhoijna', 0) == 'ahijnou'
    assert solution.rearrangeString('w', 1) == 'w'
    assert solution.rearrangeString('mjzb', 4) == 'bjmz'
    assert solution.rearrangeString('h', 0) == 'h'
    assert solution.rearrangeString('oexakxkgny', 0) == 'kxaegknoxy'
    assert solution.rearrangeString('j', 0) == 'j'
    assert solution.rearrangeString('bxyvexcfn', 5) == 'xbcefnvxy'
    assert solution.rearrangeString('vwxcopdgwso', 1) == 'owcdgopsvwx'
    assert solution.rearrangeString('rlwt', 0) == 'lrtw'
    assert solution.rearrangeString('mkynolgsfdz', 10) == 'dfgklmnosyz'
    assert solution.rearrangeString('zohnpiqyah', 5) == 'hainohpqyz'
    assert solution.rearrangeString('ftugnzg', 2) == 'gfgntuz'
    assert solution.rearrangeString('jriqc', 4) == 'cijqr'
    assert solution.rearrangeString('lpshwquwfz', 6) == 'wfhlpqsuwz'
    assert solution.rearrangeString('sgutid', 6) == 'dgistu'
    assert solution.rearrangeString('qoljk', 5) == 'jkloq'
    assert solution.rearrangeString('gctedgmdgou', 2) == 'gdgcdegmotu'
    assert solution.rearrangeString('hilzrxlfv', 3) == 'lfhilrvxz'
    assert solution.rearrangeString('xiqhlapf', 4) == 'afhilpqx'
    assert solution.rearrangeString('xocka', 5) == 'ackox'
    assert solution.rearrangeString('vrnodhe', 4) == 'dehnorv'
    assert solution.rearrangeString('zlsst', 3) == 'sltsz'
    assert solution.rearrangeString('vof', 3) == 'fov'
    assert solution.rearrangeString('swzgzuciyt', 2) == 'zcgistuwyz'
    assert solution.rearrangeString('e', 0) == 'e'
    assert solution.rearrangeString('ofpnlgadio', 0) == 'oadfgilnop'
    assert solution.rearrangeString('gpapb', 3) == 'pabgp'
    assert solution.rearrangeString('rox', 0) == 'orx'
    assert solution.rearrangeString('be', 1) == 'be'
    assert solution.rearrangeString('hpvtq', 2) == 'hpqtv'
        

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