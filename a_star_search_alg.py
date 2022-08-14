from queue import PriorityQueue
from geopy.distance import geodesic

class AStart_Search_Alg:

    #constructor
    def __init__(self, graph, nodesDict):
        self.adjacency_list = graph.adj_list 
        self.nodesDict = nodesDict
        self.H = {} # heuristic value for each node

    def __get_neighbors(self, v):
        if v in self.adjacency_list:
            return self.adjacency_list[v]
        else:
            return None

    def __getNodeLatLong(self, nodeId):
        try:
            return self.nodesDict[nodeId][0], self.nodesDict[nodeId][1] #return lat & long
        except:
            return 'error!!!'

    def __loadH(self, stopNode):
        stopNodeLatLong = self.__getNodeLatLong(stopNode)  # touple of latitude and long
        for key in self.nodesDict:
            startnodeLatLong = self.__getNodeLatLong(key)
            self.H[key] = self.__heuristic(startnodeLatLong, stopNodeLatLong)

    # heuristic function 
    def __heuristic(self, startNode, stopNode):
        return geodesic(startNode, stopNode).miles

    # function to calculate the cost of path beteween two nodes
    def __find_cost(self, node_A, node_B):
        location = [n[0] for n in self.adjacency_list[node_A]].index(node_B)
        return self.adjacency_list[node_A][location][1]

    def get_path(self, start_node, stop_node):

        self.__loadH(stop_node) # Load heuristic values to a dictonary (by nodeId)

        open_set = set([start_node]) 
        closed_set = set([])
        g = {} #store distance from starting node
        parents = {}# parents contains an adjacency map of all nodes
 
        g[start_node] = 0
        parents[start_node] = start_node #start_node is root node
        total_distance = 0 
         
        while len(open_set) > 0:
            n = None

            #node with lowest f() is found
            for v in open_set:
                if n == None or g[v] + self.H[v] < g[n] + self.H[n]:
                #if n == None or g[v] < g[n]:
                    n = v
                     
            if n == stop_node or self.adjacency_list[n] == None:
                pass
            else:
                for (m, weight) in self.__get_neighbors(n):
                    #nodes 'm' not in first and last set are added to first
                    #n is set its parent
                    if m not in open_set and m not in closed_set:
                        open_set.add(m)
                        parents[m] = n
                        g[m] = g[n] + weight
                         
                    #for each node m,compare its distance from start
                    else:
                        if g[m] > g[n] + weight:
                            #update g(m)
                            g[m] = g[n] + weight
                            #change parent of m to n
                            parents[m] = n
                             
                            #if m in closed set,remove and add to open
                            if m in closed_set:
                                closed_set.remove(m)
                                open_set.add(m)
 
            if n == None:
                print('Path does not exist!')
                return None
 
            # if the current node is the stop_node then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                path = []
 
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
 
                path.append(start_node)
 
                path.reverse()
 
                pathOutput = ''
                fromNode = start_node
                for node in path:
                    if pathOutput == '':
                        pathOutput = str(node)
                    else:
                        pathOutput = pathOutput + '-->' + str(node)
                    if fromNode != node:
                        total_distance = total_distance + self.__find_cost(fromNode, node)
                    fromNode = node

                print('\n**** Total Distance: '+ str(round(total_distance,2)))
                print( '**** Route: ' + pathOutput)
                return path
 
            # remove n from the open_list, and add it to closed_list because all of his neighbors were inspected
            open_set.remove(n)
            closed_set.add(n)
 
        print('\n***Path does not exist!')
        return None