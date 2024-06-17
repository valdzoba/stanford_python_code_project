import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball Game")

# Define colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Blue ball properties
blue_ball_radius = 30
blue_ball_pos = [50, 50]
blue_ball_velocity = [3, 3]

# Red ball properties
red_ball_radius = 10
red_ball_pos = [20, height - 20]
red_ball_velocity = [5, -5]

# Define game variables
start_time = time.time()
game_over = False
win_message = ""
start_message = "Click on the Screen to start the Game"
blue_ball_visible = True
red_ball_visible = True
game_started = False
score = 0

def reset_game():
    global blue_ball_pos, blue_ball_velocity, red_ball_pos, red_ball_velocity, start_time, game_over, win_message, blue_ball_visible, red_ball_visible, game_started, start_message
    blue_ball_pos = [50, 50]
    blue_ball_velocity = [3, 3]
    red_ball_pos = [50, height - 50]
    red_ball_velocity = [3, -3]
    start_time = time.time()
    game_over = False
    win_message = ""
    blue_ball_visible = True
    red_ball_visible = True
    game_started = False
    start_message = "Click on the Screen to start the Game"

def display_message(message, pos, color=green):
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=pos)
    screen.blit(text, text_rect)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if not game_started:
                game_started = True
                start_time = time.time()
            elif game_over:
                if win_message == "You win. Wanna play again?":
                    if width // 2 - 50 < mouse_pos[0] < width // 2 + 50 and height // 2 < mouse_pos[1] < height // 2 + 40:
                        score += 1
                        reset_game()
                    elif width // 2 - 50 < mouse_pos[0] < width // 2 + 50 and height // 2 + 40 < mouse_pos[1] < height // 2 + 80:
                        game_over = True
                        win_message = "Game over! Better luck next time"
                    elif width // 2 - 50 < mouse_pos[0] < width // 2 + 50 and height // 2 + 80 < mouse_pos[1] < height // 2 + 120:
                        pygame.quit()
                        sys.exit()
            else:
                blue_distance = ((mouse_pos[0] - blue_ball_pos[0]) ** 2 + (mouse_pos[1] - blue_ball_pos[1]) ** 2) ** 0.5
                red_distance = ((mouse_pos[0] - red_ball_pos[0]) ** 2 + (mouse_pos[1] - red_ball_pos[1]) ** 2) ** 0.5
                if blue_distance <= blue_ball_radius and blue_ball_visible:
                    blue_ball_visible = False
                if red_distance <= red_ball_radius and red_ball_visible:
                    red_ball_visible = False
                if not blue_ball_visible and not red_ball_visible:
                    game_over = True
                    win_message = "You win. Wanna play again?"

    # Move the balls if the game is not over and has started
    if not game_over and game_started:
        if blue_ball_visible:
            blue_ball_pos[0] += blue_ball_velocity[0]
            blue_ball_pos[1] += blue_ball_velocity[1]

            # Bounce the blue ball off the walls
            if blue_ball_pos[0] - blue_ball_radius <= 0 or blue_ball_pos[0] + blue_ball_radius >= width:
                blue_ball_velocity[0] = -blue_ball_velocity[0]
            if blue_ball_pos[1] - blue_ball_radius <= 0 or blue_ball_pos[1] + blue_ball_radius >= height:
                blue_ball_velocity[1] = -blue_ball_velocity[1]

        if red_ball_visible:
            red_ball_pos[0] += red_ball_velocity[0]
            red_ball_pos[1] += red_ball_velocity[1]

            # Bounce the red ball off the walls
            if red_ball_pos[0] - red_ball_radius <= 0 or red_ball_pos[0] + red_ball_radius >= width:
                red_ball_velocity[0] = -red_ball_velocity[0]
            if red_ball_pos[1] - red_ball_radius <= 0 or red_ball_pos[1] + red_ball_radius >= height:
                red_ball_velocity[1] = -red_ball_velocity[1]

    # Clear the screen
    screen.fill(white)

    # Draw the balls if they are visible
    if blue_ball_visible:
        pygame.draw.circle(screen, blue, blue_ball_pos, blue_ball_radius)
    if red_ball_visible:
        pygame.draw.circle(screen, red, red_ball_pos, red_ball_radius)

    # Draw start message if game has not started
    if not game_started:
        display_message(start_message, (width // 2, height // 2))

    # Draw win message if game is over
    if game_over and win_message:
        display_message(win_message, (width // 2, height // 2 - 80))
        display_message("Yes", (width // 2, height // 2))
        display_message("No", (width // 2, height // 2 + 40))
        display_message("Exit", (width // 2, height // 2 + 80))

    # Display the score
    if game_started:
        display_message(f"Your score is: {score}", (width // 2, 30), black)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
