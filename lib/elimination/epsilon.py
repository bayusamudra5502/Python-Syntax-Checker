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
    if rule == []:
      return [[]]
    elif rule[0] != nullableSymbol:
      # Rekurens 1: Saat simbol pertama bukan merupakan nullableSymbol,
      lastResult = self.__rule_adder(rule[1:], nullableSymbol)

      for i in range(len(lastResult)):
          lastResult[i].insert(0, rule[0])
      
      return lastResult
    else:
      # Rekurens 2: Saat simbol pertama adalah nullable
      lastResult = self.__rule_adder(rule[1:], nullableSymbol)
      appended = []

      for i in lastResult:
        i.insert(0, rule[0])
        appended.append(i)
      
      return [*lastResult, *appended]
  
  def eliminate(self) -> CFG:
    """Melakukan eliminnasi epsilon pada table"""
    result = self.__cfg.rules

    for i in result:
      if [] in result[i]:
        result[i].remove([])

        for j in result:
          addSymbol = []

          for rule in result[j]:
            if i in rule:
              added = self.__rule_adder(rule, i)

              for i in added:
                # Biar unik dan tidak menambahkan epsilon
                if not i in addSymbol and not i in result[j] and not i == []:
                  addSymbol.append(i)
            
          result[j] = [*result[j], *addSymbol]

    return CFG(result, self.__cfg.groups, self.__cfg.terminals)