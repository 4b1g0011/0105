class Game:
    # 三個遊戲類別的建構子
    def __init__(self, game_name, game_price, game_type):
        self._game_name = game_name
        self._game_price = game_price
        self._game_type = game_type

        # 直接印出當前物件的屬性
        print("遊戲名稱=", self._game_name)
        print("遊戲價格=", self._game_price)
        print("遊戲類別=", self._game_type)


# 建立 Game 物件
s1 = Game('遊戲王', '免費', '卡牌')
s2 = Game('傳說對決', '免費', '對戰')
s3 = Game('絕命精神病院', '付費', '恐怖')


# 建立 Game_name 類別
class Game_name(object):
    # 副函式定義，名稱為 method1
    def method1(self, game_name, game_price, game_type):
        # 直接回傳參數
        return game_name, game_price, game_type


# 建立 Game_name 物件
obj1 = Game_name()

# 呼叫副函式 method1
game_name = '遊戲名稱'
game_price = '遊戲價格'
game_type = '遊戲類別'
result = obj1.method1(game_name, game_price, game_type)

# 列印結果
print(result)
