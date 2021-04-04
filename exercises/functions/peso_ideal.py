def peso_ideal_masc(h):
  calc = 72.7 * h - 58
  return calc

def peso_ideal_fem(h):
  calc = 62.1*h - 44.7
  return calc

def peso_ideal(h):
  PM = peso_ideal_masc(h)
  PF = peso_ideal_fem(h)
  return print(f'{PM:.2f} {PF:.2f}')

altura = float(input())
peso_ideal(altura)