import pygame
import os
import time
import random
pygame.font.init()


WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Goblin Slayer")
# Images
Rocket_1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Rocket 1.png")), (80, 70))
Rocket_2 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Rocket 2.png")), (80, 70))
Rocket_3 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Rocket_3.png")), (80, 70))

# PLayer
Player_Rocket = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Player Rocket.png")), (90, 90))


# Laser Beam
Red_Laser = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Red Laser.png")), (30, 80))
Purple_Laser = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Purple Laser.png")), (30, 80))
Blue_Laser = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Blue Laser.png")), (30, 80))
Yellow_Laser = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Yellow laser.png")), (30, 80))


# Backgroud
Background = pygame.transform.scale(pygame.image .load(os.path.join("assets", "Space Galaxy.png")), (WIDTH, HEIGHT))


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
       self.y += vel

    def off_screen(self, height):return not(self.y < height and self.y >= 0)
    
    def collision(self, obj):
        return collide(self, obj)         
                          

class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0


    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def take_damage(self, amount):
        self.health -= amount


    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision():
                obj.health -= 10
                self.lasers.remove(laser)
    
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()
    
    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = Player_Rocket
        self.laser_img = Yellow_Laser
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x + 30, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1 
   
    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window) 
        self.healthbar(window)    

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1             


    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))


class Enemy(Ship): 
    COLOR_MAP = {
                "red": (Rocket_1, Red_Laser),
                "purple": (Rocket_2, Purple_Laser),
                "blue": (Rocket_3, Blue_Laser)
                }
     
    def __init__(self, x, y, color, health=100):           
       super().__init__(x, y , health)
       self.ship_img, self.laser_img = self.COLOR_MAP[color]
       self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)
    
    enemies = []
    wave_length = 5
    enemy_vel = 1
    
    player_vel = 5
    laser_vel = 5


    player = Player(300, 60)
    clock = pygame.time.Clock()

    lost = False
    lost_count = 0


    def redraw_window():
        WIN.blit(Background, (0,0))
        # Draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("You Lost!", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "purple", "blue"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel > 0: # Left
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH: # right
            player.x += player_vel
        if keys[pygame.K_UP] and player.y - player_vel > 0: # up
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() < HEIGHT: # down
            player.y +=  player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()
    


        for enemy in enemies:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)
           
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)
            
            

        player.move_lasers(-laser_vel, enemies)


        redraw_window()

main()
