import pygame
import sys
from a_star import PuzzleSolver


pygame.init()


WIDTH, HEIGHT = 300, 300
TILE_SIZE = WIDTH // 3
FONT = pygame.font.Font(None, 50)
BLACK, WHITE, GRAY = (0, 0, 0), (255, 255, 255), (200, 200, 200)
FPS = 1


def draw_grid(screen, state):
    screen.fill(WHITE)
    for i in range(3):
        for j in range(3):
            tile_value = state[i][j]
            rect = pygame.Rect(j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if tile_value != 0:
                pygame.draw.rect(screen, GRAY, rect)
                text = FONT.render(str(tile_value), True, BLACK)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
            pygame.draw.rect(screen, BLACK, rect, 2)


def animate_solution(screen, solution):
    clock = pygame.time.Clock()
    for state in solution:
        draw_grid(screen, state.state)
        pygame.display.flip()
        clock.tick(FPS)


def main():
    start_state = [[4, 7, 8], [3, 6, 5], [1, 2, 0]]
    solver = PuzzleSolver(start_state)
    solution = solver.solve_puzzle()

    if not solution:
        print("No solution found.")
        sys.exit()
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("8-Puzzle Solver")
    
    solution = list(solution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        animate_solution(screen, solution)
        running = False

    pygame.quit()

if __name__ == "__main__":
    main()