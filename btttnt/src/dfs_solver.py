from src.core_logic import get_start_goal, get_neighbors, print_maze_with_path

def dfs(maze):
    start, goal = get_start_goal(maze)
    stack = [(start, [start])]
    visited = set([start])
    
    visited_count = 0
    
    # Vòng lặp DFS
    while stack:
        current, path = stack.pop()  # Lấy từ đỉnh stack (LIFO)
        visited_count += 1
        
        # Nếu đến đích
        if current == goal:
            print_maze_with_path(maze, path, visited_count)
            return path
        
        # Duyệt các ô lân cận
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))
    
    print("Không tìm thấy đường đi!")
    return None