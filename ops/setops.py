from fuzzy import Set

"""
Operations on Fuzzy Sets
"""

def andx(a: Set, b: Set):
  intesection = list()
  for el in a:
    if b.value(el[1]) != None:
      intesection.append((min(el[0], b.value(el[1])), el[1]))
  return Set(intesection)

def orx(a: Set, b: Set):
  union = list()
  for el in a:
    if b.value(el[1]) != None:
      union.append((max(el[0], b.value(el[1])), el[1]))
    else:
      union.append(el)

  for el in b:
    if a.value(el[1]) == None:
      union.append(el)
  return Set(union)

def notx(op: Set):
  invert = list()
  for el in op.set:
    invert.append((1 - el[0], el[1]))
  return Set(invert)