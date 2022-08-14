class Adj_List_Graph:
    #constructor
    def __init__(self):
        self.adj_list = {}    #emtpy dictionary 
           
    #add an edge
    def add_edge(self, node1, node2, distance, directed = False):
        temp = []
        if node1 not in self.adj_list:
            temp.append([node2, distance])
            self.adj_list[node1] = temp
        elif node1 in self.adj_list:
            temp.extend(self.adj_list[node1])
            temp.append([node2, distance])
            self.adj_list[node1] = temp

        if directed == False: # add other direction
            temp1 = []
            if node2 not in self.adj_list:
                temp1.append([node1, distance])
                self.adj_list[node2] = temp1
            elif node2 in self.adj_list:
                temp1.extend(self.adj_list[node2])
                temp1.append([node1, distance])
                self.adj_list[node2] = temp1           

    # print graph
    def print_graph1(self):
        for key in self.adj_list.keys():
            print(key, " ---> ", self.adj_list[key])

    def print_graph(self, multiplePoints = False):
        if multiplePoints:
            for node in self.adj_list:
                if len(self.adj_list[node]) > 1:
                    print(node, " ---> ", [i for i in self.adj_list[node]])
        else:            
            for node in self.adj_list:
                # print(self.adj_list[3])
                print(node, " ---> ", [i for i in self.adj_list[node]])

    def get_dist(self, nodeFrom, nodeTo):
        dist = 999
        for i in self.adj_list[nodeFrom]:
            if i[0] == nodeTo:
                dist = i[1]
                break
        return dist