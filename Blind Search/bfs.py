#breadth-first algorithm
#based on queue(FIFO)
#expand all the child nodes of root and then going to the next level

#finding the path using predecessor
def solution(predecessor, finishnode, startnode):
    solution=[]
    solution.insert(0, finishnode)
    node = finishnode
    while node is not startnode:
        solution.insert(0,predecessor[node])
        node= predecessor[node]
    return solution

#checking if the path from starting node to finish node exits.
def bfs(startnode, finishnode, graph):

    frontier=[]
    explored=[]
    #precedessor is for keeping track of the predecessors of each node for finding the path.
    predecessor={}
    frontier.append(startnode)

    while frontier: 
        node= frontier[0]
        if node==finishnode:
            path= solution(predecessor, finishnode, startnode)
            print(" -> ".join(path))
            return
        else: 
            children=set(graph[node])-(set(frontier) | set(explored))
            for child in children:
                predecessor[child]=node
            frontier.extend(children)
            explored.append(node)
            frontier.pop(0)
    print("no solution")        




def main():
    graph= { 
        "A":["B","C"],
        "B":["A","D","E"],
        "C":["A"],
        "D":["B","E"],
        "E":["B","D"]
    }

    startnode= "A"
    finishnode= "E"

    bfs(startnode,finishnode,graph)

if __name__=="__main__":
    main()
