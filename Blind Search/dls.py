#implementing depth-limited search algorithm
#frontier based on stack(LIFO)
#we expand the deepest nodes first.but in here we only go tilll we reach a depth limit, then we go 
#back and search the other branches. 
#uf the final state is beyond the depth limit, then we won't find an answer, so this search algorithm is incomplete.

def solution(precedessors, finishnode, startnode):
    path=[finishnode]
    node=finishnode
    while node is not  startnode:
       path.insert(0,precedessors[node])
       node=precedessors[node]
    return path 

def dls(graph,startnode,finishnode, depth_limit):
    current_depth=0
    predecessors={}
    explored=set()
    frontier=[(startnode,0)] #frontier holds the nodes that aren't expanded yet.
    if depth_limit >= 0:
        while frontier:
            node=frontier.pop()
            if node[1] >= depth_limit+1:
                return 'No Path Exists From '+startnode+' To '+finishnode+' At Depth Limit Of '+str(depth_limit)
            if node[0] is not finishnode:
                for child in graph[node[0]]:
                    if child not in (set(explored) | set(frontier) ):
                        frontier.insert(0,(child, node[1]+1))
                        predecessors[child]= node[0]
                    explored.add(node[0])
                dls(graph, node[0], finishnode, depth_limit-1)
            elif node[0] == finishnode:
                path = solution(predecessors, finishnode, startnode )
                return " -> ".join(path)

    return 'No Path Exists From '+ startnode +' To '+ finishnode
        

def main():
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "E"],
        "D": ["B", "F"],
        "E": ["C"],
        "F": ["D"]
    }

    startnode = "A"
    finishnode = "F"
    depth_limit = 3
    
    # Expected output: ['A', 'B', 'D', 'F']


    print(dls(graph, startnode, finishnode, depth_limit))

if __name__=="__main__":
    main()
