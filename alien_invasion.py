import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from boss import Boss

def run_game():
    #初始化并创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("超级无敌宇宙第一炫酷爆炸超帅巨屌大型网络游戏——大哥之战")

    #创建按钮
    play_button = Button(ai_settings,screen,"PLAY")
    #创建一架飞船
    ship = Ship(ai_settings,screen)
    #创建用于存储子弹的编组
    bullets = Group()
    #创建一个外星人
    alien = Alien(ai_settings,screen)
    #创建外星人编组
    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #创建一个用于统计的实例
    stats = GameStats(ai_settings)
    #创建记分牌
    sb = Scoreboard(ai_settings,screen,stats)
    #创建一个boss
    boss = Boss(ai_settings,screen)
    
    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,
            aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()
