"""
Modul state
Modul implementasi Finite Automata State
"""

from time import time_ns

class State:
  def __init__(self) -> None:
      self.__transition = {}
      self.__sid = time_ns()

  @property
  def sid(self):
    return self.__sid

  def __hash__(self) -> int:
    return self.__sid
  
  def __eq__(self, __o) -> bool:
    self.__sid == __o.sid
  
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

  def eclose(self, lastSet: set = set()) -> tuple:
    if self.next("") == None:
      return (self)
    else:
      ecloseState = {self, *lastSet}
      for i in self.next(""):
        if not i in lastSet:
          # Susun eclose secara rekursi
          i.eclose(ecloseState)
      
      return tuple(ecloseState)