"""
Module enfa

Modul ini berisi implementasi Finite Automata. Bagian ini
akan digunakan untuk memeriksa kebenaran dari sebuah ekspresi
groups.
"""

from lib.fa.builder import plusBuilder
from lib.fa.state import State

class ENFA:
  def __init__(self, rule:str) -> None:
    """Membuat e-Transition Nondeterministic Finite Automata yang dapat dibentuk dari RE.
    
    Rule adalah RE
    """
    self.__rule = rule
    self.__fit = False
    self.__start = None
    self.__end = None

  def fit(self):
    """Membentuk state dari e-NFA"""
    first, end = plusBuilder(self.__rule)
    self.__start = first
    self.__end = end
    self.__fit = True
  
  def __follow(self, input, node):
    if node == None:
      return False
    elif input == "" and  node == self.__end:
      return True
    else:
      i = 0
      res = False

      if len(input) > 0:
        loc = node.next(input[0])

        while(not res and i < len(loc)):
          res = self.__follow(input[1:], loc[i])
          i += 1
      
      loc = node.next("")

      while(not res and i < len(loc)):
        res = self.__follow(input, loc[i])
        i += 1

      return res

  def match(self, input: str) -> bool:
    if not self.__fit:
      raise Exception("e-NFA belum di fit")
    else:
      return self.__follow(input, self.__start)