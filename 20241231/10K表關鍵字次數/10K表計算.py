import fitz  # PyMuPDF
from os import listdir

PDF_file_path = "原始資料/"
file_list = listdir(PDF_file_path)

keyword = ["SALES", " REVENUE", " REVENUES", " CUSTOMER", " CUSTOMERS", " CONSUMER", " CONSUMERS", " MARKET", " MARKETS", " MARKETED", " MARKETING", " MARKETPLACE", " DISTRIBUTE", " DISTRIBUTES", " DISTRIBUTED", " DISTRIBUTING", " DISTRIBUTION", " DISTRIBUTIONS", " DISTRIBUTOR", " DISTRIBUTORS", " DISTRIBUTORSHIP", " DEALER", " DEALERS", " CLIENT", " CLIENTS", " EXPORT", " EXPORTS", " EXPORTED", " EXPORTING", " SHIPMENTS", " DEMAND", " DEMANDS", " STORE", " STORES", " WHOLESALE", " WHOLESALERS", " RECEIVABLE", " RECEIVABLES"]
country =["JAPAN", "BRITISH", "CHINA", "TAIWAN"]
word_around_text = 1000

for PDF_file_name in file_list:
    All_Page_text = ""
    
    # 打開PDF文件
    pdf_document = fitz.open(PDF_file_path + PDF_file_name)
    
    # 走訪每一頁
    for current_page in range(len(pdf_document)):
        # 取得當下的頁面
        page = pdf_document.load_page(current_page)
        
        # 提取頁面上的PDF文字
        Page_text = page.get_text().replace("\n", " ")
        All_Page_text+= " " + Page_text
    All_Page_text = All_Page_text.upper()
    
    
    for c in country:
        key_word_dict = {}
        # 初始化起始位置
        start = 0
        
        # 用來儲存所有出現的索引
        indices = []
        # 迴圈執行直到 find() 返回 -1
        while True:
            # 從目前的 start 位置尋找子字串
            index = All_Page_text.find(c, start)

            # 如果找到了子字串
            if index != -1:
                # 添加索引到列表
                indices.append(index)
                # 更新 start 位置到剛找到的子字串之後
                start = index + len(c) + word_around_text
            else:
                # 如果沒有更多子字串，跳出迴圈
                break

        for i in indices:
            start_index = i - word_around_text
            end_index = i + word_around_text
            if start_index < 0:
                start_index = 0
            if end_index > len(All_Page_text):
                end_index = len(All_Page_text)
            
            sub_text = All_Page_text[start_index : end_index]
            for k in keyword:
                times = sub_text.count(k)
                if k not in key_word_dict.keys():
                    key_word_dict[k] = 0
                else:
                    key_word_dict[k]+= times
            
        print(PDF_file_name, c )
        print(key_word_dict)
        print("=============")
        
    
        
        