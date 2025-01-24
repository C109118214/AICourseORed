# E_8_3: 類別中不同方法的呼叫方式

# 車票訂單
class Ticket_order:
    # 定義固定的屬性，類別定義好的時候就有這個屬性了
    Adult_price = 500 # 成人票價屬性
    Child_price = 300 # 孩童票價屬性

    # 建構式
    def __init__(self, Ticket_type, num):
        self.Ticket_type = Ticket_type # 票種
        self.num = num # 張數
        
# =============================================================================
#     # 實體方法，更改類別的變數，之後創造的類別都是以此變數為準
#     def change_price(self):
#         self.__class__.Adult_price = 450
#         self.__class__.Child_price = 250
# ===============================================================================
    
    # 用類別方法更動設類別中的內容，創造的類別都是以此變數為準
    @classmethod 
    def change_price(cls):
        cls.Adult_price = 450
        cls.Child_price = 250
    
    
    # 類別方法，針對的對象為Class，可以用來建構不同的class
    # 概念為在設計圖中加入設計建議，用特定的參數建構物件
    @classmethod # 類別方法一定要有此標註
    def Adult_method(cls):
        return cls("Adult", 0)
    
    @classmethod # 類別方法一定要有此標註
    def Child_method(cls):
        return cls("Child", 0)
    
    # 靜態方法
    @staticmethod
    def show_result(T_type, price, num):
        if T_type == "Adult":
            show_type_txt = "成人"
            total = price * num
        else:
            show_type_txt = "孩童"
            total = price * num
        return "%d張%s票，總共%d元" % (num, show_type_txt, total)

a = Ticket_order.Adult_method() # 用類別方法建構物件
print(a.Adult_price, a.Child_price)
print(a.num, a.Ticket_type)

# 更改票價
Ticket_order.change_price()


print(a.Adult_price, a.Child_price)
b = Ticket_order.Adult_method()
print(b.Adult_price, b.Child_price)

print(a.num)
a.num = 2 # 更改物件屬性
print(a.num)

# 根據物件的票種屬性(Ticket_type)，調用靜態方法印出結果
if a.Ticket_type == "Adult":
    print(a.show_result(a.Ticket_type, a.Adult_price, a.num))
else:
    print(a.show_result(a.Ticket_type, a.Child_price, a.num))



# ------------------------

b = Ticket_order.Child_method() # 用類別方法建構物件
b.num = 3  # 更改物件屬性

# 根據物件的票種屬性(Ticket_type)，調用類別方法印出結果
if b.Ticket_type == "Adult":
    print(b.show_result(b.Ticket_type, b.Adult_price, b.num))
else:
    print(b.show_result(b.Ticket_type, b.Child_price, b.num))

# 靜態方法不用建構物件也可以直接使用
print(Ticket_order.show_result("Child", 100, 4))

