stack = {}
exts = {}

def expected(i, t, edges, lvl):
	if lvl not in stack:
		r = []
		edges_cp = edges[:]
		for l in edges:
			if i in l:
				tmp = l[:]
				tmp.remove(i)
				r.append(tmp[0])
				edges_cp.remove(l)

		ex_t = 0.0

		stack[lvl] = {}
		stack[lvl]['edges_cp'] = edges_cp
		stack[lvl]['ex_t'] = ex_t
		stack[lvl]['x'] = 0
		stack[lvl]['r'] = r
		stack[lvl]['i'] = -1
		stack[lvl]['node'] = i

		if len(r) > 0:
			stack[lvl]['i'] = r[0]
		
	if len(stack[lvl]['r']) > 0:
		if stack[lvl]['x'] < len(stack[lvl]['r']):
			if str(i) + "," + str(stack[lvl]['i']) not in exts:
				return lvl + 1
			else:
				stack[lvl]['x'] += 1
				stack[lvl]['ex_t'] += exts[str(i) + "," + str(stack[lvl]['i'])]
				if stack[lvl]['x'] < len(stack[lvl]['r']):
					stack[lvl]['i'] = stack[lvl]['r'][stack[lvl]['x']]
					
				return lvl
		else:
			stack[lvl]['ex_t'] /= len(stack[lvl]['r'])

	stack[lvl]['ex_t'] += t[i]
	if lvl > 0:
		stack[lvl - 1]['x'] += 1
		if stack[lvl - 1]['x'] < len(stack[lvl - 1]['r']):
			stack[lvl - 1]['i'] = stack[lvl - 1]['r'][stack[lvl - 1]['x']]

		stack[lvl - 1]['ex_t'] += stack[lvl]['ex_t']
		exts[str(stack[lvl - 1]['node']) + "," + str(i)] = stack[lvl]['ex_t']
		stack.pop(lvl, None)

		return lvl - 1

	return lvl - 1

def relatedQuestions(n, t, edges):
	i = 0
	times = []
	while i < n:

		lvl = expected(i, t, edges, 0)
		while lvl != -1:
			if lvl > 0:
				lvl = expected(stack[lvl - 1]['i'], t, stack[lvl - 1]['edges_cp'], lvl)
			else:
				lvl = expected(i, t, stack[lvl]['edges_cp'], 0)

		times.append(stack[0]['ex_t'])
		stack.pop(0, None)
		i += 1
	
	#print times
	return times.index(min(times))


n = 5
t = [2, 2, 1, 2, 2]
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

n = 1000
t = [2]*n
t[n/2] = 1
edges = []

i = 0
while i < n - 1:
	edges.append([i, i+1])
	i += 1

#print t
#print edges
#print len(t)
#print len(edges)


if relatedQuestions(n, t, edges) == n/2:
	print "OK"
	#print exts

n = 5
t = [2, 1, 13, 1, 12]
edges = [[3,0], 
 [3,2], 
 [4,1], 
 [3,1]]

if relatedQuestions(n, t, edges) == 3:
	print "OK"