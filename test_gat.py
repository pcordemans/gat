from gat import Gat

def test_initial_commit():
    vcs = Gat()
    assert(vcs.status() == 'main >> system : initial commit')

def test_first_commit():
    vcs = Gat()
    vcs.commit('first commit', 'piet', 'somethings')
    assert(vcs.status() == 'main >> piet : first commit')


def test_branch():
    vcs = Gat()
    vcs.commit('first commit', 'piet', 'somethings')
    vcs.createBranch('dev')
    vcs.checkout('dev')
    assert(vcs.status() == 'dev >> piet : first commit')

def test_commitAfterBranch():
    vcs = Gat()
    vcs.commit('first commit', 'piet', 'somethings')
    vcs.createBranch('dev')
    vcs.checkout('dev')
    vcs.commit('2nd commit', 'nico', 'other things')
    assert(vcs.status() == 'dev >> nico : 2nd commit')

def test_commitAfterBranchOriginalBranchUnchanged():
    vcs = Gat()
    vcs.commit('first commit', 'piet', 'somethings')
    vcs.createBranch('dev')
    vcs.checkout('dev')
    vcs.commit('2nd commit', 'nico', 'other things')
    vcs.checkout('main')
    assert(vcs.status() == 'main >> piet : first commit')

def test_log():
    vcs = Gat()
    vcs.commit('first commit', 'piet', 'somethings')
    vcs.commit('2nd commit', 'nico', 'other things')
    assert(vcs.log()=='nico : 2nd commit\npiet : first commit\nsystem : initial commit\n')

def test_logDifferentBranches():
    vcs = Gat()
    vcs.commit('first commit', 'piet', 'somethings')
    vcs.createBranch('dev')
    vcs.checkout('dev')
    vcs.commit('2nd commit', 'nico', 'other things')
    assert(vcs.log() =='nico : 2nd commit\npiet : first commit\nsystem : initial commit\n')
    vcs.checkout('main')
    assert(vcs.log() == 'piet : first commit\nsystem : initial commit\n')
    vcs.commit('3rd','sille','some')
    assert(vcs.log() == 'sille : 3rd\npiet : first commit\nsystem : initial commit\n')
    vcs.checkout('dev')
    assert(vcs.log() ==
           'nico : 2nd commit\npiet : first commit\nsystem : initial commit\n')


def test_find():
    vcs = Gat()
    vcs.commit('first commit', 'piet', 'somethings')
    vcs.commit('2nd commit', 'nico', 'other things')
    assert(vcs.findCommit('first commit') == True)
    assert(vcs.findCommit('3rd') == False)
    assert(vcs.findCommit('initial commit') == True)

def test_findCommonCommitBetweenTwoBranches():
    vcs = Gat()
    vcs.commit('first commit', 'piet', 'somethings')
    vcs.createBranch('dev')
    vcs.checkout('dev')
    assert(vcs.findCommonCommit('main') == 'piet : first commit')
    vcs.commit('2nd commit', 'nico', 'other things')
    assert(vcs.findCommonCommit('main') == 'piet : first commit')
    vcs.checkout('main')
    assert(vcs.findCommonCommit('dev') == 'piet : first commit')
    vcs.commit('3rd', 'sille', 'things')
    assert(vcs.findCommonCommit('dev') == 'piet : first commit')
    
    
