"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")


    # Print each vertex in breadth-first order
    # beginning from starting_vertex.
    
    # Breadth First Traversal
    def bft(self, starting_vertex):  
        print('BFT')
        # store visited nodes
        visited = set()
        # create an empty queue and enqueue the starting vertex
        queue = Queue()
        queue.enqueue(starting_vertex)
        # while queue is not empty
        while queue.size() > 0:
            # dequeue and store the first vertex
            vertex = queue.dequeue()
            # if that vertex hasn't been visited
            if vertex not in visited:
                # mark it as visited
                visited.add(vertex)
                # print vertex
                print(vertex)
                # add all of it's neighbors to the back of the queue
                for neighbor in self.vertices[vertex]:
                    queue.enqueue(neighbor)





    # Print each vertex in depth-first order
    # beginning from starting_vertex.

    # Depth First Traversal
    def dft(self, starting_vertex): 
        print("Start DFT")
        # create an empty set to store visited nodes
        visited = set()
        # create an empty stack and push the starting vertex on the stack
        stack = Stack()
        stack.push(starting_vertex)
        # while the stack is not empty
        while stack.size() > 0:
            # pop the first vertex
            vertex = stack.pop()
            # if that vertex hasn't been visited
            if vertex not in visited:
                # mark it as visited (add to visited set)
                visited.add(vertex)
                # print vertex
                print(vertex)
                # loop through edges
                for neighbor in self.vertices[vertex]:
                    # push edges to stack
                    stack.push(neighbor)




    def dft_recursive(self, starting_vertex, visited=None):
        if visited is None:
            visited = set()
        # if starting_vertex is not in the visited set
        if starting_vertex not in visited:
            # mark node as visited
            visited.add(starting_vertex)
            # print starting vertex
            print(starting_vertex)
            # call recursive for each child and send visited list
            for neighbor in self.vertices[starting_vertex]:
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        # Return a list containing the shortest path from
        # starting_vertex to destination_vertex in breadth-first order.

        # Create an empty set to store visited nodes
        visited = set()
        # Create an empty Queue and enqueue A PATH TO the starting vertex
        queue = Queue()
        queue.enqueue([starting_vertex])
        # While the queue is not empty...
        while queue.size() > 0:
            # Dequeue the first PATH
            path = queue.dequeue()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            vertex = path[-1]
            # IF VERTEX = TARGET, RETURN PATH
            if vertex == destination_vertex:
                return path
            # If that vertex has not been visited...
            if vertex not in visited:
                # Mark it as visited
                visited.add(vertex)
                # Then add A PATH TO all of its neighbors to the back of the queue
                for neighbor in self.vertices[vertex]:
                    # Copy the path
                    path_copy = list(path)
                    # Append neighbor to the back of the copy
                    path_copy.append(neighbor)
                    # Enqueue copy
                    queue.enqueue(path_copy)



    def dfs(self, starting_vertex, destination_vertex):
        # Return a list containing a path from
        # starting_vertex to destination_vertex in
        # depth-first order.

        visited = set()
        stack = Stack()
        stack.push([starting_vertex])
        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]
            if vertex == destination_vertex:
                return path
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.vertices[vertex]:
                    path_copy = list(path)
                    path_copy.append(neighbor)
                    stack.push(path_copy)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("start recursive DFT")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
