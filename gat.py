class _Commit:
    def __init__(self, message: str, committer: str, content:str = None, previous: '_Commit' = None) -> None:
        self.__message = message
        self.__content = content
        self.__committer = committer
        self.__previous = previous

    def getMessage(self) -> str:
        return self.__message

    def getPrevious(self) -> '_Commit':
        return self.__previous

    def __repr__(self) -> str:
        return self.__committer + ' : ' + self.__message


class _Branch:
    def __init__(self, commit: _Commit = _Commit('initial commit', 'system')) -> None:
        self.__head = commit

    @classmethod
    def fromBranch(cls, branch: '_Branch') -> '_Branch':
        return _Branch(branch.__head)

    def addCommit(self, message:str, committer: str, content: str) -> None:
        self.__head = _Commit(message, committer, content, self.__head)

    def head(self) -> str:
        return str(self.__head)

    def currentMessage(self) -> str:
        return self.__head.getMessage()

    def tail(self) -> '_Branch':
        return _Branch(self.__head.getPrevious())

    def isEmpty(self) -> bool:
        return self.__head is None

class Gat:
    """Gat is a version source control system which looks a bit like Git"""

    def __init__(self) -> None:
        """Upon calling the constructor a main branch is created with an initial commit"""
        self.__branches = {'main' : _Branch()}
        self.__current = 'main'

    def status(self) -> str:
        """Show the current branch, with the current commit"""
        return self.__current + ' >> ' + str(self.__branches[self.__current].head())

    def commit(self, message: str, committer: str, content: str) -> None:
        """Adds a commit to the current branch"""
        self.__currentBranch().addCommit(message, committer, content)

    def __currentBranch(self) -> _Branch:
        return self.__branches[self.__current]

    def createBranch(self, name: str):
        """Creates a new branch with a given name, pointing to the current commit"""
        self.__branches[name] = _Branch.fromBranch(self.__currentBranch())

    def checkout(self, name: str) -> str:
        """Switches between branches, returns name of current branch"""
        if name in self.__branches:
            self.__current = name
        return self.__current

    def log(self) -> str:
        """Returns a string of all commits in the current branch"""
        return self.__collectAllCommits(self.__currentBranch())

    def __collectAllCommits(self, cursor: _Branch) -> str:
        if cursor.isEmpty(): 
            return ''
        else:
            return cursor.head() + '\n' + self.__collectAllCommits(cursor.tail())

    def findCommonCommit(self, otherBranchName: str) -> str:
        """Finds the common commit between the current branch and the other branch"""
        return self.__findCommonCommit(self.__branches[otherBranchName])

    def __findCommonCommit(self, cursor: _Branch):
        if self.findCommit(cursor.currentMessage()):
            return cursor.head()            
        else:
           return self.__findCommonCommit(cursor.tail())


    def findCommit(self, message: str) -> bool:
        """Returns True if the commit identified by the message can be found in the current branch"""
        return self.__findCommit(message, self.__currentBranch())

    def __findCommit(self, message: str, cursor: _Branch) -> bool:
        if cursor.isEmpty():
            return False
        elif message == cursor.currentMessage(): 
            return True
        else: 
            return self.__findCommit(message, cursor.tail())




