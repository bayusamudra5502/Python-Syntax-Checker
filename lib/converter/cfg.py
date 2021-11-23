"""
module CFG2Json
Melakukan loading file cfg.txt sesuai format dan mengubahnya ke file json
"""

from lib.cfg import CFG

def loadCFG(file: str) -> CFG:
  fi = open(file, "r")

  data = fi.read().splitlines()
  fi.close()

  result = {
    "start": "",
    "rules": {},
    "groups": {},
    "terminals": []
  }

  mode = 0

  for i in data:
    if len(i) >= 2 and i[:2] == "//" or len(i) == 0 or i.isspace():
      pass
    elif len(i) >= 6 and i[:6] == "Start:":
      mode = 1
    elif len(i) >= 6 and i == "Rules:":
      mode = 2
    elif len(i) >= 10 and i == "Terminals:":
      mode = 3
    elif len(i) >= 7 and i == "Groups:":
      mode = 4
    else:
      if mode == 1:
        result["start"] = i
      elif mode == 2:
        ruleName, ruleData = i.split("->")
        ruleName = ruleName.strip()

        truncatedRule = map(lambda x: x.strip().split(" ") ,ruleData.split("|"))

        result["rules"][ruleName] = list(truncatedRule)
      elif mode == 3:
        result["terminals"].append(i)
      elif mode == 4:
        groupName, groupData = i.split("=")
        groupName = groupName.strip()
        groupData = groupData.strip()
        result["groups"][groupName] = groupData
  
  return CFG(result["rules"], result["groups"], result["terminals"], result["start"])

def convertCFGToJson(file: str, output: str) -> None:
  obj = loadCFG(file)
  obj.saveToJSON(output)

def convertCFGToYaml(file: str, output: str) -> None:
  obj = loadCFG(file)
  obj.saveToYAML(output)