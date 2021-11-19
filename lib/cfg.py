""" Module cfg
Modul ini digunakan untuk menyimpan model dari CFG yang digunakan
"""

import yaml
import json
import re

class CFG:
  def __init__(self, rules: dict, groups: dict, terminals: list) -> None:
    self.__rules = rules
    self.__groups = groups
    self.__terminals = terminals
    self.__build_inverted()

  def __build_inverted(self):
    self.__inverted_cfg = {}

    for i in self.__rules:
      for j in self.__rules[i]:
        if j in self.__inverted_cfg:
          self.__inverted_cfg[j].append(i)
        else:
          self.__inverted_cfg[j] = [i]

  @classmethod
  def loadFromJSON(cls, path: str):
    """Memuat data dari file JSON."""
    f = open(path)
    data = json.load(f)
    f.close()

    return cls(data.rules, data.groups, data.terminals)
  
  @classmethod
  def loadFromYAML(cls, path: str):
    """Memuat data dari file YAML."""
    f = open(path)
    data = yaml.safe_load(f)
    f.close()
    
    return cls(data.rules, data.groups, data.terminals)
  
  def saveToYAML(self, path: str):
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
  
  def saveRules(self, path:str):
    """Simpan Rules ke sebuah file. Rules yang disimpan sesuai dengan sintak CFG"""
    f = open(path, "w")
    
    lines = []
    for i in self.__rules:
      strRule = f"{i} -> {' | '.join(self.__rules[i])}"
      lines.append(strRule)
    
    f.writelines(lines)
    f.close()
  
  def getCFG(self):
    """Mendapatkan data CFG"""
    return self.__rules
  
  def getInverted(self):
    """Mendapatkan simbol pembangkit dari key"""
    return self.__inverted_cfg
  
  def getVariables(self) -> list:
    """Mendapatkan semua Variabel"""
    return list(self.__rules.keys())
  
  def getGroupsChecker(self):
    """Mendapatkan fungsi pemeriksa karakter dari groups"""
    result = {}
    for i in self.__groups:
      result[i] = lambda x: re.match(self.__groups[i], x)
    
    return result

  def isTerminal(self, symbol: str):
    """Mengembalikan true bila symbol merupakan terminal"""
    result = symbol in self.__terminals

    if result:
      return True
    else:
      checker = self.getGroupsChecker()
      for i in checker:
        result = checker[i](symbol)
      
      return result
  
  def isVariables(self, symbol:str):
    """Mengembalikan true bila symbol adalah variable"""
    return symbol in self.getVariables()
  
  def getGroupName(self, symbol: str):
    """Mengembalikan nama simbol. Mengembalikan None bila bukan merupakan group."""
    checker = self.getGroupsChecker()

    for i in checker:
      if checker[i](symbol):
        return i
    
    return None