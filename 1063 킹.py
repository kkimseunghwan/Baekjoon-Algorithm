
# 1063 킹

from sys import stdin
move = {
    'R':(0, 1),
    'L':(0,-1),
    'B':(1, 0),
    'T':(-1,0),
    'RT':(-1,1),
    'LT':(-1,-1),
    'RB':(1, 1),
    'LB':(1,-1)

}

king, stone, N = map(str, stdin.readline().split())

# y, x)
king = ( 8 - int(king[1]), ord(king[0]) - 65)
stone = ( 8 - int(stone[1]), ord(stone[0]) - 65)
N = int(N)

for _ in range(N):
    m = stdin.readline().strip()

    y, x = king
    sy, sx = stone
    ny, nx = move[m]

    if (0 <= y+ny < 8) and (0 <= x+nx < 8):
        if ((y+ny, x+nx) == (sy, sx)):
            if (0 <= sy+ny < 8) and (0 <= sx+nx < 8):
                stone = (sy+ny, sx+nx)
            else:
                continue
        king = (y+ny, x+nx)



print( ''.join([ chr(king[1] + 65), str(8 - king[0])] ))
print( ''.join([chr(stone[1] + 65), str(8 - stone[0])] ))

