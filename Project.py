from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = defaultdict(bool)
        queue = deque([start])
        visited[start] = True

        while queue:
            vertex = queue.popleft()
            print(vertex)

            for neighbor in self.graph[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

    def dfs_util(self, vertex, visited):
        visited[vertex] = True
        print(vertex)

        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = defaultdict(bool)
        self.dfs_util(start, visited)

# อ่านข้อมูลจากแฟ้มข้อมูล province.txt
def read_province_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

# อ่านข้อมูลจากแฟ้มข้อมูล AdjacencyMatrix.txt
def read_adjacency_matrix(filename):
    adjacency_matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split(',')))
            adjacency_matrix.append(row)
    return adjacency_matrix

def main():
    provinces = read_province_file('province.txt')
    adjacency_matrix = read_adjacency_matrix('AdjacencyMatrix.txt')

    g = Graph()

    # เพิ่มเส้นเชื่อมตามข้อมูลจาก Adjacency Matrix
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] != 0:
                g.add_edge(provinces[i], provinces[j])

    print("กรุณาเลือกจังหวัดเริ่มต้น:")
    for i, province in enumerate(provinces):
        print(f"{i + 1}. {province}")

    choice = int(input("เลือกหมายเลข: ")) - 1

    print("\nการท่องเข้าในกราฟด้วยวิธี BFS:")
    g.bfs(provinces[choice])

    print("\nการท่องเข้าในกราฟด้วยวิธี DFS:")
    g.dfs(provinces[choice])

    # รอผู้ใช้ป้อนค่าก่อนที่โปรแกรมจะปิด
    input("กด Enter เพื่อปิดโปรแกรม")

if __name__ == "__main__":
    main()
