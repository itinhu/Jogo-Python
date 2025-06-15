import pygame
import random

WIDTH = 1200
HEIGHT = 600

pygame.init()
pygame.mixer.init()  # Inicializa o sistema de áudio

# Estado do jogo
game_state = "intro"

# Sons
sound_on = True
try:
    bg_music = pygame.mixer.Sound("sounds/bg.wav")
    jump_sound = pygame.mixer.Sound("sounds/jump_hero.mp3")
    bg_music.set_volume(0.5)  # Volume da música de fundo
    jump_sound.set_volume(0.7)  # Volume do som de pulo
except:
    print("Erro ao carregar os sons")
    bg_music = None
    jump_sound = None

# Fator de escala das imagens (ajuste conforme desejar)
scale_factor = 0.3

# Carregar logo
logo = pygame.image.load("images/logo.png")

# Funções auxiliares para redimensionamento
def scale_images(image_list, scale):
    return [
        pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        for img in image_list
    ]

def scale_image(img, scale):
    return pygame.transform.scale(
        img, (int(img.get_width() * scale), int(img.get_height() * scale))
    )

# Jogador
player_img_idle = scale_images(
    [pygame.image.load(f"images/ninja/idle__{i:03}.png") for i in range(10)],
    scale_factor
)

player_img_run = scale_images(
    [pygame.image.load(f"images/ninja/run__{i:03}.png") for i in range(10)],
    scale_factor
)

player_img_jump = scale_image(
    pygame.image.load("images/ninja/jump__008.png"),
    scale_factor
)

player_rect = pygame.Rect(100, HEIGHT - 150, player_img_idle[0].get_width(), player_img_idle[0].get_height())
player_facing_right = True

# Física do jogador
player_vy = 0
gravity = 0.5
jump_strength = -15
on_ground = False
player_speed = 7

# Estado do player
player_state = "idle"
current_frame = 0
animation_timer = 0
animation_speed = 0.1

# Inimigos
enemy_img = scale_images(
    [pygame.image.load(f"images/inimigo01/run__{i:03}.png") for i in range(10)],
    scale_factor
)

enemy_dead_img = scale_images(
    [pygame.image.load(f"images/inimigo01/dead__{i:03}.png") for i in range(10)],
    scale_factor
)

enemy_attack_img = scale_images(
    [pygame.image.load(f"images/inimigo01/attack__{i:03}.png") for i in range(10)],
    scale_factor
)

enemies = []
for i in range(3):
    rect = pygame.Rect(
        400 + i * 300,
        HEIGHT - 150,
        enemy_img[0].get_width(),
        enemy_img[0].get_height()
    )
    enemies.append({
        "rect": rect,
        "direction": -1,
        "facing_right": False,
        "frame": 0,
        "timer": 0,
        "alive": True,
        "death_frame": 0,
        "state": "patrol",  # patrol, attack
        "attack_frame": 0,
        "attack_timer": 0,
        "attack_cooldown": 0
    })

# Plataformas
platforms = [pygame.Rect(0, HEIGHT - 50, WIDTH, 50)]

# Fundo do menu
bg_menu = pygame.image.load("images/bg_menu.png")
bg_menu = pygame.transform.scale(bg_menu, (WIDTH, HEIGHT))

# Contador de inimigos mortos
enemies_killed = 0

def start_intro():
    global game_state
    game_state = "intro"
    clock.schedule_unique(show_menu, 2.0)


def show_menu():
    global game_state
    game_state = "menu"
    if sound_on and bg_music:
        bg_music.play(-1)  # -1 faz a música tocar em loop


def start_game():
    global game_state
    game_state = "game"
    if sound_on and bg_music:
        bg_music.stop()


def draw():
    screen.clear()

    if game_state == "intro":
        screen.fill((0, 0, 0))
        screen.blit(logo, (WIDTH // 2 - logo.get_width() // 2, HEIGHT // 2 - logo.get_height() // 2))

    elif game_state == "menu":
<<<<<<< HEAD
        screen.blit(bg_menu, (0, 0))
        screen.draw.text("Ninja Dash", center=(WIDTH // 2, 80), fontsize=60, color="white")
        screen.draw.text("Start Game", center=(WIDTH // 2, 200), fontsize=45, color="white")
        screen.draw.text("Sound On/Off", center=(WIDTH // 2, 270), fontsize=45, color="white")
        screen.draw.text("Exit", center=(WIDTH // 2, 340), fontsize=45, color="white")

    elif game_state == "gameover":
        screen.fill((0, 0, 0))
        screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT // 2 - 50), fontsize=80, color="red")
        screen.draw.text(f"Inimigos Derrotados: {enemies_killed}", center=(WIDTH // 2, HEIGHT // 2 + 50), fontsize=40, color="white")
        screen.draw.text("Clique para voltar ao menu", center=(WIDTH // 2, HEIGHT // 2 + 150), fontsize=30, color="white")

    elif game_state == "game":
        screen.fill((100, 150, 255))

        for plat in platforms:
            screen.draw.filled_rect(plat, (50, 50, 50))

        # Desenha contador
        screen.draw.text(f"Inimigos Derrotados: {enemies_killed}", (20, 20), fontsize=30, color="white")

        # Desenha inimigos
        for enemy in enemies:
            if enemy["alive"]:
                if enemy["state"] == "attack":
                    img = enemy_attack_img[enemy["attack_frame"]]
                else:
                    img = enemy_img[enemy["frame"]]
                if not enemy["facing_right"]:
                    img = pygame.transform.flip(img, True, False)
                screen.blit(img, (enemy["rect"].x, enemy["rect"].y))
            else:
                # Animação de morte
                img = enemy_dead_img[enemy["death_frame"]]
                if not enemy["facing_right"]:
                    img = pygame.transform.flip(img, True, False)
                screen.blit(img, (enemy["rect"].x, enemy["rect"].y))

        # Desenha jogador
        if player_state == "idle":
            img = player_img_idle[current_frame]
        elif player_state == "running":
            img = player_img_run[current_frame]
        elif player_state == "jumping":
            img = player_img_jump

        if not player_facing_right:
            img = pygame.transform.flip(img, True, False)

        screen.blit(img, (player_rect.x, player_rect.y))


def update_enemy(enemy):
    if not enemy["alive"]:
        # Atualiza animação de morte
        enemy["timer"] += 0.016
        if enemy["timer"] >= animation_speed:
            enemy["timer"] = 0
            enemy["death_frame"] = min(enemy["death_frame"] + 1, 9)
            if enemy["death_frame"] == 9:  # Animação de morte terminou
                spawn_new_enemy()
                enemies.remove(enemy)
        return

    # Atualiza cooldown do ataque
    if enemy["attack_cooldown"] > 0:
        enemy["attack_cooldown"] -= 0.016

    # Verifica distância do jogador
    distance_to_player = abs(enemy["rect"].x - player_rect.x)
    
    if distance_to_player < 100 and enemy["attack_cooldown"] <= 0:
        enemy["state"] = "attack"
        enemy["attack_frame"] = 0
        enemy["attack_timer"] = 0
        enemy["attack_cooldown"] = 2.0  # 2 segundos de cooldown

    if enemy["state"] == "attack":
        enemy["attack_timer"] += 0.016
        if enemy["attack_timer"] >= animation_speed:
            enemy["attack_timer"] = 0
            enemy["attack_frame"] = (enemy["attack_frame"] + 1) % 10
            if enemy["attack_frame"] == 5:  # Meio da animação de ataque
                if distance_to_player < 100:  # Verifica colisão durante o ataque
                    game_over()
        if enemy["attack_frame"] == 9:  # Fim da animação de ataque
            enemy["state"] = "patrol"
    else:
        enemy["rect"].x += enemy["direction"] * 2
        if enemy["rect"].x < 100 or enemy["rect"].x > WIDTH - 100:
            enemy["direction"] *= -1
            enemy["facing_right"] = not enemy["facing_right"]

        enemy["timer"] += 0.016
        if enemy["timer"] >= animation_speed:
            enemy["timer"] = 0
            enemy["frame"] = (enemy["frame"] + 1) % 10


def update():
    global player_vy, on_ground, animation_timer, current_frame, player_state, player_facing_right, enemies_killed

    if game_state == "game":
        keys = keyboard
        moving = False

        # Movimento horizontal
        if keys.left:
            player_rect.x -= player_speed
            player_facing_right = False
            moving = True
        if keys.right:
            player_rect.x += player_speed
            player_facing_right = True
            moving = True

        # Estado
        if not on_ground:
            player_state = "jumping"
        elif moving:
            player_state = "running"
        else:
            player_state = "idle"

        # Animação
        animation_timer += 0.016
        if animation_timer >= animation_speed:
            animation_timer = 0
            current_frame = (current_frame + 1) % 10

        # Inimigos
        for enemy in enemies:
            update_enemy(enemy)

        # Gravidade
        player_vy += gravity
        player_rect.y += player_vy

        # Colisão
        on_ground = False
        for plat in platforms:
            if player_rect.colliderect(plat) and player_vy >= 0:
                player_rect.bottom = plat.top
                player_vy = 0
                on_ground = True

        # Fora da tela
        if player_rect.y > HEIGHT:
            reset_player()

        # Colisão com inimigos
        for enemy in enemies:
            if enemy["alive"] and player_rect.colliderect(enemy["rect"]):
                # Verifica se o jogador está caindo e acima do inimigo
                if player_vy > 0 and player_rect.bottom < enemy["rect"].centery:
                    # Mata o inimigo
                    enemy["alive"] = False
                    enemy["death_frame"] = 0
                    enemy["timer"] = 0
                    enemies_killed += 1
                    # Faz o jogador pular um pouco
                    player_vy = jump_strength / 2
                else:
                    # Jogador morre
                    reset_player()


def reset_player():
    global player_vy, current_frame, player_state
    player_rect.midbottom = (100, platforms[0].top)
    player_vy = 0
    current_frame = 0
    player_state = "idle"


def on_key_down(key):
    global player_vy, current_frame, player_state
    if game_state == "game":
        if key == keys.SPACE and on_ground:
            player_vy = jump_strength
            current_frame = 0
            player_state = "jumping"
            if sound_on and jump_sound:
                jump_sound.play()

=======
        screen.blit("bg_menu", (0, 0)) 
        screen.draw.text("Ninja Dash", center=(WIDTH // 2, 60), fontsize=50, color="white")
        screen.draw.text("Começar", center=(WIDTH // 2, 160), fontsize=40, color="white")
        screen.draw.text("Som On/Off", center=(WIDTH // 2, 220), fontsize=40, color="white")
        screen.draw.text("Sair", center=(WIDTH // 2, 280), fontsize=40, color="white")
>>>>>>> 03cb03477029ab9c54bfd0bb94b654653fbdf8ea

def on_mouse_down(pos):
    global sound_on, game_state, enemies_killed
    if game_state == "menu":
<<<<<<< HEAD
        if 160 < pos[1] < 230:
            start_game()
        elif 230 < pos[1] < 300:
=======
        if 130 < pos[1] < 190:
            print("Start Game clicked")  
        elif 190 < pos[1] < 250:
>>>>>>> 03cb03477029ab9c54bfd0bb94b654653fbdf8ea
            sound_on = not sound_on
            if sound_on and bg_music:
                bg_music.play(-1)
            elif bg_music:
                bg_music.stop()
        elif 300 < pos[1] < 370:
            exit()
    elif game_state == "gameover":
        game_state = "menu"
        enemies_killed = 0
        reset_player()
        for enemy in enemies[:]:
            enemies.remove(enemy)
        for i in range(3):
            spawn_new_enemy()


def spawn_new_enemy():
    # Encontra uma posição aleatória para o novo inimigo
    x = random.randint(100, WIDTH - 100)
    rect = pygame.Rect(
        x,
        HEIGHT - 150,
        enemy_img[0].get_width(),
        enemy_img[0].get_height()
    )
    enemies.append({
        "rect": rect,
        "direction": -1 if x > WIDTH/2 else 1,
        "facing_right": x < WIDTH/2,
        "frame": 0,
        "timer": 0,
        "alive": True,
        "death_frame": 0,
        "state": "patrol",
        "attack_frame": 0,
        "attack_timer": 0,
        "attack_cooldown": 0
    })


def game_over():
    global game_state
    game_state = "gameover"


start_intro()
