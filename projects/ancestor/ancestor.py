
testData = [[1,3],[2, 3],[3, 6],[5, 6],[5, 7],[4, 5],[4, 8],[8, 9],[11, 8],[10, 1]]

# answers = [[number, count], [number, count]]
answers = []
largest_count = 0

def findAncestor(arr, number, count=-1):
    # loop over arrays:
    base_case = True
    count += 1
    for i in range(len(testData)):
        # find number in place [1]
        if testData[i][1] == number:
            base_case = False
            findAncestor(arr, testData[i][0], count)
    if base_case == True:
        global answers
        global largest_count
        if count > largest_count:
            largest_count = count
        if count > 0:
            answers.append([number, count])

def earliest_ancestor(arr, number):
    global answers
    global largest_count
    answers = []
    largest_count = 0
    # call findAncestor (arr, number)
    findAncestor(arr, number)
    # loop over returned values
    final_answer = -1
    for i in range(len(answers)):
        if answers[i][1] == largest_count:
            if final_answer == -1 or final_answer > answers[i][0]:
                final_answer = answers[i][0]
    return final_answer

# print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 2))
# print(earliest_ancestor(testData, 9))
# print(earliest_ancestor(testData, 7))


# class Stack():
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack.append(value)
#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None
#     def size(self):
#         return len(self.stack)

# class earliest_ancestor(ancestors, starting_node):
#     def __init__(self):
#         self.starting_node = starting_node

#         self.vertices = {}
    
#     def add_vertext(self, vertex):
#         self.vertices[vertex] = {"parents": set(), "children": set()}
    
#     def add_edge(self, parent, child):
#         if parent in self.vertices and child in self.vertices:
#             self.vertices[parent].childen.add(child)
#             self.vertices[child].parents.add()

#         else:
#             raise IndexError("That vertex does not exitst!")

#     # def ancestor_search(self, starting_vertex):



