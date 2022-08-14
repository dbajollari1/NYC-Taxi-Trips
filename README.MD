# Code Desriptions - 
    HW2 Part 1:
         - HW2_part1_main.py: Driver python file that takes nyc_taxi_trips.csv and turns into a graph using adjacency list 
           representation, and the inputs two nodes from user and returns best path using Uniform cost search and A* search
         - adj_list_graph.py: Class to implement adjacency list representation of graph
         - usc_alg.py: Class to perform Uniform Cost Search given graph and start/end nodes
         - a_star_search_alg.py: Class to perform A* search given graph and start/end nodes
    HW2 Part 2: 
        - beam_search.py: Takes a NMT model that is already trained on the French to English translation, and performs beam
          search on the data
        - HW2Part2.ipynb: The notebook I created using google colab

## Test data BLEU score without beam search implementation:
- 12.5

## BLEU Score plot on validation data: 
![Beam Search Grpaph](beam_search_graph.png?raw=true "Beam Search Graph")

## Test data BLEU score on the optimal beam size: 
 - 1.6

## Time taken to run UCS and A∗ searches

- Time taken for finding path between 23 and 135 using Uniform Cost Search: 1.12332 seconds.
- Time taken for finding path between 23 and 135 using A* Search: 40.31343 seconds.
