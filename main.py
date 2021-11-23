from lib.cyk.cyk import CYK

o = CYK("data/cnf-repaired.json", "test/tc/tc2.py")
print(o.parse())

print(o.validityCheck())