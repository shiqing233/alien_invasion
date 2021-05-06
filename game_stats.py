class GameStats():
    """跟踪游戏统计信息"""
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #游戏一开始处于不活跃状态
        self.game_active = False
        
    def reset_stats(self):
        """初始化在游戏运行期间信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
