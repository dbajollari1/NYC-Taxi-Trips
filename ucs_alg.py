from queue import PriorityQueue

class UCS_Alg:

    #constructor
    def __init__(self, graph):
        self.graph = graph 

    def get_path(self, origin, destination):
        visited = set()
        path = []
        queue = PriorityQueue()
        queue.put((0, [origin]))

        while queue:
            # if no path is present beteween two nodes  
            if queue.empty():
                print('**** Path does not exist!\n')
                return
            cost, path = queue.get()
            node = path[len(path)-1]
            if node not in visited:
                visited.add(node)
                if node == destination:
                    path.append(cost)
                    #return path
                    break
                
                for n in self.__neighbors(node):
                    if n not in visited:
                        t_cost = cost + (self.__find_cost(node, n))
                        temp = path[:]
                        temp.append(n)
                        queue.put((t_cost, temp))
        
        self.__display_path(path)

    # function for finding neighbors in the graph
    def __neighbors(self, node):
        points = self.graph.adj_list[node]
        return [n[0] for n in points]

    # function to calculate the cost of path beteween two nodes
    def __find_cost(self, node_A, node_B):
        location = [n[0] for n in self.graph.adj_list[node_A]].index(node_B)
        return self.graph.adj_list[node_A][location][1]

    # output the result of search
    def __display_path(self, path):
        distance = path[-1]
        print('\n**** Total Distance: '+ str(round(distance,2)))
        route = '**** Route: ' + str(path[0])
        for p in path[:-2]:
            q = path.index(p)
            location = [r[0] for r in self.graph.adj_list[p]].index(path[q+1])
            cost = self.graph.adj_list[p][location][1]
            # route = route + '-->' + (str(p) + ' to ' + str(path[q+1])  + ', ' + str(cost))
            route = route + '-->' + str(path[q+1]) 
        print(route)