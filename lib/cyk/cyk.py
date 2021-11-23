import json
from lib.cyk.lexer import Lexer
from lib.fa.enfa import ENFA

# valid string/variable syntax
var = ENFA("(a-z+A-Z+\\_)(a-z+A-Z+\\_+0-9)*")
string = ENFA("(a-z+A-Z+0-9)*")
int = ENFA("(0-9)*")
var.fit()
string.fit()
int.fit()

class CYK :

    def __init__(self, grammar_file, sc_file) :
        cs = Lexer(sc_file)
        self.tokens = cs.tokenize()     # tokenize source code input
        self.length = len(self.tokens)
        self.cyk_table = None
        file = open(grammar_file, 'r')  # load grammar
        self.grammar = json.load(file)['rules']
        self.cnf = {}
        # convert to { rightHandProduction : leftHandProduction for easier matching}
        for x,y in self.grammar.items():
            for rule in y  :
                combined = "".join(rule)
                rules= self.cnf.get(combined)
                if (rules == None):
                    self.cnf.update({combined : [x]})
                else :
                    self.cnf[combined].append(x)

                
    def parse(self) :

        self.cyk_table = [[[] for i in range(self.length-j)] for j in range(self.length)]
        # isi baris pertama
        for i, t in enumerate(self.tokens):
            try :
                self.cyk_table[0][i].extend(self.cnf[t])
            except KeyError :
                if (var.match(t)):
                    self.cyk_table[0][i].extend(self.cnf['name']) # tergantung hasil cnf
                elif (string.match(t)):
                    self.cyk_table[0][i].extend(self.cnf['string']) # tergantung hasil cnf
                elif (int.match(t)):
                    self.cyk_table[0][i].extend(self.cnf['number']) # tergantung hasil cnf
                else :
                    continue
        
        # isi baris selanjutnya
        for i in range(2,self.length+1):
            for j in range(1,self.length-i+2):
                for k in range(1,i):

                    cell1 = self.cyk_table[k-1][j-1]
                    cell2 = self.cyk_table[k-1][j-1]

                    for a in cell1 :
                        for b in cell2 :
                            try :
                                self.cyk_table[i-1][j-1].extend(self.cnf[a+b])  
                            except :
                                continue

        return self.cyk_table 

