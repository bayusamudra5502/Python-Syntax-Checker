"""
Module fa

Modul ini berisi implementasi Finite Automata. Bagian ini
akan digunakan untuk memeriksa kebenaran dari sebuah ekspresi
groups.
"""

class FA:
  def __init__(self, rule:str) -> None:
    """Membuat Finite Automata yang dapat dibentuk dari RE.
    
    Rule adalah RE
    """
    self.__rule = rule
  
  def match(self, input: str) -> bool:
    pass

class State:
  def __init__(self) -> None:
      self.__transition = {}
  
  def addTransition(self, rule: str, next):
    if rule in self.__transition:
      self.__transition[rule] += (next,)
    else:
      self.__transition[rule] = (next,)

  def next(self, input:str):
    if not input in self.__transition:
      return None
    elif len(self.__transition[input]) == 1:
      return self.__transition[input][0]
    elif len(self.__transition[input]) > 1:
      return self.__transition[input]