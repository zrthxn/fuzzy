from fuzzy import Set
from math import sqrt

"""
Word Operations on Approximate logic
"""

def very(op: Set):
  res = list()
  for el in op.set:
    res.append((el[0]**2, el[1]))
  return Set(res)

def quite(op: Set):
  res = list()
  for el in op.set:
    res.append((sqrt(el[0]), el[1]))
  return Set(res)
