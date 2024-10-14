#implementing depth-first search algorithm
#frontier based on stack(LIFO)
#we expand the deepest nodes first.

def solution(precedessors, finishnode, startnode):
    path=[finishnode]
    node=finishnode
    while node is not  startnode:
       path.insert(0,precedessors[node])
       node=precedessors[node]
    return path 

def dfs(startnode,finishnode,graph):
    frontier=[startnode] #frontier holds the nodes that aren't expanded yet.
    predecessors={}
    explored=set()
    while frontier:
        node = frontier.pop()
        if node  == finishnode :
            path = solution(predecessors, finishnode, startnode )
            print(" -> ".join(path))
            return
        else: 
            for child in graph[node]:
                if child not in (set(explored) | set(frontier) ):
                    frontier.insert(0,child)
                    predecessors[child]= node
                explored.add(node)
    print(f"No Path From {startnode} To {finishnode} Exists.")




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

    dfs(startnode,finishnode,graph)

if __name__=="__main__":
    main()
