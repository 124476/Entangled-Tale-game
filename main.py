import os
import random

import pygame
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class Player(pygame.sprite.Sprite):
    image = load_image('m.c.front_stop.jpg')
    image = pygame.transform.scale(image, (40, 60))

    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = Player.image
        self.rect = self.image.get_rect().move(
            pos_x, pos_y)
        self.x = pos_x + 20
        self.y = pos_y + 60
        self.step = 1
        self.back = False
        self.last_skin_change_time = 0
        self.direction = ''
        self.mask = pygame.mask.from_surface(self.image)
        self.loc = 0

    def stop(self):
        image = self.image
        if self.direction == 'left':
            image = load_image(f'm.c.left_stop.jpg')
        elif self.direction == 'right':
            image = load_image(f'm.c.right_stop.jpg')
        elif self.direction == 'down':
            image = load_image(f'm.c.front_stop.jpg')
        elif self.direction == 'up':
            image = load_image(f'm.c.back_stop.jpg')
        self.image = pygame.transform.scale(image, (40, 60))


class PlayerAct1(Player):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)

    def update(self, move_up, move_down, move_left, move_right):
        global all_sprites, background, player, player_group, door_group, door, slova_group, x, y
        image = self.image
        current_time = pygame.time.get_ticks()
        if move_left:
            self.direction = 'left'
            self.rect.x -= 6
            self.x -= 6
            if background.get_rgb(self.x, self.y) == (2, 0, 0):
                self.rect.x += 6
                self.x += 6
            if current_time - self.last_skin_change_time > 150:
                self.last_skin_change_time = current_time
                if self.step == 1:
                    self.step += 1
                    self.back = False
                elif self.step == 2:
                    if self.back:
                        self.step -= 1
                    else:
                        self.step += 1
                elif self.step == 3:
                    self.step -= 1
                    self.back = True

            image = load_image(f'm.c.left_walk_{self.step}.jpg')
        if move_right:
            self.direction = 'right'
            self.rect.x += 6
            self.x += 6
            if background.get_rgb(self.x, self.y) == (2, 0, 0):
                self.rect.x -= 6
                self.x -= 6
            if current_time - self.last_skin_change_time > 150:
                self.last_skin_change_time = current_time
                if self.step == 1:
                    self.step += 1
                    self.back = False
                elif self.step == 2:
                    if self.back:
                        self.step -= 1
                    else:
                        self.step += 1
                elif self.step == 3:
                    self.step -= 1
                    self.back = True

            image = load_image(f'm.c.right_walk_{self.step}.jpg')
        if move_up:
            self.direction = 'up'
            self.rect.y -= 6
            self.y -= 6
            if background.get_rgb(self.x, self.y) == (2, 0, 0):
                self.rect.y += 6
                self.y += 6
            if current_time - self.last_skin_change_time > 150:
                self.last_skin_change_time = current_time
                if self.step == 1:
                    self.step += 1
                    self.back = False
                elif self.step == 2:
                    if self.back:
                        self.step -= 1
                    else:
                        self.step += 1
                elif self.step == 3:
                    self.step -= 1
                    self.back = True

            image = load_image(f'm.c.back_walk_{self.step}.jpg')
        if move_down:
            self.direction = 'down'
            self.rect.y += 6
            self.y += 6
            if background.get_rgb(self.x, self.y) == (2, 0, 0):
                self.rect.y -= 6
                self.y -= 6
            if current_time - self.last_skin_change_time > 150:
                self.last_skin_change_time = current_time
                if self.step == 1:
                    self.step += 1
                    self.back = False
                elif self.step == 2:
                    if self.back:
                        self.step -= 1
                    else:
                        self.step += 1
                elif self.step == 3:
                    self.step -= 1
                    self.back = True

            image = load_image(f'm.c.front_walk_{self.step}.jpg')
        self.image = pygame.transform.scale(image, (40, 60))
        if pygame.sprite.collide_mask(self, door):
            if self.loc == 0:
                all_sprites = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                door_group = pygame.sprite.Group()
                background = Background('a1_m2.png', (600, 1300))
                all_sprites.add(background)
                player = PlayerAct1(285, 950)
                player.loc = 1
                wizardRus.rect.x = 285
                wizardRus.rect.y = 600
                wizardRus.canRun = False
                wizardRus.y = 600
                all_sprites.add(wizardRus)
                door = Door(260, 100)
            elif self.loc == 1:
                all_sprites = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                slova_group = pygame.sprite.Group()
                door_group = pygame.sprite.Group()
                background = Background('a1_m3.jpg', (2100, 500))
                all_sprites.add(background)
                door = Door(1900, 200)
                player = PlayerAct1(450, 200)
                player.loc = 2
            elif self.loc == 2:
                all_sprites = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                background = Background('a1_m4.jpg', (700, 500))
                all_sprites.add(background)
                player = PlayerAct1(375, 300)
                player.loc = 3
                mathGame()
                x = player.x
                y = player.y

        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)


class Letters(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        a = random.choice(['letter_a.png', 'letter_b.png', 'letter_v.png',
                           'letter_g.png', 'letter_d.png'])
        image_path = load_image(a)
        self.image = pygame.transform.scale(image_path, (40, 60))
        self.rect = self.image.get_rect().move(pos_x, pos_y)

    def update(self):
        self.rect.x -= 8
        if pygame.sprite.collide_mask(self, player):
            act1()
            return


def newDialog():
    font = pygame.font.Font(None, 30)
    t1 = font.render('', True, (255, 255, 255))
    t2 = font.render('', True, (255, 255, 255))
    t3 = font.render('', True, (255, 255, 255))
    return t1, t2, t3


def mathGame():
    global background, all_sprites, player_group, player, door, door_group, ball_group, rectangle_group, horizontal_borders, vertical_borders
    fon = pygame.transform.scale(load_image('a1_m4.jpg'), (800, 500))
    screen.blit(fon, (0, 0))

    n1 = random.randint(0, 100)
    n3 = random.randint(0, 9)
    n2 = n3 - n1
    m = 'Я великий маг этого подземелья,'
    m2 = 'и я никому не дам ходить по нему'
    m3 = 'без моего разрешения!'
    screen.fill((0, 0, 0))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    t1, t2, t3 = newDialog()

    win = False
    i = 1
    a = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and a == 0:
                    screen.fill((0, 0, 0))
                    screen.blit(fon, (0, 0))
                    if n2 < 0:
                        m1 = f"{n1}{n2}"
                    else:
                        m1 = f"{n1}+{n2}"
                    m = 'Но ты можешь попытать удачу,'
                    m2 = 'и решить мою задачу'
                    m3 = 'сколько будет: ' + m1
                    t1, t2, t3 = newDialog()
                    i = 1
                    a = 1
                elif 48 <= event.key <= 58 and a == 1:
                    m = event.key - 48
                    t1, t2, t3 = newDialog()
                    if m == n3:
                        screen.fill((0, 0, 0))
                        screen.blit(fon, (0, 0))
                        m = 'Я вижу, что ты силен в математике'
                        m2 = 'на этот раз я тебя пропукаю,'
                        m3 = 'но мы еще встретимся!'
                        win = True
                    else:
                        screen.fill((0, 0, 0))
                        screen.blit(fon, (0, 0))
                        m = 'Я вижу, что ты слаб,'
                        m2 = 'возвращайся,'
                        m3 = 'лишь когда будешь достоен'
                    i = 1
                    a = 2
                elif event.key == pygame.K_z and a == 2:
                    if win:
                        all_sprites = pygame.sprite.Group()
                        player_group = pygame.sprite.Group()
                        ball_group = pygame.sprite.Group()
                        rectangle_group = pygame.sprite.Group()
                        background = Background('a1_m5.jpg', (900, 500))
                        all_sprites.add(background)
                        player = PlayerAct1(450, 300)
                        player.loc = 4
                        horizontal_borders = pygame.sprite.Group()
                        vertical_borders = pygame.sprite.Group()
                        Border(0, 0, 800, 0)
                        Border(0, 480, 880, 480)
                        Border(0, 0, 0, 480)
                        Border(880, 0, 880, 480)
                        camera.update(player)
                        door = Door(20000, 20000)
                        for sprite in all_sprites:
                            camera.apply(sprite)
                        return
                    else:
                        act1()
                        return

        if i <= len(m):
            t1 = font.render(m[:i], True, (255, 255, 255))
        elif i <= len(m) + len(m2):
            t2 = font.render(m2[:i - len(m)], True, (255, 255, 255))
        elif i <= len(m) + len(m2) + len(m3):
            t3 = font.render(m3[:i - len(m) - len(m2)], True, (255, 255, 255))
        i += 1
        screen.blit(t1, (230, 85))
        screen.blit(t2, (230, 115))
        screen.blit(t3, (230, 145))
        player_group.draw(screen)
        pygame.display.flip()
        clock.tick(20)
        clock.tick(FPS)


def ball(x, y):
    Ball(20, x, y, -1, 1)
    Ball(20, x, y, 1, 1)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_path, size):
        super().__init__()
        self.image = load_image(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()

    def get_rgb(self, x, y):
        pixel = pygame.PixelArray(self.image)
        return self.image.unmap_rgb(pixel[x][y])


clock = pygame.time.Clock()
FPS = 60


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    fon = pygame.transform.scale(load_image('fon.jpg'), (800, 500))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    clock.tick(0.7)
    fon = pygame.transform.scale(load_image('blackfon.png'), (800, 500))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif (event.type == pygame.KEYDOWN or event.type ==
                  pygame.MOUSEBUTTONDOWN):
                if True:
                    act1()
                    return
        clock.tick(FPS)


class Door(pygame.sprite.Sprite):
    image_path = load_image('exit-enter_a1.png')
    image_path = pygame.transform.scale(image_path, (120, 96))
    sprite_image = image_path

    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.image = Door.sprite_image
        self.rect = self.image.get_rect().move(pos_x, pos_y + 20)
        self.mask = pygame.mask.from_surface(self.image)


# группы спрайтов
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
rectangle_group = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
ball_group = pygame.sprite.Group()

x, y = 0, 0


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, vx, vy):
        super().__init__(ball_group, all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = vx
        self.vy = vy

    def update(self):
        global rectangle_group, ball_group
        self.rect.x += 3 * self.vx
        self.rect.y += 3 * self.vy
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx

        if pygame.sprite.collide_mask(self, player):
            for j in rectangle_group:
                j.rect.x = 10000

            for j in ball_group:
                j.rect.x = 10000
            rectangle_group = pygame.sprite.Group()
            ball_group = pygame.sprite.Group()
            act1()
            return


class Rectangle(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, vx, vy, xx, yy):
        image_path = load_image('rect.jpg')
        image_path = pygame.transform.scale(image_path, (xx, yy))
        sprite_image = image_path
        super().__init__(rectangle_group, all_sprites)
        self.image = sprite_image
        self.rect = self.image.get_rect().move(pos_x, pos_y + 20)
        self.mask = pygame.mask.from_surface(self.image)
        self.vx = vx
        self.vy = vy

    def update(self):
        global rectangle_group, ball_group
        self.rect.x += 3 * self.vx
        self.rect.y += 3 * self.vy
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.rect.x = 10000
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.rect.x = 10000

        if pygame.sprite.collide_mask(self, player):
            for j in rectangle_group:
                j.rect.x = 10000

            for j in ball_group:
                j.rect.x = 10000

            rectangle_group = pygame.sprite.Group()
            ball_group = pygame.sprite.Group()
            act1()
            return


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class wizardRus(pygame.sprite.Sprite):
    image = load_image('wizardRus.jpg')
    image = pygame.transform.scale(image, (80, 90))

    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.image = wizardRus.image
        self.rect = self.image.get_rect().move(
            pos_x, pos_y)
        self.canRun = False
        self.y = pos_y

    def update(self):
        if self.canRun:
            self.rect.y -= 10
            self.y -= 10
            if self.y <= 300:
                self.rect.y = -1000
        if player.y <= 800:
            self.canRun = True


wizardRus = wizardRus(2000, 2000)


def act1():
    global all_sprites, player_group, player, background, door, door_group
    fon = pygame.transform.scale(load_image('act1.png'), (800, 500))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    clock.tick(1)
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    door_group = pygame.sprite.Group()
    background = Background('a1_m1.png', (1360, 760))
    door = Door(1180, 440)
    all_sprites.add(background)
    door_group.add(door)
    player = PlayerAct1(290, 470)


def act2():
    fon = pygame.transform.scale(load_image('act2.png'), (800, 500))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    clock.tick(1)


def act3():
    fon = pygame.transform.scale(load_image('act3.png'), (800, 500))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    clock.tick(1)


def menu():
    fon = pygame.transform.scale(load_image('Menu.png'), (800, 500))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    act1()
                    return
                if event.key == pygame.K_2:
                    act2()
                    return
                if event.key == pygame.K_3:
                    act3()
                    return
                if event.key == pygame.K_p:
                    return

        clock.tick(FPS)


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


camera = Camera()
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Entangled Tale')
    size = width, height = 800, 500
    screen = pygame.display.set_mode(size)
    start_screen()

    i = 0

    slova_group = pygame.sprite.Group()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    menu()
            if event.type == pygame.KEYUP:
                player.stop()
        keys = pygame.key.get_pressed()

        screen.fill((2, 0, 0))
        # Обновление игровых объектов
        player.update(keys[pygame.K_UP], keys[pygame.K_DOWN],
                      keys[pygame.K_LEFT], keys[pygame.K_RIGHT])
        player.update(keys[pygame.K_w], keys[pygame.K_s],
                      keys[pygame.K_a], keys[pygame.K_d])
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)
        camera.update(player)
        wizardRus.update()
        all_sprites.draw(screen)
        player_group.draw(screen)
        if player.loc == 2:
            i += 1
            if i % 25 == 0:
                letter = Letters(1500, random.randint(200, 300))
                slova_group.add(letter)
            slova_group.update()
            slova_group.draw(screen)
        if player.loc == 4:
            if 100 <= i <= 1000 and i % 100 == 0:
                ball(x - player.x + 300, y - player.y - 50)
            if i == 2000:
                for j in ball_group:
                    j.rect.x = 10000
            if 2000 <= i <= 3000 and i % 100 == 0:
                Rectangle(x - player.x - 50, y - player.y - 10, 1, 0, 10, random.randint(200, 380))
                Rectangle(x - player.x + 800, y - player.y + random.randint(-10, 100), -1, 0, 10,
                          random.randint(100, 200))
            if 3000 <= i <= 3900 and i % 100 == 0:
                ball(x - player.x + 300, y - player.y - 50)
            if i == 4000:
                for j in ball_group:
                    j.rect.x = 10000
            i += 1

            rectangle_group.update()
            ball_group.update()
        door_group.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)
