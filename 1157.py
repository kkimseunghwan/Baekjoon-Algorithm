word = input().upper()
wordArr = []
wordCount = []

for i in word:
  wordArr.append(i) 

max = 0
maxStr = "?"
for i in set(word):
  if max < wordArr.count(i):
    max = wordArr.count(i)
    maxStr = i
  elif max == wordArr.count(i):
    maxStr = "?"
  
print(maxStr)

