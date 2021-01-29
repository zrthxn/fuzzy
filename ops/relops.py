from relations import Relation

"""
Operations on Relations
"""

def maxomin(row: list, col: list):
  return max(
    [ min(row[m], col[m]) ] for m in range(len(row))
  )

def suboprod(row: list, col: list):
  prod = 1
  for p in ([ row[m] - col[m] ] for m in range(len(row))):
    prod *= p
  return round(prod, ndigits=3)

def compose(src: Relation, tar: Relation, func: callable = maxomin) -> Relation:
  if len(src.rel[0]) != len(tar.rel):
    raise IndexError("Mismatched dimensions")

  composition = list()
  for x in range(len(src.rel)):
    row = src.row(x)
    new = list()
    for y in range(len(tar.rel[0])):
      col = tar.col(y)
      if len(row) != len(col):
        raise IndexError("Mismatched dimensions")

      new.append(func(row, col))
    composition.append(new)

  res = src
  res.rel = composition
  return res
