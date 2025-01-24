import matplotlib.font_manager as fm

# 列出所有可用字型的名稱和路徑
font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')

# 列出字型名稱
font_names = [fm.FontProperties(fname=font).get_name() for font in font_list]

# 印出所有字型名稱
for name in font_names:
    print(name)
