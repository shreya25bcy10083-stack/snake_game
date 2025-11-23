import pygame
from snake import Snake, Food

pygame.init()

# ---------------- GAME SETTINGS -------------------
WIDTH, HEIGHT = 600, 600
CELL = 20
GRID_SIZE = WIDTH // CELL

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Player Mode")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 26)

# Always 10 food
food_count = 10


# ---------------- RESET FUNCTION -------------------

def reset_game():
    snake = Snake(GRID_SIZE)
    food = Food(GRID_SIZE, food_count)
    score = 0
    time_left = 30   # 30 seconds
    game_started = False
    move_buffer = False
    win = False

    return snake, food, score, time_left, game_started, move_buffer, win


snake, food, score, time_left, game_started, move_buffer, win = reset_game()

# Timer event every 1 second
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)

running = True

# ---------------- MAIN GAME LOOP -------------------

while running:
    clock.tick(10)  # normal speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Countdown timer
        if event.type == timer_event and game_started:
            time_left -= 1
            if time_left <= 0:
                game_started = False  # time over

        if event.type == pygame.KEYDOWN:

            # Start game
            if event.key == pygame.K_RETURN:
                game_started = True

            # Restart game
            if event.key == pygame.K_r:
                snake, food, score, time_left, game_started, move_buffer, win = reset_game()

            # Manual movement
            if game_started:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                    move_buffer = True
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                    move_buffer = True
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                    move_buffer = True
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))
                    move_buffer = True

    # -------- GAME RUNNING STATE ---------
    if game_started:

        # Snake moves only if player pressed a key
        if move_buffer:
            snake.move()
            move_buffer = False

        # ---------- FOOD CHECK ----------
        if snake.body[0] in food.positions:
            snake.grow()
            food.positions.remove(snake.body[0])
            score += 1

            # Respawn food
            if len(food.positions) < food.count:
                food.new_positions(snake.body)

            # WIN CONDITION
            if score == food.count:
                win = True
                game_started = False

        # ---------- COLLISION CHECK ----------
        if snake.check_collision():
            win = False
            game_started = False

    # ----------- DRAW EVERYTHING ------------

    screen.fill((0, 0, 0))

    # Snake
    for x, y in snake.body:
        pygame.draw.rect(screen, (0,255,0), (x*CELL, y*CELL, CELL, CELL))

    # Food
    for fx, fy in food.positions:
        pygame.draw.rect(screen, (255,0,0), (fx*CELL, fy*CELL, CELL, CELL))

    # HUD
    info_text = f"Score: {score} | Time: {time_left} | Food Left: {food.count - score}"
    screen.blit(font.render(info_text, True, (255,255,255)), (10, 10))

    # --------- TITLE/STATUS SCREEN ---------
    if not game_started:
        if win:
            msg = " YOU WIN! Press R to Restart"
        elif time_left <= 0:
            msg = " TIME'S UP! YOU LOST. Press R to Restart"
        elif score > 0:
            msg = " You crashed! Press R to Restart"
        else:
            msg = "Press ENTER to Start"

        screen.blit(font.render(msg, True, (255,200,0)), (WIDTH//2 - 200, HEIGHT//2))

    pygame.display.update()

pygame.quit()








