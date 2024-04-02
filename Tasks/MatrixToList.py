def mat_to_list(adj_mat) :
     # Initialize the adjacency list as an empty list with n empty lists
    adj_list = [[] for _ in range(len(adj_mat))]

    # Iterate over each row (i) in the adjacency matrix
    for i, row in enumerate(adj_mat):
        # Iterate over each column (j) in the adjacency matrix
        for j, col in enumerate(row):
            # If there is an edge between nodes i and j
            if col == 1:
                # Add node j to the list of neighbors of node i
                adj_list[i].append(j)

    return adj_list
