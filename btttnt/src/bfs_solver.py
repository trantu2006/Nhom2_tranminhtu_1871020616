from collections import deque
from src.core_logic import get_start_goal, get_neighbors, print_maze_with_path

def bfs(maze):
    start, goal = get_start_goal(maze)
    queue = deque([(start, [start])])
    visited = set([start])
    
    visited_count = 0  # đếm số ô đã duyệt
    
    # Vòng lặp BFS
    while queue:
        current, path = queue.popleft()
        visited_count += 1
        
        # Kiểm tra nếu đến đích
        if current == goal:
            print_maze_with_path(maze, path, visited_count)
            return path
        
        # Duyệt các ô lân cận
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    print("Không tìm thấy đường đi!")
    return None