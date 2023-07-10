import fileinput

# Python program to find
# maximal Bipartite matching.

class GFG:
	def __init__(self,graph):
		
		# residual graph
		self.graph = graph
		self.ppl = len(graph)
		self.jobs = len(graph[0])

	def bpm(self, u, matchR, seen):
		for v in range(self.jobs):
			if self.graph[u][v] and seen[v] == False:
				seen[v] = True
				if matchR[v] == -1 or self.bpm(matchR[v],
											matchR, seen):
					matchR[v] = u
					return True
		return False

	def maxBPM(self):
		matchR = [-1] * self.jobs
		result = 0
		for i in range(self.ppl):
			seen = [False] * self.jobs
			if self.bpm(i, matchR, seen):
				result += 1
		return result

if __name__ == "__main__":
    choices = 0
    for line in fileinput.input():
        line = list(map(int, line.split(" ")))
        choices = line[1]
        stdnt_cnt = line[0]
        fileinput.close()
        break
    
    persons = set()
    preference = []

    for line in fileinput.input():
        line = list(map(int, line.split(" ")))
        persons.add(line[0])
        preference.append(line)
    
    dp = [[0 for j in range(choices)] for i in range(stdnt_cnt)]
    for line in preference:
        dp[line[0] - 1][line[1] - 1] = 1


    solution = GFG(dp)
    
    print (solution.maxBPM())

