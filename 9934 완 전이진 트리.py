from sys import stdin

k = int(stdin.readline())

visit = list(map(int, stdin.readline().split()))

building = {}
for i in range(k):
    building[i] = []



def GetTree(node, visit, loc):
    if node <= 1:
        building[loc].append(visit[0])
        return
    
    node = node//2
    building[loc].append(visit[node])
    
    GetTree(node, visit[:node], loc+1)
    GetTree(node, visit[node+1:], loc+1)

GetTree(2**k-1, visit, 0)

for value in building.values():
    print(" ".join(map(str, value)))



