import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """对子弹进行管理的类"""
    def __init__(self,ai_settings,screen,ship):
        """飞船处创建一个子弹对象"""
        super(Bullet,self).__init__()
        self.screen = screen

        #0,0处创建一个子弹，再设置正确位置
        self.image = pygame.image.load('images/bullet.bmp')
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #存储用小数表示子弹位置
        self.y = float(self.rect.y)

        self.speed = ai_settings.bullet_speed

    def update(self):
        """向上移动子弹"""
        #更新子弹位置的小数值
        self.y -= self.speed
        #更新表示子弹的rect位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        self.screen.blit(self.image,self.rect)
        
