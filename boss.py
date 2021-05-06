import pygame

class Boss():
    """创建boss类"""
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/boss.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self,rect)
        
    def update(self):
        self.x += (self.ai_settings.boss_speed * self.ai_settings.fleet_direction)
        self.rect.x = self.x
