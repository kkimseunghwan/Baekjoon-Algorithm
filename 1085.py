position = [*map(int, input().split())]

min = 1000
for i in range(0,2):
  if (position[i+2] - position[i]) <= position[i] and (position[i+2] - position[i]) <= min:
    min = position[i+2] - position[i]
  elif (position[i+2] - position[i]) >= position[i] and position[i] <= min:
    min = position[i]
  

print(min)



