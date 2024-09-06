#1927 최소힙
from sys import stdin

def min_Heap_Append(heap, item, heapLen):
  i = heapLen
  heap.append(item) # 힙 크기를 하나 증가하고 마지막 노드에 x를 넣는다.

  while i > 1:
    if heap[i] < heap[i//2]:
      heap[i], heap[i//2] = heap[i//2], heap[i]
      i = i//2
    else:
      break


def min_Heap_Pop(heap, heapLen):
  item = heap[1] # 최소값 저장
  heap[1] = heap[heapLen] # 마지막 노드를 루트 노드로 이동
  heap.pop() # 마지막 노드 삭제
  heapLen -= 1 # 힙 크기 하나 감소

  i = 1 # 루트 노드 검사 시작.
  while i*2 <= heapLen:
    left = i*2
    right = i*2+1

    if right <= heapLen: # 노드가 오른쪽에 존재하는지 확인. (2개 남음 대비)
      if heap[i] < heap[i*2] and heap[i] < heap[i*2+1]:
        break
      elif heap[i*2] < heap[i*2+1]:
        heap[i], heap[i*2] = heap[i*2], heap[i]
        i = i*2
      else:
        heap[i], heap[i*2+1] = heap[i*2+1], heap[i]
        i = i*2+1
    else:
      if heap[i] > heap[i*2]:
        heap[i], heap[i*2] = heap[i*2], heap[i]
      break

  return item


N = int(stdin.readline()) # N(1 ≤ N ≤ 100,000)
heap = [ 0 ]
heapLen = 0
for _ in range(N): 
  x = int(stdin.readline())
  if x != 0:
    heapLen += 1
    min_Heap_Append(heap, x, heapLen)
  else:
    if heapLen < 1:
      print(0)
    else:
      item = min_Heap_Pop(heap, heapLen)
      heapLen -= 1
      print(item)



