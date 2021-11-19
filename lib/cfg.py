""" Module cfg
Modul ini digunakan untuk menyimpan model dari CFG yang digunakan
"""

import yaml
import json
import re

class CFG:
  def __init__(self, rules: dict, groups: dict, terminals: list) -> None:
    tmpRules = rules

    for i in tmpRules:
      data = tmpRules[i]
      for j in range(len(data)):
        data[j] = tuple(data[j])
      
      tmpRules[i] = tuple(data)

    self.__rules = tmpRules
    self.__groups = groups
    self.__terminals = tuple(terminals)

  @classmethod
  def loadFromJSON(cls, path: str) -> None:
    """Memuat data dari file JSON."""
    f = open(path)
    data = json.load(f)
    f.close()

    return cls(data["rules"], data["groups"], data["terminals"])
  
  @classmethod
  def loadFromYAML(cls, path: str) -> None:
    """Memuat data dari file YAML."""
    f = open(path)
    data = yaml.safe_load(f)
    f.close()

    return cls(data["rules"], data["groups"], data["terminals"])
  
  @property
  def groups(self) -> dict:
    """Mengembalikan groups CFG"""
    return self.__groups
  
  @property
  def terminals(self) -> tuple:
    """Mengembalikan terminal pada CFG"""
    return self.__terminals
  
  @property
  def rules(self) -> dict:
    """Mendapatkan data CFG"""
    return self.__rules
  
  def saveToYAML(self, path: str) -> None:
    """Simpan CFG ke file YAML"""
    f = open(path, "w")
    obj = {
      "groups": self.__groups,
      "terminals": self.__terminals,
      "rules": self.__groups
    }
    
    yaml.dump(obj, f)
    f.close()
  
  def saveToJSON(self, path:str):
    """Simpan CFG ke file JSON"""
    f = open(path, "w")
    obj = {
      "groups": self.__groups,
      "terminals": self.__terminals,
      "rules": self.__groups
    }
    
    json.dump(obj, f)
    f.close()
  
  def saveRules(self, path:str) -> None:
    """Simpan Rules ke sebuah file. Rules yang disimpan sesuai dengan sintak CFG"""
    f = open(path, "w")
    
    lines = []
    for i in self.__rules:
      symbolStr = []
      for j in self.__rules[i]:
        symbolStr.append(" ".join(j))

      strRule = f"{i} -> {' | '.join(symbolStr)}"
      lines.append(strRule)
    
    f.writelines(lines)
    f.close()
  
  def getInvertedTable(self) -> dict:
    """Mendapatkan simbol pembangkit dari key"""
    inverted_cfg = {}

    for i in self.__rules:
      for j in self.__rules[i]:
        if j in inverted_cfg:
          if not i in inverted_cfg[j]:
            inverted_cfg[j] += (i,)
        else:
          inverted_cfg[j] = (i,)

    return inverted_cfg
  
  def getVariables(self) -> tuple:
    """Mendapatkan semua Variabel"""
    return tuple(self.__rules.keys())
  
  def getGroupsChecker(self):
    """Mendapatkan fungsi pemeriksa karakter dari groups"""
    result = {}
    for i in self.__groups:
      result[i] = lambda x: re.match(self.__groups[i], x)
    
    return result

  def isTerminal(self, symbol: str) -> bool:
    """Mengembalikan true bila symbol merupakan terminal"""
    result = symbol in self.__terminals

    if result:
      return True
    else:
      checker = self.getGroupsChecker()
      for i in checker:
        result = checker[i](symbol)
      
      return result
  
  def isVariables(self, symbol:str) -> bool:
    """Mengembalikan true bila symbol adalah variable"""
    return symbol in self.getVariables()
  
  def getGroupName(self, symbol: str) -> object:
    """Mengembalikan nama simbol. Mengembalikan None bila bukan merupakan group."""
    checker = self.getGroupsChecker()

    for i in checker:
      if checker[i](symbol):
        return i
    
    return None