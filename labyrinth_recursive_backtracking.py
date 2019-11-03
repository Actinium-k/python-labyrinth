from random import sample

N, S, E, W, V = 1, 2, 4, 8, 16
opposite = {N:S, S:N, E:W, W:E}
move = {N: lambda x, y: (x, y-1),
    S: lambda x, y: (x, y+1),
    E: lambda x, y: (x+1, y),
    W: lambda x, y: (x-1, y)}
directions = lambda: sample((N, S, E, W), 4)

def maze_generation(width, height):
    maze = [[0] * width for i in range(height)]
    total_cells = width * height
    x, y = 0, 0

    while total_cells > 1:
        for d in directions():
            nx, ny = move[d](x, y)
            if not 0 <= nx < width or not 0 <= ny < height:
                continue
            elif maze[ny][nx] == 0:
                maze[y][x] |= d
                maze[ny][nx] |= opposite[d]
                x, y = nx, ny
                break

        else:
            for d in directions():
                nx, ny = move[d](x, y)
                if (not 0 <= nx < width
                 or not 0 <= ny < height
                 or not maze[ny][nx] & V == 0):
                    continue
                elif not maze[ny][nx] & opposite[d] == 0:
                    maze[y][x] |= V
                    total_cells -= 1
                    x, y = nx, ny
                    break

    return maze

def draw_maze(maze):
    width = len(maze[0])
    height = len(maze)
    print('█' * (width*2+1))

    for i in range(height*2):
        line = ['█']
        for j in range(width*2):
            if i % 2 == 0 and j % 2 == 0:
                line.append(' ')
            elif i % 2 == 0 and j % 2 != 0:
                if not maze[i//2][j//2] & E == 0:
                    line.append(' ')
                else:
                    line.append('█')
            elif i % 2 != 0 and j % 2 == 0:
                if not maze[i//2][j//2] & S == 0:
                    line.append(' ')
                else:
                    line.append('█')
            else:
                line.append('█')
        print(''.join(line))

draw_maze(maze_generation(15, 15))
