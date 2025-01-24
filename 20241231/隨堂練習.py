# -*- coding: utf-8 -*-
# =============================================================================
# 有一個字串
# Str_1 = "NKUST is Good School"
# 請完成以下要求
# 1. 將School更換成University
# 2. 根據空格將文字分割成串列(list)
# 3. 以print輸出串列中的Good
# 4. 用"!"將串列合併成一個字串
# =============================================================================
Str_1 = "NKUST is Good School"
Str_1 = Str_1.replace("School", "University")
Str_list = Str_1.split(" ")
print(Str_list[2])
merge_list = "!".join(Str_list)