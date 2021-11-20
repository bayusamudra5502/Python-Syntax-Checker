# tokenize python source code

import re

class lexer :

    def __init__(self,filename) :
        self.filename = filename
        file = open(self.filename,"r")
        self.tokens = file.read().split()
        file.close()
        
        self.reserved = ["!=", "%", "%=", "&", "&=", r'\(', r'\)', r'\*', r'\*\*',
        r'\*\*\=', r'\*\=', r'\+', r'\+\=',",", "-", "-=", "/", "//", "//=", "/=",
        ":", ";", "<", "<<", "<<=","<=", "<>", "=", "==", ">", ">=", ">>", ">>=",
        "@", r'\[', r'\]', "^", "^=", "`",r'\'\'\'', r'\'', r'\"']

    def tokenize(self) :
        for reserved in self.reserved :
            tempTokens = []
            for string in self.tokens :
                format = r"[A..z]*(" + reserved +r")[A..z]*"
                splitted = re.split(format, string)
                for splitString in splitted :
                    tempTokens.append(splitString)
            self.tokens = tempTokens

        tempTokens = []
        for string in self.tokens:
            splitted = string.split()
            for splitString in splitted :
                tempTokens.append(splitString)

        self.tokens = tempTokens
        self.tokens = [token for token in self.tokens if token!='']
        return self.tokens
        

a = lexer("input.py")
print(a.tokenize())