from pygame import font, time


def title_font_config():
    font_type = "./Assets/font/Pixeltype.ttf"
    font_size = 100
    title_font = font.Font(font_type, font_size)
    return title_font


def font_config():
    font_type = "./Assets/font/Pixeltype.ttf"
    font_size = 50
    game_font = font.Font(font_type, font_size)
    return game_font


def display_menu_text(screen):
    title_font = title_font_config()
    font = font_config()
    game_title_text = "Runner.py"
    bottom_text = "Press SPACE to play"
    antialising = False
    color = "White"

    game_title_position = (400, 75)
    bottom_text_position = (400, 325)

    game_title_surface = title_font.render(game_title_text, antialising, color)
    bottom_text_surface = font.render(bottom_text, antialising, color)

    game_title_rectangle = game_title_surface.get_rect(center=game_title_position)
    bottom_text_rectangle = bottom_text_surface.get_rect(center=bottom_text_position)

    screen.blit(game_title_surface, game_title_rectangle)
    screen.blit(bottom_text_surface, bottom_text_rectangle)


def display_score(screen, timer):
    font = font_config()

    score = (time.get_ticks() - timer) // 1000
    text = f"Score: {score}"

    color = "Black"
    antialising = False
    position = (400, 30)

    surface = font.render(text, antialising, color)
    rectangle = surface.get_rect(center=(position))

    screen.blit(surface, rectangle)


def display_lose_screen(screen):
    font = font_config()

    lose_text = "You Lose!"
    play_again_text = "Press SPACE to play again"

    antialising = False
    color = "Black"

    lose_text_position = (400, 150)
    lose_text_surface = font.render(lose_text, antialising, color)
    lose_text_rectangle = lose_text_surface.get_rect(midbottom=(lose_text_position))
    screen.blit(lose_text_surface, lose_text_rectangle)

    play_again_text_position = (400, 200)
    play_again_text_surface = font.render(play_again_text, antialising, color)
    play_again_text_rectangle = play_again_text_surface.get_rect(
        midbottom=(play_again_text_position)
    )
    screen.blit(play_again_text_surface, play_again_text_rectangle)
