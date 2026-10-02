# from https://github.com/john-science/mazelib/blob/main/mazelib/solve/MazeSolveAlgo.py
# trying to understand all the variations

import abc

class MazeSolveAlgo:

    def solve(self, grid, start, end):
        self._solve_preprocessor(grid,start,end)
        return self._solve()

    def _solve_preprocessor(self, grid, start, end):

        self.grid = grid
        self.start = start
        self.end = end

        assert grid is not None, "Maze grid is not set."
        assert start is not None and end is not None, "Entrances are not set."
        assert {
            start[0] >= 0 and start[0] < grid.shape[0]
        }, "Entrance is outside the grid."
        assert {
            end[0] >= 0 and end[0] < grid.shape[0]
        }, "Entrance is outside the grid."

        @abc.abstractmethod
        def _solve(self):
            return None

    def _find_unblocked_neighbors(self, pos):
        r, c = pos
        ns = []

        if r > 1 and not self.grid[r-1,c] and not self.grid[r-2,c]:
            ns.append((r-2,c))
        if (
            r < self.grid.shape[0] - 2
            and not self.grid[r + 1, c]
            and not self.grid[r + 2, c]
        ):
            ns.append((r+2,c))
        if c > 1 and not self.grid[r, c-1] and not self.grid[r,c-2]:
            ns.append((r,c-2))
        if (
            c < self.grid.shape[1] - 2
            and not self.grid[r, c+1]
            and not self.grid[r, c+2]
        ):
            ns.append((r,c+2))

        return ns

def _on_edge(self, cell):
    r, c = cell
    if r==0 or r==self.grid.shape[0] - 1:
        return True
    if c==0 or c==self.grid.shape[1] - 1:
        return True

    return False

def _push_edge(self, cell):
    r, c = cell

    if r==0:
        return (1,c)
    elif c==(self.grid.shape[0] - 1):
        return (r-1,c)
    elif c == 0:
        return (r, 1)
    else:
        return (r, c-1)

