import pygame
import random
import sys
import math

# Инициализация
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Пять Ночей у Бабушки: 3D Edition")
clock = pygame.time.Clock()

# Цвета
BLACK = (10, 10, 10)
WHITE = (255, 255, 255)
RED = (180, 30, 30)
GREEN = (0, 180, 0)
GRAY = (80, 80, 80)
DARK_GRAY = (40, 40, 40)
YELLOW = (255, 200, 0)
BROWN = (139, 90, 43)
DARK_BROWN = (60, 35, 15)
LIGHT_BROWN = (160, 110, 60)
BLUE = (50, 100, 150)
DARK_BLUE = (20, 40, 60)
WALL_COLOR = (55, 50, 48)
FLOOR_COLOR = (70, 50, 35)
METAL = (90, 90, 95)
METAL_DARK = (50, 50, 55)

# Шрифты
font_large = pygame.font.SysFont("arial", 50, bold=True)
font_med = pygame.font.SysFont("arial", 28)
font_small = pygame.font.SysFont("arial", 18)
font_title = pygame.font.SysFont("arial", 60, bold=True)
font_huge = pygame.font.SysFont("arial", 80, bold=True)
font_tiny = pygame.font.SysFont("arial", 14)

# Локализация
TEXTS = {
    'ru': {
        'studio': 'Dead Loop Studio',
        'presents': 'представляет',
        'choose_language': 'Выберите язык',
        'russian': 'Русский',
        'english': 'English',
        'new_game': 'Новая игра',
        'settings': 'Настройки',
        'exit': 'Выход',
        'back': 'Назад',
        'volume': 'Громкость',
        'fullscreen': 'Полный экран',
        'reset_progress': 'Сбросить прогресс',
        'confirm_reset': 'Уверены, что хотите сбросить прогресс?',
        'yes': 'Да',
        'no': 'Нет',
        'night': 'Ночь',
        'game_title': 'ПЯТЬ НОЧЕЙ У БАБУШКИ',
        'start_night': 'Ночь началась. Интернет есть, но генератор шумит...',
        'energy': 'Энергия',
        'shed': 'Сарай',
        'kitchen': 'Кухня',
        'window': 'Окно',
        'closed': 'ЗАКРЫТ',
        'open': 'ОТКРЫТ',
        'deed': 'Дед',
        'granny': 'Бабушка',
        'cat': 'Кот',
        'hint': 'Нажимай на кнопки, чтобы закрывать двери. Береги генератор!',
        'fail': 'ПРОВАЛ!',
        'win': 'ТЫ ВЫЖИЛ!',
        'win_text': 'Солнце встало. Бабушка принесла завтрак.',
        'click_restart': '(Кликни, чтобы начать заново)',
        'jumpscare_deed': 'ДЕД В САРДЕ!\nОН НАШЕЛ ТВОЙ НОУТБУК\nИ ТЕПЕРЬ ТЫ ЧИНИШЬ ТРАКТОР!',
        'jumpscare_granny': 'БАБУШКА НА КУХНЕ!\nОНА ЗАПЕКАЕТ ТЕБЯ В ДУХОВКУ\nВМЕСТЕ С ПИРОЖКАМИ!',
        'jumpscare_cat': 'КОТ ВАСЬКА В ОКНЕ!\nОН СИДИТ У ТЕБЯ НА ЛИЦЕ\nИ МУРЛЫЧИТ В УХО!',
        'jumpscare_power': 'ГЕНЕРАТОР ЗАГЛОХ!\nДЕД ПРИШЕЛ ЧИНИТЬ ТРАКТОР\nПРЯМО В ТВОЮ КОМНАТУ!',
        'camera': 'Камера',
        'flashlight': 'Фонарик',
        'curtain': 'Шторка',
        'holding': 'ДЕРЖИТЕ!',
        'no_threat': 'Чисто',
        'cat_detected': 'КОТ ОБНАРУЖЕН!',
        'close_curtain': 'ЗАКРОЙТЕ ШТОРКУ!',
        'left_door': 'ДВЕРЬ',
        'right_door': 'ДВЕРЬ',
        'left_light': 'СВЕТ',
        'right_light': 'СВЕТ',
        'curtain_btn': 'ШТОРКА',
        'maximize': 'Развернуть',
        'minimize': 'Свернуть'
    },
    'en': {
        'studio': 'Dead Loop Studio',
        'presents': 'presents',
        'choose_language': 'Choose Language',
        'russian': 'Русский',
        'english': 'English',
        'new_game': 'New Game',
        'settings': 'Settings',
        'exit': 'Exit',
        'back': 'Back',
        'volume': 'Volume',
        'fullscreen': 'Fullscreen',
        'reset_progress': 'Reset Progress',
        'confirm_reset': 'Are you sure you want to reset progress?',
        'yes': 'Yes',
        'no': 'No',
        'night': 'Night',
        'game_title': 'FIVE NIGHTS AT GRANDMA\'S',
        'start_night': 'Night has begun. Internet works, but the generator is noisy...',
        'energy': 'Energy',
        'shed': 'Shed',
        'kitchen': 'Kitchen',
        'window': 'Window',
        'closed': 'CLOSED',
        'open': 'OPEN',
        'deed': 'Grandpa',
        'granny': 'Grandma',
        'cat': 'Cat',
        'hint': 'Click buttons to close doors. Save the generator!',
        'fail': 'FAILED!',
        'win': 'YOU SURVIVED!',
        'win_text': 'The sun is up. Grandma brought breakfast.',
        'click_restart': '(Click to restart)',
        'jumpscare_deed': 'GRANDPA IN THE SHED!\nHE FOUND YOUR LAPTOP\nAND NOW YOU FIX THE TRACTOR!',
        'jumpscare_granny': 'GRANDMA IN THE KITCHEN!\nSHE BAKES YOU IN THE OVEN\nWITH THE PIES!',
        'jumpscare_cat': 'CAT VASYA IN THE WINDOW!\nHE SITS ON YOUR FACE\nAND PURRS IN YOUR EAR!',
        'jumpscare_power': 'GENERATOR DIED!\nGRANDPA CAME TO FIX THE TRACTOR\nRIGHT INTO YOUR ROOM!',
        'camera': 'Camera',
        'flashlight': 'Flashlight',
        'curtain': 'Curtain',
        'holding': 'HOLD!',
        'no_threat': 'Clear',
        'cat_detected': 'CAT DETECTED!',
        'close_curtain': 'CLOSE THE CURTAIN!',
        'left_door': 'DOOR',
        'right_door': 'DOOR',
        'left_light': 'LIGHT',
        'right_light': 'LIGHT',
        'curtain_btn': 'CURTAIN',
        'maximize': 'Maximize',
        'minimize': 'Minimize'
    }
}


class Camera:
    def __init__(self, name, location, color):
        self.name = name
        self.location = location
        self.color = color


class Animatronic:
    def __init__(self, name, start_location, color):
        self.name = name
        self.location = start_location
        self.color = color
        self.timer = random.randint(10, 20)


class Game:
    def __init__(self):
        self.language = 'ru'
        self.state = 'INTRO'
        self.intro_timer = 0
        self.intro_alpha = 0
        self.fade_alpha = 255
        self.fade_direction = -1
        self.next_state = None

        self.settings_volume = 100
        self.settings_fullscreen = False
        self.night_number = 1

        self.night_intro_timer = 0
        self.night_intro_alpha = 0

        # Офис
        self.office_rotation = 0
        self.office_rotation_target = 0
        self.flashlight_on = False
        self.curtain_closed = False
        self.curtain_holding = False
        self.left_door_closed = False
        self.right_door_closed = False
        self.left_light_on = False
        self.right_light_on = False

        # Камеры
        self.cameras = []
        self.current_camera = None
        self.tablet_open = False
        self.setup_cameras()

        # Аниматроники
        self.animatronics = []
        self.setup_animatronics()

        # Время
        self.game_time = 0

        # Размер окна
        self.is_maximized = False
        self.original_size = (WIDTH, HEIGHT)

        self.reset_game()

    def setup_cameras(self):
        self.cameras = [
            Camera("CAM 1", "Кухня", (150, 100, 80)),
            Camera("CAM 2", "Гостиная", (120, 100, 90)),
            Camera("CAM 3", "Коридор слева", (100, 100, 100)),
            Camera("CAM 4", "Коридор справа", (100, 100, 100)),
            Camera("CAM 5", "Спальня бабушки", (140, 110, 100)),
            Camera("CAM 6", "Спальня дедушки", (130, 100, 90)),
            Camera("CAM 7", "Ванная", (110, 130, 140)),
            Camera("CAM 8", "Подвал", (60, 60, 60)),
            Camera("CAM 9", "Чердак", (90, 80, 70)),
            Camera("CAM 10", "Сарай", (100, 90, 70))
        ]

    def setup_animatronics(self):
        self.animatronics = [
            Animatronic('Дед', 'Спальня дедушки', (139, 90, 43)),
            Animatronic('Бабушка', 'Кухня', (160, 110, 60)),
            Animatronic('Кот', 'Чердак', (80, 80, 80))
        ]

    def reset_game(self):
        self.hour = 0
        self.power = 100.0

        self.deed_timer = random.randint(15, 25)
        self.granny_timer = random.randint(10, 20)
        self.cat_timer = random.randint(5, 15)

        self.time_counter = 0
        self.game_state = "PLAYING"
        self.jumpscare_text = ""
        self.message = TEXTS[self.language]['start_night']
        self.message_timer = 0

        self.game_time = 0
        self.office_rotation = 0
        self.office_rotation_target = 0
        self.flashlight_on = False
        self.curtain_closed = False
        self.tablet_open = False
        self.current_camera = None
        self.left_door_closed = False
        self.right_door_closed = False
        self.left_light_on = False
        self.right_light_on = False

        for anim in self.animatronics:
            anim.timer = random.randint(10, 20)
            anim.location = ['Спальня дедушки', 'Кухня', 'Чердак'][self.animatronics.index(anim)]

    def t(self, key):
        return TEXTS[self.language][key]

    def toggle_maximize(self):
        if self.is_maximized:
            screen = pygame.display.set_mode(self.original_size, pygame.RESIZABLE)
            self.is_maximized = False
        else:
            info = pygame.display.Info()
            screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.RESIZABLE)
            self.is_maximized = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    self.toggle_maximize()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                # Кнопка разворачивания окна
                if WIDTH - 100 <= mx <= WIDTH - 20 and 10 <= my <= 50:
                    self.toggle_maximize()

                if self.state == 'INTRO' and self.intro_timer > 2:
                    self.start_fade('LANGUAGE')

                elif self.state == 'LANGUAGE':
                    btn_width = 300
                    btn_x = WIDTH // 2 - btn_width // 2
                    if btn_x <= mx <= btn_x + btn_width and 300 <= my <= 360:
                        self.language = 'ru'
                        self.start_fade('MENU')
                    elif btn_x <= mx <= btn_x + btn_width and 380 <= my <= 440:
                        self.language = 'en'
                        self.start_fade('MENU')

                elif self.state == 'MENU':
                    btn_width = 250
                    btn_x = WIDTH // 2 - btn_width // 2
                    if btn_x <= mx <= btn_x + btn_width and 300 <= my <= 350:
                        self.start_fade('NIGHT_INTRO')
                        self.reset_game()
                    elif btn_x <= mx <= btn_x + btn_width and 370 <= my <= 420:
                        self.start_fade('SETTINGS')
                    elif btn_x <= mx <= btn_x + btn_width and 440 <= my <= 490:
                        pygame.quit()
                        sys.exit()

                elif self.state == 'SETTINGS':
                    btn_width = 250
                    btn_x = WIDTH // 2 - btn_width // 2
                    if btn_x <= mx <= btn_x + btn_width and 250 <= my <= 300:
                        self.settings_volume = max(0, self.settings_volume - 10)
                    elif btn_x + 270 <= mx <= btn_x + 270 + btn_width and 250 <= my <= 300:
                        self.settings_volume = min(100, self.settings_volume + 10)
                    elif btn_x <= mx <= btn_x + btn_width and 330 <= my <= 380:
                        self.settings_fullscreen = not self.settings_fullscreen
                    elif btn_x <= mx <= btn_x + btn_width and 410 <= my <= 460:
                        self.start_fade('CONFIRM_RESET')
                    elif btn_x <= mx <= btn_x + btn_width and 550 <= my <= 600:
                        self.start_fade('MENU')

                elif self.state == 'CONFIRM_RESET':
                    btn_width = 150
                    btn_x = WIDTH // 2 - btn_width - 20
                    if btn_x <= mx <= btn_x + btn_width and 400 <= my <= 460:
                        self.night_number = 1
                        self.settings_volume = 100
                        self.start_fade('SETTINGS')
                    elif btn_x + btn_width + 40 <= mx <= btn_x + btn_width + 40 + btn_width and 400 <= my <= 460:
                        self.start_fade('SETTINGS')

                elif self.state == 'NIGHT_INTRO':
                    if self.night_intro_timer > 3:
                        self.start_fade('PLAYING')

                elif self.state == 'PLAYING':
                    if self.game_state == "PLAYING":
                        if not self.tablet_open:
                            # Панель управления СЛЕВА
                            if 150 <= mx <= 230 and 320 <= my <= 360:
                                self.left_door_closed = not self.left_door_closed
                            elif 150 <= mx <= 230 and 370 <= my <= 410:
                                self.left_light_on = not self.left_light_on
                            # Панель управления СПРАВА
                            elif WIDTH - 230 <= mx <= WIDTH - 150 and 320 <= my <= 360:
                                self.right_door_closed = not self.right_door_closed
                            elif WIDTH - 230 <= mx <= WIDTH - 150 and 370 <= my <= 410:
                                self.right_light_on = not self.right_light_on
                            # Кнопка планшета
                            elif WIDTH // 2 - 80 <= mx <= WIDTH // 2 + 80 and HEIGHT - 80 <= my <= HEIGHT - 30:
                                self.tablet_open = True
                            # Кнопка поворота к окну
                            elif WIDTH // 2 - 220 <= mx <= WIDTH // 2 - 80 and HEIGHT - 80 <= my <= HEIGHT - 30:
                                self.office_rotation_target = 1 if self.office_rotation == 0 else 0
                        else:
                            for i, cam in enumerate(self.cameras):
                                x = 100 + (i % 5) * 200
                                y = 150 + (i // 5) * 150
                                if x <= mx <= x + 180 and y <= my <= y + 130:
                                    self.current_camera = cam
                            if WIDTH // 2 - 80 <= mx <= WIDTH // 2 + 80 and HEIGHT - 80 <= my <= HEIGHT - 30:
                                self.tablet_open = False
                    else:
                        self.start_fade('MENU')

            elif event.type == pygame.MOUSEBUTTONUP:
                if self.state == 'PLAYING' and self.game_state == "PLAYING":
                    self.curtain_holding = False
                    mx, my = pygame.mouse.get_pos()
                    if WIDTH - 140 <= mx <= WIDTH - 20 and 440 <= my <= 500:
                        self.curtain_closed = not self.curtain_closed

    def start_fade(self, target_state):
        self.fade_direction = 1
        self.next_state = target_state

    def update(self, dt):
        if self.fade_direction != 0:
            self.fade_alpha += self.fade_direction * 255 * dt * 2

            if self.fade_alpha >= 255 and self.fade_direction == 1:
                self.fade_alpha = 255
                self.fade_direction = -1
                if self.next_state:
                    self.state = self.next_state
                    self.next_state = None
                    if self.state == 'INTRO':
                        self.intro_timer = 0
                        self.intro_alpha = 0
                    elif self.state == 'NIGHT_INTRO':
                        self.night_intro_timer = 0
                        self.night_intro_alpha = 0

            elif self.fade_alpha <= 0 and self.fade_direction == -1:
                self.fade_alpha = 0
                self.fade_direction = 0

        if self.state == 'INTRO':
            self.intro_timer += dt
            if self.intro_timer < 1:
                self.intro_alpha = min(255, self.intro_alpha + 255 * dt)
            elif self.intro_timer < 3:
                self.intro_alpha = 255
            elif self.intro_timer < 4:
                self.intro_alpha = max(0, self.intro_alpha - 255 * dt)
            else:
                self.start_fade('LANGUAGE')

        elif self.state == 'NIGHT_INTRO':
            self.night_intro_timer += dt
            if self.night_intro_timer < 1:
                self.night_intro_alpha = min(255, self.night_intro_alpha + 255 * dt)
            elif self.night_intro_timer < 2.5:
                self.night_intro_alpha = 255
            elif self.night_intro_timer < 3.5:
                self.night_intro_alpha = max(0, self.night_intro_alpha - 255 * dt)

        elif self.state == 'PLAYING' and self.game_state == "PLAYING":
            if self.office_rotation != self.office_rotation_target:
                diff = self.office_rotation_target - self.office_rotation
                self.office_rotation += diff * dt * 2
                if abs(diff) < 0.01:
                    self.office_rotation = self.office_rotation_target

            if self.office_rotation > 0.5 and pygame.mouse.get_pressed()[0]:
                mx, my = pygame.mouse.get_pos()
                if WIDTH * 0.3 <= mx <= WIDTH * 0.7 and HEIGHT * 0.2 <= my <= HEIGHT * 0.7:
                    self.flashlight_on = True
                else:
                    self.flashlight_on = False
            else:
                self.flashlight_on = False

            drain = 0.3
            if self.left_door_closed: drain += 0.2
            if self.right_door_closed: drain += 0.2
            if self.left_light_on: drain += 0.1
            if self.right_light_on: drain += 0.1
            if self.tablet_open: drain += 0.3
            if self.flashlight_on: drain += 0.4

            self.power -= drain * dt
            if self.power <= 0:
                self.power = 0
                self.game_state = "JUMPSCARE"
                self.jumpscare_text = self.t('jumpscare_power')
                return

            self.game_time += dt * 2
            if self.game_time >= 360:
                self.game_state = "WIN"
                return

            for anim in self.animatronics:
                anim.timer -= dt
                if anim.timer <= 0:
                    self.move_animatronic(anim)
                    anim.timer = random.randint(15, 30)

            self.check_threats()

            if self.message_timer > 0:
                self.message_timer -= dt

    def move_animatronic(self, anim):
        locations = ['Кухня', 'Гостиная', 'Коридор слева', 'Коридор справа',
                     'Спальня бабушки', 'Спальня дедушки', 'Ванная', 'Подвал',
                     'Чердак', 'Сарай']
        anim.location = random.choice(locations)

    def check_threats(self):
        cat_at_window = any(anim.name == 'Кот' and self.office_rotation > 0.5
                            for anim in self.animatronics)

        if cat_at_window and self.flashlight_on and not self.curtain_closed:
            self.game_state = "JUMPSCARE"
            self.jumpscare_text = self.t('jumpscare_cat')

        if self.office_rotation < 0.5:
            deed_at_left = any(anim.name == 'Дед' and anim.location == 'Коридор слева'
                               for anim in self.animatronics)
            granny_at_right = any(anim.name == 'Бабушка' and anim.location == 'Коридор справа'
                                  for anim in self.animatronics)

            if deed_at_left and not self.left_door_closed:
                self.game_state = "JUMPSCARE"
                self.jumpscare_text = self.t('jumpscare_deed')
            elif granny_at_right and not self.right_door_closed:
                self.game_state = "JUMPSCARE"
                self.jumpscare_text = self.t('jumpscare_granny')

    def draw(self):
        screen.fill(BLACK)

        if self.state == 'INTRO':
            surf1 = font_title.render(self.t('studio'), True, YELLOW)
            surf1.set_alpha(self.intro_alpha)
            rect1 = surf1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
            screen.blit(surf1, rect1)

            surf2 = font_med.render(self.t('presents'), True, WHITE)
            surf2.set_alpha(self.intro_alpha)
            rect2 = surf2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
            screen.blit(surf2, rect2)

        elif self.state == 'LANGUAGE':
            self.draw_text(self.t('choose_language'), font_large, WIDTH // 2, 200, WHITE)
            btn_width = 300
            btn_x = WIDTH // 2 - btn_width // 2
            self.draw_button(self.t('russian'), btn_x, 300, btn_width, 60, GRAY)
            self.draw_button(self.t('english'), btn_x, 380, btn_width, 60, GRAY)

        elif self.state == 'MENU':
            self.draw_text(self.t('game_title'), font_title, WIDTH // 2, 150, YELLOW)
            btn_width = 250
            btn_x = WIDTH // 2 - btn_width // 2
            self.draw_button(self.t('new_game'), btn_x, 300, btn_width, 50, GRAY)
            self.draw_button(self.t('settings'), btn_x, 370, btn_width, 50, GRAY)
            self.draw_button(self.t('exit'), btn_x, 440, btn_width, 50, GRAY)

            version_text = f"{self.t('studio')} / V.1.0"
            self.draw_text(version_text, font_small, WIDTH // 2, HEIGHT - 30, GRAY)

        elif self.state == 'SETTINGS':
            self.draw_text(self.t('settings'), font_large, WIDTH // 2, 150, WHITE)

            btn_width = 250
            btn_x = WIDTH // 2 - btn_width // 2

            self.draw_text(f"{self.t('volume')}: {self.settings_volume}%", font_med, WIDTH // 2, 275, WHITE)
            self.draw_button("-", btn_x, 250, btn_width, 50, GRAY)
            self.draw_button("+", btn_x + 270, 250, btn_width, 50, GRAY)

            fs_text = f"{self.t('fullscreen')}: {'ON' if self.settings_fullscreen else 'OFF'}"
            self.draw_button(fs_text, btn_x, 330, btn_width, 50, GRAY)

            self.draw_button(self.t('reset_progress'), btn_x, 410, btn_width, 50, RED)
            self.draw_button(self.t('back'), btn_x, 550, btn_width, 50, GRAY)

        elif self.state == 'CONFIRM_RESET':
            self.draw_text(self.t('confirm_reset'), font_med, WIDTH // 2, 300, WHITE)
            btn_width = 150
            btn_x = WIDTH // 2 - btn_width - 20
            self.draw_button(self.t('yes'), btn_x, 400, btn_width, 60, GREEN)
            self.draw_button(self.t('no'), btn_x + btn_width + 40, 400, btn_width, 60, RED)

        elif self.state == 'NIGHT_INTRO':
            time_text = "12:00 AM"
            night_text = f"{self.t('night')} {self.night_number}"

            surf1 = font_huge.render(time_text, True, WHITE)
            surf1.set_alpha(self.night_intro_alpha)
            rect1 = surf1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
            screen.blit(surf1, rect1)

            surf2 = font_large.render(night_text, True, YELLOW)
            surf2.set_alpha(self.night_intro_alpha)
            rect2 = surf2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
            screen.blit(surf2, rect2)

        elif self.state == 'PLAYING':
            if self.game_state == "PLAYING":
                if self.tablet_open:
                    self.draw_tablet()
                else:
                    self.draw_office()

                self.draw_text(f"{self.t('energy')}: {int(self.power)}%",
                               font_small, 100, 40,
                               GREEN if self.power > 30 else RED)

                self.draw_clock()
                self.draw_controls()

                max_text = self.t('minimize') if self.is_maximized else self.t('maximize')
                self.draw_button(max_text, WIDTH - 100, 10, 80, 40, DARK_GRAY)

            elif self.game_state == "JUMPSCARE":
                screen.fill(RED)
                self.draw_text(self.t('fail'), font_large, WIDTH // 2, HEIGHT // 2 - 100, BLACK)
                lines = self.jumpscare_text.split('\n')
                for i, line in enumerate(lines):
                    self.draw_text(line, font_med, WIDTH // 2, HEIGHT // 2 + i * 40, BLACK)
                self.draw_text(self.t('click_restart'), font_small, WIDTH // 2, HEIGHT - 50, BLACK)

            elif self.game_state == "WIN":
                screen.fill(GREEN)
                self.draw_text(self.t('win'), font_large, WIDTH // 2, HEIGHT // 2 - 50, BLACK)
                self.draw_text(self.t('win_text'), font_med, WIDTH // 2, HEIGHT // 2 + 20, BLACK)
                self.draw_text(self.t('click_restart'), font_small, WIDTH // 2, HEIGHT - 50, BLACK)

        if self.fade_alpha > 0:
            fade_surf = pygame.Surface((WIDTH, HEIGHT))
            fade_surf.fill(BLACK)
            fade_surf.set_alpha(self.fade_alpha)
            screen.blit(fade_surf, (0, 0))

        pygame.display.flip()

    # ==================== ОТРИСОВКА ОФИСА ====================

    def draw_office(self):
        if self.office_rotation < 0.5:
            self.draw_room_forward()
        else:
            self.draw_room_backward()
        self.draw_vignette()

    def draw_vignette(self):
        vignette = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        for i in range(25):
            alpha = int(150 * (i / 25))
            pygame.draw.ellipse(vignette, (0, 0, 0, alpha),
                                (-i * 50, -i * 40, WIDTH + i * 100, HEIGHT + i * 80), 50)
        screen.blit(vignette, (0, 0))

    def draw_room_forward(self):
        W, H = WIDTH, HEIGHT

        # Потолок
        pygame.draw.polygon(screen, (30, 25, 22),
                            [(0, 0), (W, 0), (int(W * 0.82), int(H * 0.22)), (int(W * 0.18), int(H * 0.22))])
        # Пол
        pygame.draw.polygon(screen, FLOOR_COLOR,
                            [(int(W * 0.18), int(H * 0.22)), (int(W * 0.82), int(H * 0.22)),
                             (W, H), (0, H)])
        for i in range(9):
            t = i / 8
            x_top = int(W * 0.18 + W * 0.64 * t)
            x_bot = int(W * 0.05 + W * 0.9 * t)
            pygame.draw.line(screen, (45, 30, 18), (x_top, int(H * 0.22)), (x_bot, H), 2)

        # Стены
        pygame.draw.polygon(screen, WALL_COLOR,
                            [(0, 0), (int(W * 0.18), int(H * 0.22)),
                             (int(W * 0.18), H), (0, H)])
        pygame.draw.polygon(screen, WALL_COLOR,
                            [(W, 0), (int(W * 0.82), int(H * 0.22)),
                             (int(W * 0.82), H), (W, H)])
        pygame.draw.rect(screen, (42, 38, 36),
                         [int(W * 0.18), 0, int(W * 0.64), int(H * 0.22)])

        # Угловые тени
        pygame.draw.line(screen, (10, 8, 6), (0, 0), (int(W * 0.18), int(H * 0.22)), 5)
        pygame.draw.line(screen, (10, 8, 6), (W, 0), (int(W * 0.82), int(H * 0.22)), 5)
        pygame.draw.line(screen, (15, 10, 5), (0, H), (int(W * 0.18), int(H * 0.22)), 4)
        pygame.draw.line(screen, (15, 10, 5), (W, H), (int(W * 0.82), int(H * 0.22)), 4)
        pygame.draw.line(screen, (15, 12, 10),
                         (int(W * 0.18), int(H * 0.22)), (int(W * 0.18), H), 4)
        pygame.draw.line(screen, (15, 12, 10),
                         (int(W * 0.82), int(H * 0.22)), (int(W * 0.82), H), 4)

        # Дверные проёмы
        door_w = int(W * 0.11)
        door_h = int(H * 0.55)
        door_top = int(H * 0.28)

        left_door_rect = pygame.Rect(int(W * 0.03), door_top, door_w, door_h)
        right_door_rect = pygame.Rect(W - int(W * 0.03) - door_w, door_top, door_w, door_h)

        # Тёмные проёмы
        pygame.draw.rect(screen, (5, 3, 2), left_door_rect)
        pygame.draw.rect(screen, (5, 3, 2), right_door_rect)

        # СВЕТ В ПРОХОДАХ (рисуем сразу после проёмов, до рам)
        if self.left_light_on:
            self.draw_hallway_light(left_door_rect, 'left')
        if self.right_light_on:
            self.draw_hallway_light(right_door_rect, 'right')

        # Рама дверей (поверх света)
        pygame.draw.rect(screen, (50, 35, 20), left_door_rect, 5)
        pygame.draw.rect(screen, (50, 35, 20), right_door_rect, 5)

        # Металлические двери
        if self.left_door_closed:
            pygame.draw.rect(screen, METAL, left_door_rect)
            pygame.draw.rect(screen, METAL_DARK, left_door_rect, 3)
            for dy in range(0, door_h, 50):
                for dx in [12, door_w - 15]:
                    pygame.draw.circle(screen, (30, 30, 35),
                                       (left_door_rect.x + dx, left_door_rect.y + dy + 25), 5)
        if self.right_door_closed:
            pygame.draw.rect(screen, METAL, right_door_rect)
            pygame.draw.rect(screen, METAL_DARK, right_door_rect, 3)
            for dy in range(0, door_h, 50):
                for dx in [12, door_w - 15]:
                    pygame.draw.circle(screen, (30, 30, 35),
                                       (right_door_rect.x + dx, right_door_rect.y + dy + 25), 5)

        # Советский ковёр
        carpet_x = int(W * 0.35)
        carpet_y = int(H * 0.05)
        carpet_w = int(W * 0.3)
        carpet_h = int(H * 0.15)
        pygame.draw.rect(screen, (120, 30, 30), [carpet_x, carpet_y, carpet_w, carpet_h])
        pygame.draw.rect(screen, (80, 20, 20), [carpet_x + 5, carpet_y + 5, carpet_w - 10, carpet_h - 10], 3)
        for i in range(5):
            cx = carpet_x + 20 + i * (carpet_w - 40) // 4
            cy = carpet_y + carpet_h // 2
            pygame.draw.polygon(screen, (200, 180, 80),
                                [(cx, cy - 15), (cx + 15, cy), (cx, cy + 15), (cx - 15, cy)])
        for i in range(0, carpet_w, 8):
            pygame.draw.line(screen, (180, 160, 60),
                             (carpet_x + i, carpet_y + carpet_h),
                             (carpet_x + i, carpet_y + carpet_h + 8), 2)

        # Стол
        table_x = int(W * 0.35)
        table_y = int(H * 0.55)
        table_w = int(W * 0.30)
        table_h = int(H * 0.22)

        shadow = pygame.Surface((table_w + 40, 30), pygame.SRCALPHA)
        pygame.draw.ellipse(shadow, (0, 0, 0, 80), [0, 0, table_w + 40, 30])
        screen.blit(shadow, (table_x - 20, table_y + table_h - 5))

        pygame.draw.rect(screen, DARK_BROWN, [table_x, table_y, table_w, table_h])
        pygame.draw.rect(screen, BROWN, [table_x + 5, table_y + 5, table_w - 10, table_h - 10])
        pygame.draw.line(screen, (180, 130, 80),
                         (table_x + 10, table_y + 15),
                         (table_x + table_w - 10, table_y + 15), 2)

        # Кружевная салфетка
        napkin_x = int(W * 0.5)
        napkin_y = int(H * 0.62)
        napkin_r = 35
        pygame.draw.circle(screen, (240, 240, 230), (napkin_x, napkin_y), napkin_r)
        for i in range(16):
            a = math.radians(i * 22.5)
            cx = napkin_x + int((napkin_r - 5) * math.cos(a))
            cy = napkin_y + int((napkin_r - 5) * math.sin(a))
            pygame.draw.circle(screen, (220, 220, 210), (cx, cy), 4)
        pygame.draw.circle(screen, (200, 200, 190), (napkin_x, napkin_y), 15, 2)

        # Вентилятор
        fan_x = napkin_x
        fan_y = napkin_y - 5
        pygame.draw.circle(screen, (50, 50, 50), (fan_x, fan_y), 32)
        pygame.draw.circle(screen, (30, 30, 30), (fan_x, fan_y), 28)
        angle = pygame.time.get_ticks() / 80
        for i in range(3):
            a = math.radians(angle + i * 120)
            x2 = fan_x + int(22 * math.cos(a))
            y2 = fan_y + int(22 * math.sin(a))
            pygame.draw.line(screen, (200, 200, 200), (fan_x, fan_y), (x2, y2), 6)
        pygame.draw.circle(screen, (80, 80, 80), (fan_x, fan_y), 6)

        # Кружка
        mug_x = int(W * 0.42)
        mug_y = int(H * 0.60)
        pygame.draw.rect(screen, (180, 50, 50), [mug_x, mug_y, 25, 30])
        pygame.draw.arc(screen, (180, 50, 50), [mug_x + 25, mug_y + 5, 15, 20], -1.5, 1.5, 3)
        pygame.draw.ellipse(screen, (220, 220, 220), [mug_x - 2, mug_y - 3, 29, 8], 2)

        # Телефон
        phone_x = int(W * 0.58)
        phone_y = int(H * 0.61)
        pygame.draw.rect(screen, (40, 40, 40), [phone_x, phone_y, 40, 25], border_radius=5)
        pygame.draw.rect(screen, (30, 30, 30), [phone_x - 5, phone_y - 8, 50, 10], border_radius=5)
        pygame.draw.circle(screen, (60, 60, 60), (phone_x + 20, phone_y + 15), 8)

        # Панели кнопок (поверх всего)
        self.draw_control_panel(150, 300, 'left')
        self.draw_control_panel(WIDTH - 230, 300, 'right')

    def draw_hallway_light(self, door_rect, side):
        """Реалистичное освещение прохода"""
        W, H = WIDTH, HEIGHT

        # 1. Светлый коридор внутри проёма
        corridor_surf = pygame.Surface((door_rect.width, door_rect.height), pygame.SRCALPHA)
        pygame.draw.rect(corridor_surf, (180, 160, 120, 200), [0, 0, door_rect.width, door_rect.height])

        # Градиент затемнения к краям
        for i in range(20):
            alpha = int(150 * (i / 20))
            pygame.draw.rect(corridor_surf, (0, 0, 0, alpha),
                             [i * 3, i * 3, door_rect.width - i * 6, door_rect.height - i * 6], 2)

        # Дальняя стена коридора
        far_wall_x = door_rect.width // 2 - 20
        far_wall_y = door_rect.height // 3
        far_wall_w = 40
        far_wall_h = 60
        pygame.draw.rect(corridor_surf, (200, 180, 140, 220),
                         [far_wall_x, far_wall_y, far_wall_w, far_wall_h])

        # Лампочка в коридоре
        bulb_x = door_rect.width // 2
        bulb_y = 15
        pygame.draw.circle(corridor_surf, (255, 240, 200, 255), (bulb_x, bulb_y), 8)
        for r in range(20, 5, -5):
            alpha = 100 - r * 3
            pygame.draw.circle(corridor_surf, (255, 230, 150, alpha), (bulb_x, bulb_y), r)

        screen.blit(corridor_surf, door_rect.topleft)

        # 2. Конус света на полу
        floor_light_surf = pygame.Surface((door_rect.width * 3, 150), pygame.SRCALPHA)
        cone_points = [
            (door_rect.width, 0),
            (0, 150),
            (door_rect.width * 2, 150)
        ]
        pygame.draw.polygon(floor_light_surf, (255, 230, 150, 80), cone_points)

        center_cone = [
            (door_rect.width, 0),
            (door_rect.width // 2, 150),
            (door_rect.width * 3 // 2, 150)
        ]
        pygame.draw.polygon(floor_light_surf, (255, 240, 180, 120), center_cone)

        floor_x = door_rect.x - door_rect.width
        floor_y = door_rect.y + door_rect.height - 10
        screen.blit(floor_light_surf, (floor_x, floor_y))

        # 3. Боковое освещение стен
        wall_light_surf = pygame.Surface((60, door_rect.height), pygame.SRCALPHA)
        for i in range(60):
            alpha = int(100 * (1 - i / 60))
            pygame.draw.line(wall_light_surf, (255, 230, 150, alpha),
                             (i, 0), (i, door_rect.height), 2)

        if side == 'left':
            screen.blit(wall_light_surf, (door_rect.x + door_rect.width, door_rect.y))
        else:
            flipped = pygame.transform.flip(wall_light_surf, True, False)
            screen.blit(flipped, (door_rect.x - 60, door_rect.y))

    def draw_control_panel(self, x, y, side):
        panel_w = 80
        panel_h = 130

        pygame.draw.rect(screen, (70, 70, 75), [x, y, panel_w, panel_h])
        pygame.draw.rect(screen, (40, 40, 45), [x, y, panel_w, panel_h], 3)
        pygame.draw.rect(screen, (50, 50, 55), [x + 5, y + 5, panel_w - 10, panel_h - 10], 2)

        # Кнопка ДВЕРЬ
        btn_door_rect = pygame.Rect(x + 10, y + 15, panel_w - 20, 40)
        door_active = (self.left_door_closed if side == 'left' else self.right_door_closed)
        door_color = (220, 50, 50) if door_active else (150, 30, 30)
        pygame.draw.rect(screen, door_color, btn_door_rect)
        pygame.draw.rect(screen, (255, 255, 255), btn_door_rect, 2)
        indicator_color = (255, 100, 100) if door_active else (80, 20, 20)
        pygame.draw.circle(screen, indicator_color, (x + panel_w // 2, y + 10), 4)
        self.draw_text(self.t('left_door' if side == 'left' else 'right_door'),
                       font_tiny, x + panel_w // 2, y + 35, WHITE)

        # Кнопка СВЕТ
        btn_light_rect = pygame.Rect(x + 10, y + 75, panel_w - 20, 40)
        light_active = (self.left_light_on if side == 'left' else self.right_light_on)
        light_color = (200, 200, 220) if light_active else (80, 100, 140)
        pygame.draw.rect(screen, light_color, btn_light_rect)
        pygame.draw.rect(screen, (255, 255, 255), btn_light_rect, 2)
        indicator_color = (255, 255, 150) if light_active else (40, 50, 70)
        pygame.draw.circle(screen, indicator_color, (x + panel_w // 2, y + 70), 4)
        self.draw_text(self.t('left_light' if side == 'left' else 'right_light'),
                       font_tiny, x + panel_w // 2, y + 95, WHITE)

    def draw_room_backward(self):
        W, H = WIDTH, HEIGHT

        pygame.draw.polygon(screen, (30, 25, 22),
                            [(0, 0), (W, 0), (int(W * 0.82), int(H * 0.22)), (int(W * 0.18), int(H * 0.22))])
        pygame.draw.polygon(screen, FLOOR_COLOR,
                            [(int(W * 0.18), int(H * 0.22)), (int(W * 0.82), int(H * 0.22)),
                             (W, H), (0, H)])
        for i in range(9):
            t = i / 8
            x_top = int(W * 0.18 + W * 0.64 * t)
            x_bot = int(W * 0.05 + W * 0.9 * t)
            pygame.draw.line(screen, (45, 30, 18), (x_top, int(H * 0.22)), (x_bot, H), 2)

        pygame.draw.polygon(screen, WALL_COLOR,
                            [(0, 0), (int(W * 0.18), int(H * 0.22)),
                             (int(W * 0.18), H), (0, H)])
        pygame.draw.polygon(screen, WALL_COLOR,
                            [(W, 0), (int(W * 0.82), int(H * 0.22)),
                             (int(W * 0.82), H), (W, H)])
        pygame.draw.rect(screen, (42, 38, 36),
                         [int(W * 0.18), 0, int(W * 0.64), int(H * 0.22)])

        pygame.draw.line(screen, (10, 8, 6), (0, 0), (int(W * 0.18), int(H * 0.22)), 5)
        pygame.draw.line(screen, (10, 8, 6), (W, 0), (int(W * 0.82), int(H * 0.22)), 5)
        pygame.draw.line(screen, (15, 10, 5), (0, H), (int(W * 0.18), int(H * 0.22)), 4)
        pygame.draw.line(screen, (15, 10, 5), (W, H), (int(W * 0.82), int(H * 0.22)), 4)
        pygame.draw.line(screen, (15, 12, 10),
                         (int(W * 0.18), int(H * 0.22)), (int(W * 0.18), H), 4)
        pygame.draw.line(screen, (15, 12, 10),
                         (int(W * 0.82), int(H * 0.22)), (int(W * 0.82), H), 4)

        # Окно
        window_w = int(W * 0.35)
        window_h = int(H * 0.55)
        window_x = int(W * 0.32)
        window_y = int(H * 0.15)
        window_rect = pygame.Rect(window_x, window_y, window_w, window_h)

        pygame.draw.rect(screen, (50, 35, 20), window_rect.inflate(16, 16))
        pygame.draw.rect(screen, DARK_BLUE, window_rect)

        pygame.draw.circle(screen, (200, 200, 180),
                           (window_x + window_w - 40, window_y + 50), 20)
        for sx, sy in [(30, 30), (80, 60), (150, 40), (200, 80), (100, 100)]:
            pygame.draw.circle(screen, (255, 255, 220),
                               (window_x + sx, window_y + sy), 2)

        pygame.draw.line(screen, (50, 35, 20),
                         [window_x + window_w // 2, window_y],
                         [window_x + window_w // 2, window_y + window_h], 6)
        pygame.draw.line(screen, (50, 35, 20),
                         [window_x, window_y + window_h // 2],
                         [window_x + window_w, window_y + window_h // 2], 6)

        # Фонарик
        if self.flashlight_on:
            light_surf = pygame.Surface((W, H), pygame.SRCALPHA)
            pygame.draw.circle(light_surf, (255, 255, 200, 100),
                               (W // 2, H // 2), 280)
            pygame.draw.circle(light_surf, (255, 255, 220, 60),
                               (W // 2, H // 2), 180)
            screen.blit(light_surf, (0, 0))

            cat_at_window = any(anim.name == 'Кот' for anim in self.animatronics)
            if cat_at_window:
                self.draw_text(self.t('cat_detected'), font_large, W // 2, H // 2, RED)
                self.draw_text(self.t('close_curtain'), font_med, W // 2, H // 2 + 80, YELLOW)
            else:
                self.draw_text(self.t('no_threat'), font_med, W // 2, H // 2, GREEN)

        # Шторка
        if self.curtain_closed or self.curtain_holding:
            pygame.draw.rect(screen, (80, 30, 30), window_rect.inflate(10, 10))
            for i in range(0, window_w, 20):
                pygame.draw.line(screen, (60, 20, 20),
                                 (window_x + i, window_y),
                                 (window_x + i, window_y + window_h), 2)
            if self.curtain_holding:
                self.draw_text(self.t('holding'), font_med, W // 2, H // 2 + 120, YELLOW)

        # Кнопка шторки
        curtain_color = (220, 50, 50) if self.curtain_closed else (150, 30, 30)
        pygame.draw.rect(screen, (70, 70, 75), [WIDTH - 230, 440, 80, 130])
        pygame.draw.rect(screen, (40, 40, 45), [WIDTH - 230, 440, 80, 130], 3)
        btn = pygame.Rect(WIDTH - 220, 460, 60, 90)
        pygame.draw.rect(screen, curtain_color, btn)
        pygame.draw.rect(screen, WHITE, btn, 2)
        self.draw_text(self.t('curtain_btn'), font_tiny, WIDTH - 190, 505, WHITE)

    def draw_tablet(self):
        pygame.draw.rect(screen, (30, 30, 30), [50, 50, WIDTH - 100, HEIGHT - 150])
        pygame.draw.rect(screen, GRAY, [50, 50, WIDTH - 100, HEIGHT - 150], 5)

        self.draw_text("КАМЕРЫ НАБЛЮДЕНИЯ", font_med, WIDTH // 2, 80, WHITE)

        for i, cam in enumerate(self.cameras):
            x = 100 + (i % 5) * 200
            y = 120 + (i // 5) * 150

            pygame.draw.rect(screen, cam.color, [x, y, 180, 130])
            pygame.draw.rect(screen, WHITE, [x, y, 180, 130], 3)

            self.draw_text(cam.name, font_small, x + 90, y + 25, WHITE)
            self.draw_text(cam.location, font_tiny, x + 90, y + 55, WHITE)

            anim_count = sum(1 for anim in self.animatronics if anim.location == cam.location)

            if anim_count > 0:
                self.draw_text(f"{anim_count} движ.", font_tiny, x + 90, y + 85, RED)
            else:
                self.draw_text("Пусто", font_tiny, x + 90, y + 85, GREEN)

            if self.current_camera == cam:
                pygame.draw.rect(screen, YELLOW, [x, y, 180, 130], 5)

    def draw_clock(self):
        hours = int(self.game_time // 60)
        minutes = int(self.game_time % 60)

        if hours == 0:
            time_str = f"12:{minutes:02d} AM"
        elif hours < 12:
            time_str = f"{hours}:{minutes:02d} AM"
        else:
            time_str = f"{hours - 12}:{minutes:02d} AM"

        clock_surf = pygame.Surface((200, 70), pygame.SRCALPHA)
        clock_surf.fill((0, 0, 0, 180))
        screen.blit(clock_surf, (WIDTH - 220, 20))

        self.draw_text(time_str, font_med, WIDTH - 120, 55, WHITE)

    def draw_controls(self):
        if not self.tablet_open and self.office_rotation < 0.5:
            pass

        tablet_color = GREEN if self.tablet_open else GRAY
        self.draw_button(self.t('camera'), WIDTH // 2 - 80, HEIGHT - 80, 160, 50, tablet_color)

        rotate_text = self.t('window') if self.office_rotation < 0.5 else self.t('back')
        self.draw_button(rotate_text, WIDTH // 2 - 220, HEIGHT - 80, 140, 50, BLUE)

    def draw_text(self, text, font, x, y, color):
        surf = font.render(text, True, color)
        rect = surf.get_rect(center=(x, y))
        screen.blit(surf, rect)

    def draw_button(self, text, x, y, w, h, color):
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, WHITE, rect, 2)
        self.draw_text(text, font_small, x + w // 2, y + h // 2, WHITE)


# Запуск
game = Game()
running = True
while running:
    dt = clock.tick(60) / 1000.0
    game.handle_events()
    game.update(dt)
    game.draw()