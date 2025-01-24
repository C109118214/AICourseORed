# ch8-9: 多重繼承
class vehicle( ):
    def __init__(self, color, style):
        self.color = color
        self.style = style
    def start(self):
        return ('啟動車子')
    def driving(self):
       return ('前進車子')
    def brake(self):
        return ('停止車子')
class boat( ):
    def sailing(self):
        return ('水中航行')
class amphibious(vehicle,boat):
    pass
print('---呼叫多重繼承類別---')
obj_amp = amphibious('白色', '水陸觀光車')
print(obj_amp.color + obj_amp.style)
print('可在陸地' + str(obj_amp.driving( )) + '也可' + str(obj_amp.sailing( )))