import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, x):
        heapq.heappush(self.queue, (x.f, x))

    def dequeue(self):        
        return heapq.heappop(self.queue)[1]
    
    def is_empty(self):
        return len(self.queue) == 0


class Node:
    def __init__(self, state, level, parent=None):
        self.state = state 
        self.parent = parent
        self.h = self.heuristic(self.state)
        self.f = self.h + level

    def __lt__ (self, other):
        return self.f < other.f
    
    def heuristic(self, state):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        h = 0

        for i in range(3):
            for j in range(3):
                if state[i][j] != goal[i][j]:
                    h += 1
        return h
    
    def __str__ (self):
        s = ""

        for row in self.state:
            for col in row:
                s += str(col)
                s += ' '
            s += '\n'
        return s
    
class PuzzleSolver:
    def __init__(self, start):
        self.start = Node(start, 0)
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    
    def find_space(self, state):
        space = [(i, j) for i in range(3) for j in range(3) if state[i][j] == 0]
        return space[0]
    
    def find_moves(self, pos):
        x, y = pos
        return [((x + 1, y), 'UP'), ((x - 1, y), 'DOWN'), ((x, y + 1), 'LEFT'), ((x, y - 1), 'RIGHT')]
    
    def find_children(self, state):
        children = []
        space = self.find_space(state)
        moves = self.find_moves(space)

        for move, action in moves:
            if self.is_valid(move):
                child = self.play_move(state, move, space)
                children.append(child)
        return children
    
    def is_valid(self, move):
        x, y = move
        return 0 <= x < 3 and 0 <= y < 3
    
    def play_move(self, state, move, space):
        new_state = [row[:] for row in state]
        x, y = space
        move_x, move_y = move
        new_state[x][y], new_state[move_x][move_y] = new_state[move_x][move_y], new_state[x][y]
        return new_state
    
    def solve_puzzle(self):
        pq = PriorityQueue()
        pq.enqueue(self.start)
        explored = set(tuple(tuple(row) for row in self.start.state))
        while not pq.is_empty():
            node = pq.dequeue()

            if node.state == self.goal:                
                return self.print_solution(node)                        
            children = self.find_children(node.state)      
                 
            for child in children:
                child_tuple = tuple(tuple(row) for row in child)
                if not child_tuple in explored:
                    child_node = Node(child, node.f-node.h + 1, parent=node)                    
                    explored.add(child_tuple)
                    pq.enqueue(child_node)
        return False
    
    def print_solution(self, node):        
        solution = []
        while node:
            solution.append(node)
            node = node.parent        
        return reversed(solution)


ps = PuzzleSolver([[4, 7, 8], [3, 6, 5], [1, 2, 0]])
solution = ps.solve_puzzle()

if solution:
    for state in solution:
        print(state)
else:
    print(solution)
