# Write a function to find the shortest path from a source vertex to all other vertices in a graph using Dijkstra's algorithm. Sample Test Case
# Input: graph = {0: {1: 4, 2: 1}, 1: {3: 1}, 2: {1: 2, 3: 5}, 3: {}}, source = 0 Output: {0: 0, 1: 3, 2: 1, 3: 4}

import heapq

def dijkstra(graph, source):
    dist = {vertex: float('inf') for vertex in graph}
    dist[source] = 0
    priority_queue = [(0, source)]
    
    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)
        
        if current_dist > dist[u]:
            continue
        
        for neighbor, weight in graph[u].items():
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return dist

graph = {0: {1: 4, 2: 1}, 1: {3: 1}, 2: {1: 2, 3: 5}, 3: {}}
source = 0
print(dijkstra(graph, source)) 