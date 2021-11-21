"""
Module cnf
Implementasi konverter CFG menjadi CNF
"""

from lib.cfg import CFG
from lib.elimination.epsilon import EpsilonElimination
from lib.elimination.unit import  UnitElimination
from lib.elimination.useless import UselessElimination

class CNF:
  """Kelas Konverter CFG menjadi CNF"""
  def __init__(self, cfg: CFG) -> None:
    self.__cfg = cfg
    self.__rules = {}
    self.__symbolCnt = 0

    # Menghindari Runtime Error
    self.__queue = []
  
  def __simplifyCFG(self):
    """Melakukan simplifikasi CFG"""
    ee = EpsilonElimination(self.__cfg).eliminate()
    ue = UnitElimination(ee).eliminate()
    newCFG = UselessElimination(ue).eliminate()

    self.__rules = {}
    self.__terminals = newCFG.terminals
    self.__groups = newCFG.groups
    self.__start = newCFG.start

    # Mengubah menjadi list supaya mutable
    for i in newCFG.rules:
      self.__rules[i] = list(newCFG.rules[i]) 
      self.__queue.append(i)
  
  def __getNewSymbol(self) -> str:
    """Mendapatkan Nama Symbol baru yang tidak ada di CFG"""
    cnt = self.__symbolCnt
    result = ""

    # Bentuk simbol baru
    while(cnt >= 26):
      result = chr(cnt % 26 + ord("A")) + result
      cnt //= 26
    
    result = chr(cnt + ord("A")) + result
    
    cnt += 1

    if result in self.__rules.keys():
      # Buat simbol baru selanjunya karena simbol sudah ada
      return self.__getNewSymbol()
    else:
      return result
  
  def __simplifyRule(self, rule: tuple) -> tuple:
    """Memberikan rule baru hasil penyederhanaan dan menyesuaikan dengan rule table"""
    if len(rule) < 3:
      # Bila panjangnya sudah < 3, do nothing
      return rule
    else:
      newName = self.__getNewSymbol()

      self.__rules[newName] = tuple(rule[1:])
      self.__queue.append(newName)

      return (rule[0], newName)
  
  def transform(self) -> CFG:
    """Melakukan pengubahan CFG menjadi dalam bentuk CNF"""

    # Menyederhanakan CFG
    self.__simplifyCFG()

    while(len(self.__queue) > 0):
      i = self.__queue.pop(0)
      for j in range(len(self.__rules[i])):
        self.__rules[i][j] = tuple(self.__simplifyRule(self.__rules[i][j]))
    
    return CFG(self.__rules, self.__groups, self.__terminals, self.__start)