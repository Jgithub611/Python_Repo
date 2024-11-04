#La matriz binaria N*N se da en un laberinto de la siguiente manera, y el ratón debe moverse desde la coordenada (0,0) hasta la coordenada(N-1,N-1)
def solve_maze(maze):
    Len_maze = len(maze)
    caminos = []
  
    def solve_aux(x, y):
        if x == Len_maze - 1 and y == Len_maze - 1:
            caminos.append((x, y))
            return True
        if x < 0 or x >= Len_maze or y < 0 or y >= Len_maze or maze[x][y] == 1:
            return False
        
        maze[x][y] = 1
        caminos.append((x, y)) 
        
        if solve_aux(x, y + 1): 
            return True
        if solve_aux(x + 1, y):  
            return True
        if solve_aux(x, y - 1): 
            return True
        if solve_aux(x - 1, y):
            return True
        
        caminos.pop()
        maze[x][y] = 0  
    if solve_aux(0, 0):
        return caminos  
    else:
        print("No hay caminos disponibles")
        return -1 

maze = [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [0, 0, 0, 0]
]

caminos = solve_maze(maze)
print(caminos)