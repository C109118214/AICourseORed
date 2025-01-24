# -*- coding: utf-8 -*-
#https://www.pythoncharts.com/matplotlib/radar-charts/

# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def main(labels, values):
    plt.rcParams.update({'font.size': 20})
    
    font_path = "mingliu.ttc"	#中文字型路徑
    font_prop = fm.FontProperties(fname=font_path)		#調整字型
    
    # 項目標題
    #labels = ['Acceleration', 'Displacement', 'Horsepower', 'MPG', 'Weight']
    # 有幾個項目
    num_vars = len(labels)
    # 雷達圖各個項目角度
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    # 將第一個角度放到最後，這樣圖形才會閉鎖
    angles.append(angles[0])
    # 設定圖表的大小與座標軸
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    
    # 將資料放入圖表
    def add_to_radar(label, color):
      #values = [10,20,30,40,50] # 加入資料
      values.append(values[0]) #在最後加入第一筆資料，讓圖形閉合
      
      ax.plot(angles, values, color=color, linewidth=1, label=label)
      ax.fill(angles, values, color=color, alpha=0.25)
    
    # Add each car to the chart.
    add_to_radar('score', '#1aaf6c')
    #add_to_radar('peugeot 504 1979', '#429bf4')
    #add_to_radar('ford granada 1977', '#d42cea')
    
    # Fix axis to go in the right order and start at 12 o'clock.
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    
    # 將標籤名稱加上第一筆資料配合圖表閉合
    labels.append(labels[0])
    # 設定
    ax.set_thetagrids(np.degrees(angles), labels, fontproperties=font_prop)
    
    # 根據角度調整圖表項目標籤的位置
    for label, angle in zip(ax.get_xticklabels(), angles):
      if angle in (0, np.pi):
        label.set_horizontalalignment('center')
      elif 0 < angle < np.pi:
        label.set_horizontalalignment('left')
      else:
        label.set_horizontalalignment('right')
    
    # 設定數值的上下限
    ax.set_ylim(0, 10)
    
    # 將Y數值的數值標籤，置中在第一與第二個項目之間
    ax.set_rlabel_position(180 / num_vars)
    
    # Add title.
    ax.set_title('各項指標分數雷達圖', y=1.08, fontproperties = font_prop)
    
    # Add a legend as well.
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    
    return fig

if __name__ == "__main__":
   labels = ['自有資本率', "速動比率", "淨利率", "A", "B"]
   values = [2.6, 8.5, 8.6, 5 ,6]
   fig =  main(labels, values)
   fig.show()
   