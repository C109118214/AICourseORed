#  ch8-17: 作業系統錯誤
print('---檔案不存在錯誤---')
du = open('lee.txt', 'r')
# du = open('Dufu.txt', 'r')
print(du.read( ))
print('---允許錯誤---')
# du = open('D:/temp', 'r')