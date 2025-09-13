# Графыг хөрш жагсаалтаар дүрсэлж байна
graph = {
    "A": ["B", "C"],
    "B": ["A"],
    "C": ["A"]
}

# Бүх орой ба түүний хөршүүдийг хэвлэх
for node in graph:
    print(f"{node} -> {graph[node]}")

# Adjacency list to adjacency matrix  
#Give an adjacency-list representation for a complete binary tree on 7 vertices. Give an equivalent adjacency-matrix representation. Assume that vertices are numbered from 1 to 7 as in a binary heap.
def adjlist_to_matrix(adj_list, n):
    # n = number of vertices
    matrix = [[0] * n for _ in range(n)]
    
    for u in adj_list:
        for v in adj_list[u]:
            matrix[u-1][v-1] = 1  # u, v дугааруудыг 0-based болгоод тэмдэглэнэ
    return matrix


# Жишээ: 7 оройтой бүрэн хоёртын мод
adj_list = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2],
    5: [2],
    6: [3],
    7: [3]
}

matrix = adjlist_to_matrix(adj_list, 7)

# Хэвлэх
# for row in matrix:
#     print(row)

# The transpose of a directed graph GD.V; E/ is the graph GT D.V; ET/, where ET Df.; u/ 2V V W.u; / 2Eg. Thus, GT is G with all its edges reversed. Describe efficient algorithms for computing GT from G, for both the adjacency- list and adjacency matrix representations of G. Analyze the running times of your algorithms.
def adjlist_to_transpose(adj_list):
    transpose = {u:[] for u in adj_list}
    for u in adj_list:
        for v in adj_list[u]:
            transpose[v].append(u)
            return transpose

print("Adjacency list")
print(adjlist_to_transpose(adj_list))