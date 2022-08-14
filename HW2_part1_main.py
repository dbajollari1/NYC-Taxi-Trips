import pandas as pd
from adj_list_graph import Adj_List_Graph
from ucs_alg import UCS_Alg
from a_star_search_alg import AStart_Search_Alg
import numpy as np
import csv
import datetime
from timeit import default_timer as timer


def turnToGraph(dataTable):
    #drop all columns we don't need 
    dataTable.drop(dataTable.columns[0], axis=1, inplace=True)
    dataTable.drop(['tpep_pickup_datetime','tpep_dropoff_datetime','pickup_hrs','dropoff_hrs','day_week','tpep_pickup_timestamp','tpep_dropoff_timestamp','duration','speed'], axis=1, inplace=True)
    #dataTable = dataTable.head(10000) #for testing purposes don't use whole dataset
    dataTable = dataTable.round(4)  # round to 4 decimals
    dataTable  = dataTable.drop_duplicates()
    row_count = dataTable.shape[0]

    # Iterate thru data to create a dictonary of unique node id's (1, 2, 3) along with latitude and longitude
    nodesDictionary = {} # KEY: Lat+Long -> VALUES: NodeId, Lat, Long
    i = 0
    for index, row in dataTable.iterrows():
        # pickup coordinates
        lat = dataTable.at[index,'pickup_latitude'] 
        long = dataTable.at[index,'pickup_longitude']
        key = str(lat) + str(long)
        if not key in nodesDictionary:
            i += 1 # New Node Id
            nodesDictionary[key] = [i, lat, long]
        # dropoff coordinates
        lat = dataTable.at[index,'dropoff_latitude'] 
        long = dataTable.at[index,'dropoff_longitude']
        key = str(lat) + str(long)
        if not key in nodesDictionary:
            i += 1 # New Node Id
            nodesDictionary[key] = [i, lat, long]

    graph = Adj_List_Graph()

    #create edges with weight (trip distance) and add to graph
    for index, row in dataTable.iterrows():
        pickupLat = dataTable.loc[index,'pickup_latitude']
        pickupLong = dataTable.loc[index,'pickup_longitude']
        dropoffLat = dataTable.loc[index,'dropoff_latitude']
        dropoffLong = dataTable.loc[index,'dropoff_longitude']
        pickupNodeId = getNodeId(nodesDictionary, pickupLat, pickupLong)
        dropoffNodeId = getNodeId(nodesDictionary, dropoffLat, dropoffLong)
        trip_distance = dataTable.loc[index,'trip_distance']
        graph.add_edge(int(pickupNodeId), int(dropoffNodeId), trip_distance)
    
    return graph, nodesDictionary

# get unique node id by passing lat and long values
def getNodeId(nodesDictionary, lat, long):
    try:
        #return nodes.loc[(nodes['lat'] == lat) & (nodes['long'] == long)]['nodeid'].values[0]
        return nodesDictionary[str(lat) + str(long)][0]
    except:
        return 'error!!!'

def main():
    print('Loading data (adjacency list graph)...')
    dataTable = pd.read_csv('nyc_taxi_data.csv')
    graph, nodesDictionary = turnToGraph(dataTable)
    print('**** DATA LOADED ****')


    nodesList = []
    nodeIdDict = {} # KEY: NodeId -> VALUES: Lat, Long
    for key in nodesDictionary:
        nodesList.append({'nodeid': nodesDictionary[key][0], 'lat': nodesDictionary[key][1], 'long': nodesDictionary[key][2] })
        nodeIdDict[nodesDictionary[key][0]] = [nodesDictionary[key][1], nodesDictionary[key][2]]
    nodesDF = pd.DataFrame.from_dict(nodesList)
    nodesDF.to_csv('nodes.csv', index = False)
    print('**** GENERATED nodes.csv ****')

    edgesList = []
    for nodePikup in graph.adj_list:
        for nodeDropoff in graph.adj_list[nodePikup]:
            edgesList.append({'p': nodePikup, 'd': nodeDropoff[0] })
    edgesDF = pd.DataFrame.from_dict(edgesList)
    edgesDF.to_csv('edges.csv', index = False)
    print('**** GENERATED edges.csv ****')

    # Path calcualation using UCS
    nodeCount = len(graph.adj_list)
    fromNode = input('Enter origin node - a number between 1 and ' + str(nodeCount) + ": ")
    toNode = input('Enter destination node - a number between 1 and ' + str(nodeCount) + ": ")
    
    ucsAlg = UCS_Alg(graph)
    print('\nCalculating path using UCS ... ')
    start1 = timer()
    ucsAlg.get_path(int(fromNode), int(toNode))
    end1 = timer()
    printTime1 = "Time taken for finding path between " + fromNode + " and " + toNode + " using Uniform Cost Search: " + str(round(end1 - start1, 5)) + " seconds."
    print(printTime1)
    
    asearchAlg = AStart_Search_Alg(graph, nodeIdDict)
    print('\nCalculating path using A* Search ... ')
    start2 = timer()
    asearchAlg.get_path(int(fromNode), int(toNode))
    end2 = timer()
    printTime2 = "Time taken for finding path between " + fromNode + " and " + toNode + " using A* Search: " + str(round(end2 - start2, 5)) + " seconds."
    print(printTime2)

    # open README FILE for append
    readmeFile = open("README.MD", "a")  # append mode
    readmeFile.write("- " + printTime1 + "\n")
    readmeFile.write("- " + printTime2 + "\n")
    readmeFile.close()

if __name__ == "__main__":
    main()