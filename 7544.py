def count_crosses(n, m, blue_peasants, red_peasants):
    crosses = 0
    blue_peasants = sorted(blue_peasants, key=lambda x: x[1])
    red_peasants = sorted(red_peasants, key=lambda x: x[0])
    b = r = 0
    while b < n and r < m:
        if blue_peasants[b][1] < red_peasants[r][0]:
            crosses += r
            b += 1
        else:
            r += 1
    return crosses

t = int(input().strip())
for scenario in range(1, t + 1):
    n, m = map(int, input().strip().split())
    blue_peasants = [list(map(int, input().strip().split())) for i in range(n)]
    red_peasants = [list(map(int, input().strip().split())) for i in range(m)]
    crosses = count_crosses(n, m, blue_peasants, red_peasants)
    print("Scenario #{}:".format(scenario))
    print(crosses)
    print("")
