class Gat:
    """Gat is a version source control system which looks a bit like Git"""

    def __init__(self):
        """Upon calling the constructor a main branch is created with an initial commit"""
        self.__branches = {'main' : _Branch(_Commit('initial commit','system'))}
        self.__current = 'main'

    def status(self):
        """Show the current branch, with the current commit"""
        return self.__current + ' >> ' + str(self.__branches[self.__current].head())

    def commit(self, message, committer, content):
        """Adds a commit to the current branch"""
        self.__currentBranch().addCommit(
            _Commit(message, committer, content, self.__currentBranch().head()))

    def __currentBranch(self):
        return self.__branches[self.__current]

    def createBranch(self, name):
        """Creates a new branch with a given name, pointing to the current commit"""
        self.__branches[name] = _Branch(self.__currentBranch().head())

    def checkout(self, name):
        """Switches between branches"""
        if name in self.__branches:
            self.__current = name

    def log(self):
        """Returns a string of all commits in the current branch"""
        return self.__collectAllCommits(self.__currentBranch().head())

    def __collectAllCommits(self, cursor):
        if cursor is None: 
            return ''
        else:
            return str(cursor) + '\n' + self.__collectAllCommits(cursor.getPrevious())

    def findCommonCommit(self, otherBranchName):
        """Finds the common commit between the current branch and the other branch"""
        return str(self.__findCommonCommit(self.__branches[otherBranchName].head()))

    def __findCommonCommit(self, cursor):
        if self.findCommit(cursor.getMessage()):
            return cursor            
        else:
           return self.__findCommonCommit(cursor.getPrevious())


    def findCommit(self, message):
        """Returns True if the commit identified by the message can be found in the current branch"""
        return self.__findCommit(message, self.__currentBranch().head())

    def __findCommit(self, message, cursor):
        if cursor is None:
            return False
        elif message == cursor.getMessage(): 
            return True
        else: 
            return self.__findCommit(message, cursor.getPrevious())

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

    def getMessage(self):
        return self.__message
    
    def getPrevious(self):
        return self.__previous

    def __repr__(self):
        return self.__committer + ' : ' + self.__message
