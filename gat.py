class Gat:
    def __init__(self):
        self.__branches = {'main' : _Branch(_Commit('initial commit','system'))}
        self.__current = 'main'

    def status(self):
        return self.__current + ' >> ' + str(self.__branches[self.__current].head())

    def commit(self, message, committer, content):
        self.__currentBranch().addCommit(
            _Commit(message, committer, content, self.__currentBranch().head()))

    def __currentBranch(self):
        return self.__branches[self.__current]

    def createBranch(self, name):
        self.__branches[name] = self.__currentBranch()

    def checkout(self, name):
        if name in self.__branches:
            self.__current = name

class _Branch:
    def __init__(self, firstCommit):
        self.__head = firstCommit

    def addCommit(self, commit):
        self.__head = commit

    def head(self):
        return self.__head


class _Commit:
    def __init__(self, message, committer, content=None, previous=None):
        self.__message = message
        self.__content = content
        self.__committer = committer
        self.__previous = previous

    def __repr__(self):
        return self.__committer + ' : ' + self.__message
