import heapq


# Define a class Node to create a graph
class Node:

	def __init__(self, name, adjacencies=None):
		adjacencies = [] if adjacencies is None else adjacencies
		self.name = name
		self.adjacenciesList = adjacencies
		self.minDistance = float('inf')
		self.predecessor = None
		self.visited = False

	def __cmp__(self, otherVertex):
		return self.cmp(self.minDistance, otherVertex.minDistance)

	def __lt__(self, other):
		selfPriority = self.minDistance
		otherPriority = other.minDistance
		return selfPriority < otherPriority

	def __str__(self):
		return f"Graph Node. Value {self.name}. Adjacent: {list(map(lambda a: a.name, self.adjacenciesList))}. Min Distance: {self.minDistance}"


# Parse the input, remove duplicates, and subtract
# one to every pointer to match Python's list number starting at 0
pages = int(input())
temp_pages_reachable = [list(map(lambda a: a - 1, list(map(int, input().split())))) for _ in range(pages)]
pages_reachable = []
end_pages = []
visited = dict()

for page in range(len(temp_pages_reachable)):
	if temp_pages_reachable[page][0] == -1:
		end_pages.append(page)
	if -1 not in temp_pages_reachable[page]:
		pages_reachable.append(list((list(set(temp_pages_reachable[page][1:])))))
	else:
		pages_reachable.append([-1])
	visited[page] = []
del temp_pages_reachable
visited[-1] = []
reachable_pages = [0]


# Find all of the reachable pages in the book
def find_reachable_pages(current_page=0):
	global reachable_pages
	for reachable in pages_reachable[current_page]:
		if reachable in reachable_pages:
			continue
		reachable_pages.append(reachable)
		find_reachable_pages(current_page=reachable)


pages_nodes = []
for i in range(pages):
	pages_nodes.append(Node(i))
pages_nodes.append(Node(-1))


for i, pages_adj in enumerate(pages_reachable):
	nodes_adj = []
	for page in pages_adj:
		nodes_adj.append(pages_nodes[page])
	pages_nodes[i].adjacenciesList = nodes_adj


# Find the shortest path from the first page
# to an ending page using Dijkstra's algorithm
def dijkstra(startVertex):

	q = []

	startVertex.minDistance = 0
	heapq.heappush(q, startVertex)

	while q:

		vertex = heapq.heappop(q)

		for endNode in vertex.adjacenciesList:
			newDistance = vertex.minDistance + 1

			if newDistance < endNode.minDistance:
				endNode.predecessor = vertex
				endNode.minDistance = newDistance
				heapq.heappush(q, endNode)


dijkstra(pages_nodes[0])

find_reachable_pages()
reachable_pages.remove(-1)
if len(reachable_pages) >= pages:
	print("Y")
else:
	print("N")

print(reachable_pages)

shortest_path = float('inf')

for i, node_ in enumerate(pages_nodes):
	if node_.name == -1:
		shortest_path = min(shortest_path, node_.minDistance)

		# Uncomment the below code to show the shortest path tree
		# curr_tree = node_
		# print("Shortest Path Tree: ")
		# while True:
		# 	print(curr_tree)
		# 	if curr_tree.name == 0:
		# 		break
		# 	curr_tree = curr_tree.predecessor

print(shortest_path)



