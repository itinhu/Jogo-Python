WIDTH = 800
HEIGHT = 400

# Estados do jogo: intro → menu
game_state = "intro"

# Ator da logo
logo = Actor("logo", center=(WIDTH // 2, HEIGHT // 2))

# Controle de som
sound_on = True

def start_intro():
    global game_state
    game_state = "intro"
    clock.schedule_unique(show_menu, 2.0)

def show_menu():
    global game_state
    game_state = "menu"
    if sound_on:
        sounds.bg.play(-1)

def draw():
    screen.clear()
    if game_state == "intro":
        screen.fill((0, 0, 0))
        logo.draw()
    elif game_state == "menu":
        screen.blit("bg_menu", (0, 0))  # imagem de fundo
        screen.draw.text("Ninja Dash", center=(WIDTH // 2, 60), fontsize=50, color="white")
        screen.draw.text("Start Game", center=(WIDTH // 2, 160), fontsize=40, color="white")
        screen.draw.text("Sound On/Off", center=(WIDTH // 2, 220), fontsize=40, color="white")
        screen.draw.text("Exit", center=(WIDTH // 2, 280), fontsize=40, color="white")

def on_mouse_down(pos):
    global sound_on
    if game_state == "menu":
        if 130 < pos[1] < 190:
            print("Start Game clicked")  # depois você implementa
        elif 190 < pos[1] < 250:
            sound_on = not sound_on
            if sound_on:
                sounds.bg.play(-1)
            else:
                sounds.bg.stop()
        elif 250 < pos[1] < 310:
            exit()

start_intro()
