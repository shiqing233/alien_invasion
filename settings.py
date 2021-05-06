class Settings():
    """用于存储游戏的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1050
        self.screen_height = 750
        self.bg_color = (0,255,100)

        #飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed = 1
        self.bullets_allowed = 5

        #外星人设置
        self.alien_speed = 5
        self.fleet_drop_speed  = 20
        self.fleet_direction = 1

        #加快游戏节奏
        self.speedup_scale = 1.1**3

        #boss设置
        self.boss_speed = 8
        self.HP = 50

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.alien_points = 50
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 1
        self.fleet_direction = 1

        self.boss_speed = 8
        self.HP = 50

    def increase_speed(self):
        """提高速度"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.boss_speed *= self.speedup_scale
        self.HP *= self.speedup_scale
