import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from maps.maze_basic import maze as basic_maze
from src.bfs_solver import bfs
from src.dfs_solver import dfs   

print("BFS:")
bfs(basic_maze)

print("DFS:")
dfs(basic_maze)

if __name__ == "__main__":
    print("\n========== BẢN ĐỒ CƠ BẢN ==========")
    print(">>> CHẠY THUẬT TOÁN BFS:")
    bfs(basic_maze)
    
    print("\n>>> CHẠY THUẬT TOÁN DFS:")
    dfs(basic_maze)
    
    print("\n========== BẢN ĐỒ KHÓ (10x10) ==========")
    print(">>> CHẠY THUẬT TOÁN BFS:")
    bfs(basic_maze)
    
    print("\n>>> CHẠY THUẬT TOÁN DFS:")
    dfs(basic_maze)