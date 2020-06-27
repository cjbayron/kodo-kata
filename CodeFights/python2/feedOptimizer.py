import math

class Queue(object):

	def __init__(self, max_size, h):
		self.max_size = max_size
		self.span = max_size - 1
		self.size = 0
		self.q = []
		self.max_score = 0
		self.max_ids = []
		self.cur_space = h
		self.h = h

	def addHead(self, head):
		if self.size < self.max_size:
			self.q.insert(0, head)
			self.size += 1

			if self.cur_space >= head[3]:
				self.max_ids.append(head[0])
				self.max_ids.sort()
				self.max_score += head[2]
				self.cur_space -= head[3]

			elif head[2] >= self.max_score and len(self.max_ids) > 1:
				self.max_ids = [head[0]]
				self.max_score = head[2]
				self.cur_space = self.h - head[3]

			else:
				max_score = self.max_score
				max_ids = self.max_ids
				
				i = 1
				q_copy = self.q[1:]
				while i < (1 << self.size - 1):
					sh = 0
					score = head[2]
					space = self.h - head[3]
					ids = [head[0]]


					for e in reversed(q_copy):
						if (i >> sh) % 2 and space >= e[3]:
							score += e[2]
							space -= e[3]
							ids.append(e[0])

							if space == 0:
								break

						sh += 1

					if score > max_score or (score == max_score and len(ids) < len(max_ids)):
						max_score = score
						max_ids = ids
						self.cur_space = space

					i += 1

				max_ids.sort()
				self.max_score = max_score
				self.max_ids = max_ids[:]

			#print 'add, ',
			#print self.max_score,
			#print ': ',
			#print self.max_ids

	def removeTail(self):
		if self.size > 0:
			r = self.q.pop()
			self.size -= 1

			if r[0] in self.max_ids:
				#print self.q
				self.max_ids.remove(r[0])
				self.max_ids.sort()
				self.max_score -= r[2]
				self.cur_space += r[3]

				max_score = self.max_score
				max_ids = self.max_ids
				
				i = 1
				while i < (1 << self.size):
					sh = 0
					score = 0
					space = self.h
					ids = []

					for e in reversed(self.q):
						if (i >> sh) % 2 and space >= e[3]:
							score += e[2]
							space -= e[3]
							ids.append(e[0])

							if space == 0:
								break

						sh += 1

					if score > max_score or (score == max_score and len(ids) < len(max_ids)):
						max_score = score
						max_ids = ids
						self.cur_space = space

					i += 1

				max_ids.sort()
				self.max_score = max_score
				self.max_ids = max_ids[:]

				#print 'remove, ',
				#print self.max_score,
				#print ': ',
				#print self.max_ids

	def update(self, time):
		for e in reversed(self.q):
			if e[1] < time - self.span:
				self.removeTail()
			else:
				break

	def getMax(self, h):
		max_ids = self.max_ids[:]

		max_ids.insert(0, self.max_score)
		return max_ids

def feedOptimizer(span, h, events):
	eventQueue = Queue(span + 1, h)
	# [id, time, score, pixel]
	cur_id = 1
	feed_list = []

	for e in events:
		t = e[0]
		eventQueue.update(t)

		if len(e) == 1:
			feed_list.append(eventQueue.getMax(h))
		else:
			if e[2] <= h:
				eventQueue.addHead([cur_id] + e)
			cur_id += 1

	#print feed_list
	return feed_list


# test data 1
span = 10
h = 100
events = [[11, 50, 30], 
          [12],
          [13, 40, 20],
          [14, 45, 40],
          [15],
          [16],
          [18, 45, 20],
          [21],
          [22]]

output = [[50, 1],
          [135, 1, 2, 3],
          [135, 1, 2, 3],
          [140, 1, 3, 4],
          [130, 2, 3, 4]]

if feedOptimizer(span, h, events) == output:
	print "OK"

span = 10
h = 50
events = [[1,50,25], 
 [3,100,50], 
 [4,50,25], 
 [5], 
 [6,200,50], 
 [7,100,25], 
 [8,100,25], 
 [9], 
 [10,101,25], 
 [11,101,25], 
 [12], 
 [101,10,10], 
 [102,25,25], 
 [103,25,25], 
 [104,15,15], 
 [105,25,25], 
 [106], 
 [201,20,10], 
 [202,20,15], 
 [203,40,25], 
 [204,40,25], 
 [205,40,25], 
 [206], 
 [301,1,15], 
 [302], 
 [303,1,15], 
 [304], 
 [305,1,15], 
 [306], 
 [307,1,15], 
 [308], 
 [309,1,15], 
 [310], 
 [311,1,15], 
 [312], 
 [313,1,15], 
 [314]]

output = [[100,2], 
 [200,4], 
 [202,7,8], 
 [50,10,11], 
 [80,16,17], 
 [1,19], 
 [2,19,20], 
 [3,19,20,21], 
 [3,19,20,21], 
 [3,19,20,21], 
 [3,20,21,22], 
 [3,21,22,23]]

if feedOptimizer(span, h, events) == output:
	print "OK"

# test data 3
span =  100
h = 100
events = [[12,44,405], 
 [13,39,614], 
 [20,5,841], 
 [23,89,129], 
 [28,18,918], 
 [30,44,325], 
 [32,91,184], 
 [35,26,773], 
 [43,6,591], 
 [44,87,955], 
 [59,43,83], 
 [60,8,198], 
 [61,49,805], 
 [68,29,623], 
 [70,47,344], 
 [85,23,341], 
 [88,6,811], 
 [92,31,662], 
 [95,21,306], 
 [98,27,445], 
 [118,9,466], 
 [122,59,283], 
 [124,63,638], 
 [125,37,601], 
 [136,80,900], 
 [144,72,469], 
 [150,82,132], 
 [168,95,934], 
 [171,100,164], 
 [173,97,900], 
 [179,14,774], 
 [194,96,191], 
 [199,85,467], 
 [212,85,91], 
 [220,37,543], 
 [227,57,446], 
 [228,88,419], 
 [229,73,349], 
 [230,37,10], 
 [236,88,343], 
 [238,14,302], 
 [246,56,322], 
 [271,22,600], 
 [276,12,940], 
 [277,6,668], 
 [281,51,128], 
 [282,21,659], 
 [287,70,423], 
 [302,31,82], 
 [306], 
 [307,73,973], 
 [314,86,626], 
 [316,41,300], 
 [318], 
 [325,99,714], 
 [328,91,525], 
 [336,20,582], 
 [337,56,733], 
 [341,80,5], 
 [351,77,274], 
 [354,61,256], 
 [363,85,580], 
 [365,22,206], 
 [366,14,505], 
 [368,27,755], 
 [369,3,945], 
 [371,85,507], 
 [374], 
 [379,29,869], 
 [380,9,873], 
 [384,37,499], 
 [387,49,754], 
 [394,34,334], 
 [396,55,891], 
 [400,69,747], 
 [404,47,501], 
 [408,50,798], 
 [414,34,304], 
 [422,54,498], 
 [427,26,687], 
 [429,76,997], 
 [430,30,158], 
 [433,15,461], 
 [435,5,461], 
 [438], 
 [445,3,557], 
 [452,100,698], 
 [457], 
 [482,1,404], 
 [489,39,648], 
 [492,36,152], 
 [493,93,340], 
 [498,5,128], 
 [501,65,50], 
 [504,44,430], 
 [506,1,178]]

output = [[85,34], 
 [68,39,49], 
 [111,49,57], 
 [80,57], 
 [0]]

if feedOptimizer(span, h, events) == output:
	print "OK"