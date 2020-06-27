import operator
def mostViewedWriters(topicIds, answerIds, views):
	topics = []
	for l in topicIds:
		for t in l:
			if t not in topics:
				topics.append(t)

	topics.sort()

	fl = []
	for t in topics:
		ai = []
		an = 0
		for l in topicIds:
			if t in l:
				ai.append(an)
			an += 1

		ans_t = []
		for i in ai:
			for e in answerIds[i]:
				if e not in ans_t:
					ans_t.append(e)
		
		v_t = {}
		for a in ans_t:
			for l in views:
				if a == l[0]:
					if l[1] not in v_t:
						v_t[l[1]] = l[2]
					else:
						v_t[l[1]] += l[2]

		lvt = []
		for v in v_t:
			lvt.append([v, v_t[v]])

		fl.append(sorted(sorted(lvt, key=operator.itemgetter(0), reverse=False), key=operator.itemgetter(1), reverse=True))

	return fl


topicIds = [[1, 2, 3], [2, 3, 4], [1, 4], [2, 3]]
answerIds = [[6, 4], [1, 2], [5], [3]]
views = [[2, 1, 2], [6, 3, 5], [3, 3, 0], [5, 1, 1], [4, 2, 3], [1, 4, 2]]
output = [
	[[3, 5], [2, 3], [1, 1]],
	[[3, 5], [2, 3], [1, 2], [4, 2]],
	[[3, 5], [2, 3], [1, 2], [4, 2]],
	[[1, 3], [4, 2]]
]

if mostViewedWriters(topicIds, answerIds, views) == output:
	print "OK"