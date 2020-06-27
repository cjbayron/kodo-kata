def kikCode(userId):
	intId = int(userId)
	z = 0
	while (1 << z)*intId < 2**51 and intId > 0:
		z += 1

	code = int(bin(intId)[:1:-1], 2) << z
	bits = [3, 4, 8, 10, 12, 15]

	i = 1
	fl = []
	for b in bits:
		
		s = 0
		for t in bits[i:]:
			s += t

		bc = (code >> s) & ((1 << b) - 1)

		m = 1 << b
		l = []
		j = 0
		while m > 1:
			m >>= 1
			if m & bc:
				if not l:
					l.append([j, j])
				else:
					if l[-1][1] == j - 1:
						l[-1][1] = j
					else:
						l.append([j, j])

			j += 1

		if len(l) > 1:
			if l[0][0] == 0 and l[-1][1] == b - 1:
				l[0][0] = l[-1][0]
				l[0][1] += b
				l.pop()

		a = 360/b
		for c in l:
			fl.append([[i, c[0]*a], [i, (c[1] + 1)*a]])

		i += 1

	return fl  

output = [
  [[1, 0], [1, 120]],
  [[2, 270], [2, 540]],
  [[3, 45], [3, 135]], [[3, 180], [3, 225]], [[3, 270], [3, 360]],
  [[4, 0], [4, 72]], [[4, 108], [4, 180]], 
  [[4, 216], [4, 252]], [[4, 288], [4, 324]],
  [[5, 0], [5, 360]],
  [[6, 0], [6, 48]], [[6, 72], [6, 120]], [[6, 168], [6, 192]], 
  [[6, 240], [6, 264]], [[6, 288], [6, 336]]
]

if kikCode("1851027803204441") == output:
	print "OK"

print kikCode("1")
print kikCode(str(2**52 - 1))

print kikCode(str(int("1111110111111111111110111111111011111110111111111111", 2)))