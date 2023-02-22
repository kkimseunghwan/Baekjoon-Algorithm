
while True:
  a = input()
  if a == "0": break
  if ''.join(reversed(a)) == a: print("yes")
  else: print("no")

