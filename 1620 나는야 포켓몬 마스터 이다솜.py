from sys import stdin
N, M = map(int, stdin.readline().split())
poke = {}
pokeNum = {}

for i in range(N):
  pokeName = stdin.readline().strip()
  poke[i+1] = pokeName
  pokeNum[pokeName] = i + 1

for _ in range(M):
  search = stdin.readline().strip()
  try:
    float(search)
    print(poke[int(search)])
  except ValueError:
    print(pokeNum[search])
    
