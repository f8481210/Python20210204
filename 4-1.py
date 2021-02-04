print('########################')
print('#Python蘋果店進出貨系統#')
print('########################')
sell = 0  
cus = []  
while True:
    print('功能=>')
    print('1. 設定')
    print('2. 進貨')
    print('3. 出貨')
    print('4. 營業額統計')
    print('5. 庫存顯示')
    print('6. 結束系統')
    
    op = int(input('請輸入功能選項：'))
    if op == 6:
        break
    elif op == 1: #選擇功能1
        number = int(input('輸入蘋果數量：'))
        price = int(input('蘋果單價：'))
        print('蘋果目前有',number, '顆')
        print('蘋果一顆', price, '元')
    
    elif op == 2: #選擇功能2
        applein = int(input('蘋果進貨數量：'))
        number = applein + number #number 蘋果總數量
        print('蘋果目前有',number, '顆')
        
    elif op == 3: #選擇功能3
        appleout = int(input('蘋果賣出數量：'))
        print('應付', appleout * price, '元')
        number = number - appleout #總數量
        sell = sell + appleout #sell 賣出蘋果數
        print('蘋果目前有',number, '顆')
        cus.append(appleout) #記錄一位客人買了幾顆蘋果
        
    elif op == 4: #選擇功能4
        for i in range(len(cus)): #len(cus) 幾位客人
            print(cus[i],'顆',cus[i] * price,'元')
        total = sell * price #total 總共賺多少錢
        print('共賣了',sell, '顆')
        print('營業額',total,'元')
        
    elif op == 5: #選擇功能5
        print('蘋果目前有',number, '顆')
    else:
        print('ERROR')