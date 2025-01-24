# -*- coding: utf-8 -*-
target = 1000000 # 目標
annual_salary = 45000 * 12 # 年收入
annual_cost = 30000 * 12  # 年花費
salary_growth_rate = 0.05 # 薪資成長率
cost_growth_rate = 0.02 # 花費成長率
interest_rate = 0.01 # 存款或投資利率

deposit = 0 # 存款
year_count = 0 # 存了幾年

# 當存款不達目標，就繼續存錢
while deposit < target:
    year_count+= 1
    # 年初存入的存款
    deposit += annual_salary - annual_cost
    
    # 進行複利與成長
    annual_salary *= (1 + salary_growth_rate)
    annual_cost *= (1 + cost_growth_rate)
    deposit *= (1 + interest_rate)

print(year_count)