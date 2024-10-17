from sys import stdin
S = stdin.readline()
ROT13 = ""
for i in S:
	if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
		if ord(i) < 91 and ord(i) + 13  > 90 or ord(i) + 13  > 122:
			ROT13 += chr(ord(i)  - 13)
		else:
			ROT13 += chr(ord(i)  + 13)		
	else:
		ROT13 += i

print(ROT13)

