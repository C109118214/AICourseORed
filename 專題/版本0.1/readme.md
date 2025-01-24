![image](https://github.com/user-attachments/assets/1cedb44a-2146-4e71-96b2-21fa4da00739)
K線表格.py
```python
def onclick(self):
    stock_id = self.lineEdit.text()  # 獲取用戶輸入的幣種代號
    from Draw_plot import main as dp
    
    df = dp(stock_id, "1h", 30)  # 調用主函數
    if df is None:
        self.label_2.setText("無效的幣種代號或無法獲取資料")
        self.label.setPixmap(QtGui.QPixmap("起始圖.png"))
        self.tableWidget.clear()
        return
    
    # 替換成畫好的圖
    self.label.setPixmap(QtGui.QPixmap(f"{stock_id}_Kbar.png"))
    
    # 用 df 的 shape 資訊，讓 tableWidget 繪製相同大小的表格
    self.tableWidget.setColumnCount(df.shape[1])
    self.tableWidget.setRowCount(df.shape[0])

    _translate = QtCore.QCoreApplication.translate
    count = 0
    for i in df.index:
        # 建構列的物件
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(count, item)
        
        # 設定列的名稱
        item = self.tableWidget.verticalHeaderItem(count)
        item.setText(_translate("MainWindow", str(i)))
        count += 1

    count = 0
    for c in df.columns:
        # 建構欄的物件
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(count, item)
        
        # 設定欄的名稱
        item = self.tableWidget.horizontalHeaderItem(count)
        item.setText(_translate("MainWindow", c))
        count += 1

    index_count = 0
    for index, row in df.iterrows():
        columns_count = 0
        for c in df.columns:
            # 建構儲存格的物件
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(index_count, columns_count, item)
            
            # 設定儲存格的內容
            item = self.tableWidget.item(index_count, columns_count)
            text = str(df.at[index, c])
            item.setText(_translate("MainWindow", text))
            columns_count += 1
        index_count += 1

```
