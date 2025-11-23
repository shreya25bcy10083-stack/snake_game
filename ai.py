from collections import deque
import random

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

DIRECTIONS = [UP, DOWN, LEFT, RIGHT]


def bfs_path(start, goal, blocks, grid_size):
    queue = deque([start])
    visited = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            break

        x, y = current
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            nxt = (nx, ny)

            if (
                0 <= nx < grid_size and
                0 <= ny < grid_size and
                nxt not in visited and
                nxt not in blocks
            ):
                visited[nxt] = current
                queue.append(nxt)

    return visited


def reconstruct_path(visited, start, goal):
    path = []
    node = goal

    while node in visited:
        path.append(node)
        node = visited[node]

    path.reverse()
    return path if path and path[0] == start else []


def safe_random_move(snake):
    head = snake.body[0]

    safe = []
    for dx, dy in DIRECTIONS:
        nx, ny = head[0] + dx, head[1] + dy
        nxt = (nx, ny)
        if (
            0 <= nx < snake.grid and
            0 <= ny < snake.grid and
            nxt not in snake.body
        ):
            safe.append((dx,dy))

    return random.choice(safe) if safe else snake.direction


def tail_safe(snake):
    head = snake.body[0]
    tail = snake.body[-1]

    # Only block the body except tail (tail moves next turn)
    blocks = snake.body[:-1]

    visited = bfs_path(head, tail, blocks, snake.grid)
    path = reconstruct_path(visited, head, tail)
    return len(path) > 1


def choose_move(snake, food):
    head = snake.body[0]

    # Pick nearest food
    target = min(food.positions, key=lambda f: abs(f[0] - head[0]) + abs(f[1] - head[1]))

    # Block FULL snake (tail does NOT move when eating)
    visited = bfs_path(head, target, snake.body, snake.grid)
    path = reconstruct_path(visited, head, target)

    if path and len(path) > 1 and tail_safe(snake):
        nx, ny = path[1]
        return (nx - head[0], ny - head[1])

    # fallback: random but safe
    return safe_random_move(snake)






