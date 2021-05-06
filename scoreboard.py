import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """显示得分信息的类"""

    def __init__(self,ai_settings,screen,stats):
        """初始化显示得分涉及属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #显示得分信息时使用的字体
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #准备初始得分图像
        self.prep_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """得分转换成图像"""
        score_str = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,
                self.ai_settings.bg_color)

        #得分放在右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """显示得分"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)

    def prep_level(self):
        """等级转换成图像"""
        self.level_image = self.font.render(str(self.stats.level),True,
                    self.text_color,self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """显示还有多少飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings,self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
