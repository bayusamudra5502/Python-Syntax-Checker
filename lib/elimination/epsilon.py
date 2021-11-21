"""
Modul Epsilon
Implementasi Epsilon Elimination pada saat pembentukan CNF
"""

from lib.elimination import Elimination
from lib.cfg import CFG

class EpsilonElimination(Elimination):
  """Kelas Pengeliminasi epsilon pada CFG"""

  def __init__(self, cfg: CFG) -> None:
    super().__init__(cfg)

  def __rule_adder(self, rule, nullableSymbol):
    """Menambahkan segala kemungkinan rule apabila terdapat nullable symbol.
    
    Contoh, bila B adalah nullable symbol, maka ABABA memiliki kemungkinan rule
    AABA, AAA, ABABA, AABA"""

    # Basis: saat rule sudah kosong
    if rule == ():
      return ((),)
    elif rule[0] != nullableSymbol:
      # Rekurens 1: Saat simbol pertama bukan merupakan nullableSymbol,
      #   tidak perlu membuat  kemungkinan epsilon
      lastResult = list(self.__rule_adder(rule[1:], nullableSymbol))

      for i in range(len(lastResult)):
          lastResult[i] = (rule[0], *lastResult[i])
      
      return tuple(lastResult)
    else:
      # Rekurens 2: Saat simbol pertama adalah nullable, perlu membuat
      #   dua kasus, yaitu saat epsilon dan saat tidak epsilon
      lastResult = self.__rule_adder(rule[1:], nullableSymbol)
      appended = []

      for i in lastResult:
        tmp = (rule[0], *i)
        appended.append(tmp)
      
      return (*lastResult, *appended)
  
  def eliminate(self) -> CFG:
    """Melakukan eliminnasi epsilon pada table"""
    rules = super().rules

    # Ubah menjadi tipe data set
    rulesSet = {}
    for i in rules:
      rulesSet[i] = set(rules[i])

    for i in rulesSet:
      if () in rulesSet[i]:
        # Membuang rule epsilon
        rulesSet[i].remove(())

        # Menambahkan kasus epsilon pada tiap rule sebagai
        # konsekuensi dibuangnya rule epsilon
        for j in rulesSet:
          adder = set()
          for rule in rulesSet[j]:
            if i in rule:
              added = self.__rule_adder(rule, i)

              for k in added:
                if not k == ():
                  adder.add(k)
        
          rulesSet[j] = adder.union(rulesSet[j])

    result = {}
    for i in rulesSet:
      result[i] = tuple(rulesSet[i])

    return CFG(result, super().groups, list(super().terminals), super().start)