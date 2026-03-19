# Artificial-Intelligence-Assignment---3
These are the codes and the description for the AI Assignment - 3

1.
In search problems where different actions carry varying costs, the most effective approach is a best-first search that evaluates the total path cost from the starting point to the current location. Computer scientists know this as Dijkstra’s Algorithm, while the AI field refers to it as Uniform-Cost Search. Your objective is to apply this concept to a network of Indian cities, using publicly available road distance data to navigate the network.

How the Code Works

Overview:
The program implements Dijkstra’s Algorithm to determine the shortest travel routes between cities. It maps this out mathematically by treating each city as a node and the road distances between them as edge weights.

Input:
It requires a designated starting city and a graph representing the map. This graph is structured as a dictionary containing the cities and the exact distances connecting them.

Process:
The algorithm systematically calculates the shortest possible route from the origin city to every other city in the network. It relies on a priority queue data structure to efficiently prioritize and explore the next closest, unvisited city.

Output:
The program provides the final, minimum travel distances from the starting city to all other reachable cities on the map.

Output Screenshot

<img width="1100" height="909" alt="image" src="https://github.com/user-attachments/assets/79d94d80-fc6b-41f8-9006-4a58bad42f9c" />


2.
An Unmanned Ground Vehicle (UGV) is a robot that finds the optimal path from a given user-specified start node to a user-specified Goal node on a map of a small area in a battlefield (Eg 70x70 Kms). There are obstacles known a-priori. The density of the obstacles can be generated randomly with three different levels of density. Design an algorithm that makes the UGV to navigate through this grid space avoiding all the known obstacles to reach the goal by the shortest distance. Trace this path along with the Measures of Effectiveness.

what the code does: -It simulates a UGV moving in a grid using the A* algorithm. It avoids obstacles and finds the shortest path from start to goal.

Input: -Grid (2D list) -Start position -Goal position -Obstacles (1 = blocked,0 = Unblocked)

Process: -Finds shortest path using A* Algorithm -Uses Manhattan distance as heuristic

Output -Path (as a list of coordinates)

<img width="1109" height="855" alt="image" src="https://github.com/user-attachments/assets/3b4f0b23-b0e1-4675-b2cf-e5851c49dbf4" />

3.
In the above problem, we relax the condition that all obstacles are Static. In a real world, obstacles can be dynamic and not known a priori. How do you make the UGV navigate and find the optinal path in a dynamic obstacles environment.

what the code does:

extends the UGV problem to handle dynamic obstacles. The robot replans its path at every step when new obstacles appear
Input: -Grid (2D list) -Start position -Goal position -Obstacles (1 = blocked,0 = Unblocked)

Process: -Moves step-by-step -Runs A* again if environment changes -Adds random obstacles

Output: -Final path taken (may differ from optimal solution)

<img width="1113" height="901" alt="image" src="https://github.com/user-attachments/assets/94b73581-5ce6-456d-991d-b36dd7b092ae" />










