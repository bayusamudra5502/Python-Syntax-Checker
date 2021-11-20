"""
Module enfa

Modul ini berisi implementasi Finite Automata. Bagian ini
akan digunakan untuk memeriksa kebenaran dari sebuah ekspresi
groups.
"""

class ENFA:
  def __init__(self, rule:str) -> None:
    """Membuat e-Transition Nondeterministic Finite Automata yang dapat dibentuk dari RE.
    
    Rule adalah RE
    """
    self.__rule = rule
  
  def match(self, input: str) -> bool:
    pass
