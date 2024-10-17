#implementing Uniform-Cost Search
#choosing the lowest path cost at any state with regards to the nodes that are not exapanded yet even if they are at a lower level.
#if in bfs and dfs we just needed a frontier then in here aside from that we also need to save the path costs.
#using a dictionary to associate the edge(key) to the cost(value).
#the frontier operates with the same logic as bfs meaning it uses queue(FIFO).
#so it's kind of an upgraded(?) version of bfs. that works for weighted graphs.


def ucs(graph, startnode, finishnode, path_cost):
    total_cost={startnode: 0}
    frontier=[startnode]
    current_path=startnode
    explored=[] #precedessor is for keeping track of the predecessors of each node for finding the path.
    #predecessor={}
    node= frontier[0]
    while frontier: 
        frontier.pop(0)
        #explored.append(node)
        if node==finishnode:
            #path = solution(predecessor, finishnode, startnode)
            print("the final cost using ucs algorithm is: "+ str(total_cost[current_path]))
            print(" -> ".join(current_path))
            return
        else: 
            explored.append(node)
            children=set(graph[node])-(set(frontier) | set(explored))
            for child in children:
                total_cost[str(current_path)+child]=total_cost[current_path]+path_cost[node+child]
            del total_cost[current_path]
            current_path= min(total_cost, key=lambda path: total_cost[path])
            frontier.extend(children)
            node=current_path[-1]
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

    path_cost = {
    "AB": 12,  
    "AC": 5,   
    "BD": 8,   
    "BE": 7,   
    "CA": 5,    
    "DB": 8,    
    "DE": 3,   
    "EB": 7,    
    "ED": 3    
}
    
    ucs(graph,startnode,finishnode,path_cost)

if __name__=="__main__":
    main()