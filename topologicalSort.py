import graph

gra = graph.Graph()

def topologicalOrder(v, visited, stack):

    #Mark the node visited 
    visited[v] = True    

    #Check if there is any unvisited node from the node to its neighbors
    for i in gra.graph[v]:
        if visited[i]==False:
            topologicalOrder(i, visited, stack)

    #Pushes the node to stack if it has no neighbor unvisited
    stack.append(v)

def main():

    no_of_nodes = int(input("How many nodes are there: "))
    
    no_of_edges = int(input("How many edges are there: "))
    print("Enter the edges in u v style, where edge is from the node u to v in case of directed")

    #To add the edges in the Graph
    for i in range(no_of_edges):
        u, v = input().split()
        u = int(u)
        v = int(v)
        gra.addEdge(u, v)

    #maintains which node is visited
    visited = [False]*no_of_nodes

    #maintain the topological order
    stack=[]

    #To iterate over every node in the Graph
    for i in range(no_of_nodes):
        if visited[i]==False:
            topologicalOrder(i, visited, stack)

    #printing the Topological number
    print("Topological Sorted :", end="")
    for i in stack[::-1]:
        print(" -> ", i, end="")
    print("")
   

if __name__=="__main__":
    main()