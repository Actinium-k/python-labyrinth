# Python Labyrinth

*_Generates a labyrinth using the recursive backtracking algorithm_*
*Todo: implement more algorithms (Hunt and Kill, Aldous-Broder, Kruskal)

### How it works

This implementation of the recursive backtracking algorithm makes use of bitwise operators. The four cardinal directions are assigned an unique power of 2, as well as the V flag, which is used to mark a cell as visited.

```python
N, S, E, W, V = 1, 2, 4, 8, 16
```

Or in binary:

```
N = 00001
S = 00010
E = 00100
W = 01000
V = 10000
```

Whenever we need to carve a wall, we use the | operator.

```python
maze[0][0] = 0  #   00000
maze[0][0] |= S # | 00010 # Carved the southern wall
maze[0][0] |= W # | 01000 # Carved the western wall
maze[0][0] = 10 # = 01010 # Final cell with two carved walls
```

In order to check if a cell contains a specific flag, we use the & operator. If the result is 0, it means that the flag is absent.

```python
maze[0][0] = 10     #   00010
maze[0][0] & S == 0 # & 00010
True                # = 00010 (Result is not 0, flag S is present)

maze[0][0] & N == 0 # & 00001
False               # = 00000 (Result if 0, flag N is absent)
```

### Recursive backtracking

1. Choose a starting point
2. Randomly choose an adjacent cell, check if the cell is valid and hasn't been visited, and carve if the latter are false
3. If all adjacents cells have been visited, go back to the previous cell
4. When all cells have been visited, end the function