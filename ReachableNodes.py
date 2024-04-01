def reachable(adj_list, start_node):
    #initialize a set to keep track of the visited nodes
    visited = set()
    #initialize a stack to keep track of the nodes to visit
    stack = [start_node]

    #continue visiting nodes until the stack is empty:
    while stack:
        #get the next node to visit
        node = stack.pop()
        #check if the node has been visited; if not, visit it
        if node not in visited:
            visited.add(node)
            #add all unvisited neighbors of the node to the stack
            stack.extend(n for n in adj_list[node] if n not in visited)

    return visited
