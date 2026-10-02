from random import choice

import MazeSolveAlgo

class RandomMouse(MazeSolveAlgo):

    def _solve(self):

        solution = []

        current = self.start
        if self._on_edge(self.start):
            current = self._push_self(self.start)
        solution.append(current)

        while not self._within_one(solution[-1], self.end):
            ns = self._find_unblocked_neighbors(solution[-1])

            nxt = choice(ns)
            solution.append(self._midpoint(solution[-1], nxt))
            solution.append(nxt)

        return [solution]
