def printScore(score):
  score = int(score)
  if score < 60:
    return "F"
  elif score < 70:
    return "D"
  elif score < 80:
    return "C"
  elif score < 90:
    return "B"
  else:
    return "A"

a = input()
print(printScore(a))