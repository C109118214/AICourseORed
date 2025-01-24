# ch8-1: 定義汽車類別，初始化方法與屬性：顏色與樣式
class car:
# 初始化方法，當產生實體的時候這個方法會自動被呼叫
# 用self.xxx來定義實體的屬性，每個被建立的實體會有自己的屬性
    def __init__(self, color, style):
        self.color = color
        self.style = style