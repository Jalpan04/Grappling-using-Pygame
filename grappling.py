import pygame
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Constants
GRAVITY = 0.2
FRICTION = 0.98
PLAYER_RADIUS = 10
HOOK_SPEED = 15
MAX_HOOK_DISTANCE = 500
PULL_FORCE = 0.8

# Player
player_pos = pygame.Vector2(0, 0)  # Set initial position to (0, 0) but we will set it later
player_vel = pygame.Vector2(0, 0)
on_ground = False

# Hook
hook_pos = pygame.Vector2(0, 0)
hook_vel = pygame.Vector2(0, 0)
hook_attached = False
hook_flying = False
mouse_held = False

# World
platforms = [
    pygame.Rect(300, 400, 200, 20),
    pygame.Rect(600, 300, 150, 20),
    pygame.Rect(900, 250, 150, 20)
]
last_platform_x = 1000
highest_platform_y = 250  # Y-coordinate of highest platform
camera_offset = pygame.Vector2(0, 0)

def shoot_hook(target):
    global hook_flying, hook_attached, hook_pos, hook_vel
    hook_attached = False
    hook_flying = True
    hook_pos.update(player_pos)
    direction = (target + camera_offset - player_pos).normalize()
    hook_vel = direction * HOOK_SPEED

def update_hook():
    global hook_flying, hook_attached, hook_pos
    if hook_flying:
        hook_pos += hook_vel
        if (hook_pos - player_pos).length() > MAX_HOOK_DISTANCE:
            hook_flying = False
        for plat in platforms:
            if plat.collidepoint(hook_pos):
                hook_flying = False
                hook_attached = True
                hook_pos -= hook_vel
                break

def pull_player_to_hook():
    global player_pos, player_vel, hook_pos
    to_hook = hook_pos - player_pos
    distance = to_hook.length()
    if distance < 5:
        player_pos.update(hook_pos)
        player_vel *= 0
        return
    direction = to_hook.normalize()
    player_vel += direction * PULL_FORCE

def handle_platform_collisions():
    global player_pos, player_vel, on_ground
    on_ground = False
    for plat in platforms:
        if (plat.left < player_pos.x < plat.right and
            player_pos.y + PLAYER_RADIUS > plat.top >= player_pos.y + PLAYER_RADIUS - player_vel.y and
            player_vel.y > 0):
            player_pos.y = plat.top - PLAYER_RADIUS
            player_vel.y = 0
            on_ground = True

def generate_platforms_if_needed():
    global last_platform_x, highest_platform_y
    # Horizontal
    while last_platform_x < player_pos.x + WIDTH:
        x = last_platform_x + random.randint(150, 300)
        y = random.randint(200, HEIGHT - 100)
        width = random.randint(100, 200)
        platforms.append(pygame.Rect(x, y, width, 20))
        last_platform_x = x

    # Vertical (generate above current player position if going up)
    threshold = player_pos.y - 300
    while highest_platform_y > threshold:
        x = random.randint(int(player_pos.x) - 300, int(player_pos.x) + 300)
        width = random.randint(100, 200)
        new_platform = pygame.Rect(x, highest_platform_y - 100, width, 20)
        platforms.append(new_platform)
        highest_platform_y -= 100

def start_on_random_platform():
    global player_pos
    # Choose a random platform
    platform = random.choice(platforms)
    # Set the player position on the platform
    player_pos.x = random.randint(platform.left + PLAYER_RADIUS, platform.right - PLAYER_RADIUS)
    player_pos.y = platform.top - PLAYER_RADIUS

running = True
start_on_random_platform()  # Set the player to a random platform before starting the game

while running:
    dt = clock.tick(60) / 1000
    screen.fill((25, 25, 25))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_held = True
            shoot_hook(pygame.Vector2(pygame.mouse.get_pos()))
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_held = False
            hook_attached = False
            hook_flying = False

    # Physics
    player_vel.y += GRAVITY

    # Hook logic
    if hook_flying:
        update_hook()
    if hook_attached and mouse_held:
        pull_player_to_hook()
    elif not mouse_held:
        hook_attached = False
        hook_flying = False

    # Movement and collisions
    player_pos += player_vel
    handle_platform_collisions()
    player_vel *= FRICTION

    # Platform generation
    generate_platforms_if_needed()

    # Camera follows player
    camera_offset.x = player_pos.x - WIDTH / 2
    camera_offset.y = player_pos.y - HEIGHT / 2

    # Draw world
    for plat in platforms:
        pygame.draw.rect(screen, (100, 100, 220), plat.move(-camera_offset))

    if (hook_flying or hook_attached) and mouse_held:
        pygame.draw.line(screen, (200, 200, 200), player_pos - camera_offset, hook_pos - camera_offset, 2)
        pygame.draw.circle(screen, (255, 100, 100), hook_pos - camera_offset, 4)

    pygame.draw.circle(screen, (100, 200, 255), player_pos - camera_offset, PLAYER_RADIUS)

    pygame.display.flip()

pygame.quit()
