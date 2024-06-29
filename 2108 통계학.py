from sys import stdin
def manyNum(ln):
  ld = {}
  for i in ln:
    if i in ld:
        ld[i] += 1
    else:
        ld[i] = 1
  max_value = max(ld.values())
  max_keys = [key for key, value in ld.items() if value == max_value]
  if len(max_keys) > 1:
    return sorted(max_keys)[1]
  else:
    return max_keys[0]
    
N = int(stdin.readline().strip())
ln = [int(stdin.readline().strip()) for _ in range(N)]
ln.sort()
print(round(sum(ln)/N))
print(ln[N // 2])
print(manyNum(ld))
print(max(ln) - min(ln))
