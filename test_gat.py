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

def test_log():
    vcs = Gat()
    vcs.commit('first commit', 'piet', 'somethings')
    vcs.commit('2nd commit', 'nico', 'other things')
    assert(vcs.log()=='nico : 2nd commit\npiet : first commit\nsystem : initial commit\n')

def test_find():
    vcs = Gat()
    vcs.commit('first commit', 'piet', 'somethings')
    vcs.commit('2nd commit', 'nico', 'other things')
    assert(vcs.findCommit('first commit') == True)
    assert(vcs.findCommit('3rd') == False)
