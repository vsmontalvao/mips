import re

class FileReader():
    def __init__(self):
        self.instArray = {}

    def read(self, fileName):
        # checking if files exists
        try:
            with open(fileName): pass
        except IOError:
            print "File does not exist."

        # reading file and adding instructions to list
        i = 0
        with open(fileName) as f:
            for line in f:
                m = re.search('([01]*)(\s+)(;)(.*)', line)
                self.instArray[i] = [ m.group(1).strip(), m.group(4).strip() ]
                i += 1

    def getInst(self, i):
        return self.instArray[i][0]

    def getIdent(self, i):
        return self.instArray[i][1]

    def count(self):
        return len(self.instArray)

