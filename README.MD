# NYC Taxi Trips
This python project performs Uniform Cost Search and A* Search on a dataset of Taxi Trips in NYC from January 2015 and finds the shortest path between two points that are input from the user. It also compares the two searching algorithms by timing how long they take to find the shortest path between two points. 

## How to run this project on your pc ? 
1. Create a project locally and clone this GitHub repository in it. 
2. Navigate to the folder and run the following command in your terminal to set up the virtual environment: py -3 -m venv .venv 
3. Next activate the python virtual environment using the following command: .venv\scripts\activate
4. After this you need to install the necessary packages, and that can be done by running the following command: pip install -r requirements.txt
5. Now update the requirement file to keep everything up to date: pip freeze > requirements.txt 
6. Finally you can run the project with the following command: python driver.py


## Code Desriptions - 
- driver.py: Driver python file that takes nyc_taxi_trips.csv and turns into a graph using adjacency list representation, and then find between two user inputted nodes using Uniform Cost Search and A* Search
- adj_list_graph.py: Class to implement adjacency list representation of a graph
- usc_alg.py: Class to perform Uniform Cost Search given graph and start/end nodes
- a_star_search_alg.py: Class to perform A* search given graph and start/end nodes.Uses the geographical distance(longitude and latitude coordinates) as the heuristic for the searching algorithm. 

## Time taken to run UCS and A∗ searches(updates everytime you run the project) -
- Time taken for finding path between 23  and 135 using Uniform Cost Search: 0.68382 seconds.
- Time taken for finding path between 23  and 135 using A* Search: 25.81375 seconds.
