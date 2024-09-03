from sys import stdin 

#  1m2당 참외의 개수 K (1 ≤ K ≤ 20)
K = int( stdin.readline() )

field = []
for _ in range(6):
  way, dis = map(int, stdin.readline().split())
  field.append( (way, dis) )

max_width, index_width, max_height, index_height = 0, 0, 0, 0
for way, dis in field:
  if way in (1,2) and max_width < dis:
    max_width = dis
    index_width = field.index((way, dis))
  if way in (3,4) and max_height < dis:
    max_height = dis
    index_height = field.index((way, dis))

field[index_width-1] = (0,0)
field[index_width] = (0,0)
field[index_width+1 if index_width+1 < 6 else 0] = (0,0)
field[index_height-1] = (0,0)
field[index_height] = (0,0)
field[index_height+1 if index_height+1 < 6 else 0] = (0,0)

excep_extent = 1
for way, dis in field:
  if way != 0:
    excep_extent *= dis

all_extent = max_width * max_height

print((all_extent - excep_extent) * K)