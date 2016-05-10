﻿'''
turtle_docstringdict_tc.py
a doc file for turtle_tc.py
'''
# 已重新手動翻譯  
# Translated automatically by Google Tranlator,
# Modified partially by Renyuan Lyu, in Taoyuan, Taiwan.
#
# renyuan.lyu@gmail.com 
# http://google.com/+RenyuanLyu
#

docsdict = {

'Turtle.back':
        '''後退，後退 一段距離。

        別名: 後退 | back | backward | bk

        參數:
        distance -- 一個數字

        往 龜指標 的反方向前進指定的距離，但不會改變龜指標 的方向。
        

        範例(物件名為「龜」的實例):

        >>> 龜.位置() # 位置 = position
        (0.00,0.00)
        >>> 龜.後退(30) # 後退 = backward
        >>> 龜.位置()
        (-30.00,0.00)

''',

'Turtle.begin_fill':
        '''開始填，開始填色，要畫一塊要被填色的形狀之前呼叫。

        沒有參數。

        範例(物件名為「龜」的實例):

        >>> 龜.顏色(黑,紅)
        >>> 龜.開始填色()
        >>> 龜.畫圓(60)
        >>> 龜.結束填色()

''',

'Turtle.begin_poly':
        '''開始多邊形，開始紀錄多邊形的頂點。

        沒有參數。

        將目前 龜指標 的位置記錄為多邊形的第一點。
        

        範例(物件名為「龜」的實例):

        >>> 龜.開始多邊形()

''',

'Turtle.circle':
        '''畫圓，給定半徑。

        參數:
        radius(半徑)  - 一個數字
        extent (圓弧角度)(可選) - 一個數字
        steps (步數)(可選) - 一個整數

        可畫指定半徑的圓，其圓心座標在 龜指標 的左方半徑單位。
        extent (圓弧角度)決定圓弧的角度範圍(完整的圓為360)。
        如沒給與該值，則自動為360。
        給予的值非完整的圓，則最後圓弧的位置即為 龜指標 位置。
        繪製圓弧時，如radius(半徑)為正時為則逆時針方​​向，
        否則以順時針方向繪製。
        而 龜指標 的方向由extent(圓弧角度)的量改變。

        由於圓形是由一個內接正多邊形所迫近而成，
        steps (步數)設定使用的正多邊形數量。
        如果沒有給予，則會自動計算。
        可用來畫標準多邊形。。

        呼叫:圓(半徑)#完整的圓
        - 或:圓(半徑,圓弧角度)#弧
        - 或:圓(半徑,圓弧角度,步數)
        - 或:圓(半徑,步數= 6)#6邊形

        範例(物件名為「龜」的實例):

        >>> 龜.畫圓(50)
        >>> 龜.畫圓(120,180) # 180度 代表 半圓

''',

'Turtle.clear':
        '''清除，清除 龜指標 在螢幕上所畫的圖，龜指標 不會移動。

        沒有參數。

        從螢幕中刪除指定的龜所畫的圖。
        龜指標 的位置和狀態以及其他 龜類 的圖，不會受到影響
        

        範例(物件名為「龜」的實例):

        >>> 龜.清除()

''',

'Turtle.clearstamp':
        '''清除蓋章，根據指定的編號清除曾經的蓋章

        參數:
        stampid  - 一個整數，必須是曾經回傳的蓋章的編號。

        範例(物件名為「龜」的實例):

        >>> 龜.顏色(藍)
        >>> 章= 龜.蓋章()
        >>> 龜.前進(50)
        >>> 龜.清除蓋章(章)

''',

'Turtle.clearstamps':
        '''清除蓋章群，清除所有或前後 n 個 龜的蓋章。

        可選參數:
        n - 一個整數

        如果 n 數字不存在，則清除全部蓋章。
        如果 n > 0 ，清除前n個。
        如果 n < 0 ，清除後n個。

        範例(物件名為「龜」的實例):

        >>>for i in 範圍(8):
        ... 龜.蓋章(); 龜.前進(30)
        ...
        >>> 龜.清除蓋章群(2)
        >>> 龜.清除蓋章群(-2)
        >>> 龜.清除蓋章群()

''',

'Turtle.clone':
        '''複製，複製產生另一隻 龜類。

        沒有參數。

        創建並回傳龜的複製品，
        與原本的龜具有相同位置、方向和設定。

        範例(物件名為「米克龜」的實例):

        米克龜= 龜類()
        喬伊龜= 米克龜.複製()

''',

'Turtle.color':
        '''顏色，回傳或設定 顏色 和 填色。

        參數：
        允許多種輸入格式。
        能使用 0~3個參數，如下所示:

        顏色()
            回傳當前的「筆色」和當前的「填色」。
            組成一對顏色字串作為回傳值。
            與 筆色() 和 填色() 2個函數呼叫後的的傳回值一樣。
        顏色(colorstring)、顏色((r,g,b))、顏色(r,g,b)
            輸入筆色，同時將給定值設定為 筆色與填色。
        顏色(colorstring1,colorstring2)、顏色((R1,G1,B1)、(R2,G2,B2))
            設定筆色(colorstring1)和填色(colorstring2)。
            也可使用其他顏色的格式設定。

        如果 龜指標 是一個多邊形(龜形、正方形等)，
        輪廓和多邊形的內部將以新設置的顏色來繪製。
        如需更多信息請參見： 筆色、填色

        範例(物件名為「龜」的實例)：

        >>> 龜.顏色(紅,綠)
        >>> 龜.顏色()
        ('red',"green")
        >>> 顏色模式(255)
        >>>顏色((40,80,120),(160,200,240))
        >>>顏色()
        ('#285078','#a0c8f0')

''',

'Turtle.degrees':
        '''角度，設定 角 的度量單位為 「度數」。

        可選參數:
        fullcircle  - 一個數字(整數或浮點數)

        設定測量角度的單位，即設定幾〝度〞為一個完整的圓。
        預設值為 360 度。
        

        範例(物件名為「龜」的實例):

        >>> 龜.左轉(90)
        >>> 龜.頭向()
        90

        可改變角的度量單位 為 grad ( 也稱作 gon、grade或 gradian)，
        定義為「直角」定為 100 grads，所以全圓定為 400 grads。
        >>> 龜.角度(400.0)
        >>> 龜.頭向()
        100


''',

'Turtle.distance':
        '''距離，回傳從龜指標本身位置 到 座標 x, y 的距離。

        參數：
        x  - 一個數字 或 數字的一對/向量 或 龜類實例
        y  - 一個數字 或 無

        呼叫: 距離(x,y)    # 兩個座標
        - 或: 距離((x,y))  # 一對(元組)
        - 或: 距離(vec)    # 與 位置() 的回傳值一樣
        - 或: 距離(mypen)  # 其中 mypen 是另一個龜

        範例(物件名為「龜」的實例):

        >>> 龜.位置()
        (0.00,0.00)
        >>> 龜.距離(30,40)
        50.0
        >>> 筆= 龜類()
        >>> 筆.前進(77)
        >>> 龜.距離(筆)
        77.0

''',

'Turtle.dot':
        '''畫點，可指定直徑大小及顏色。

        可選參數:
        size - 一個整數 >= 1(如果有設定的話)
        color - 一個 顏色字串 或 顏色的數字元組(r,g,b)

        畫一個圓點，用給定的直徑大小及顏色。
        如果直徑大小沒有給定, 就用 寬度 +4 和 2 * 寬度 中較大的值。

        範例(物件名為「龜」的實例):

        >>> 龜.畫點()
        >>> 龜.前進(50); 龜.畫點(20,藍); 龜.前進(50)

''',

'Turtle.down':
        '''下筆 - 移動時畫圖。

        別名: 下筆 | pendown | pd | down

        沒有參數。

        範例(物件名為「龜」的實例):

        >>> 龜.下筆()

''',

'Turtle.end_fill':
        '''結束填，在呼叫過 開始填() 函數後，呼叫本函數將其整個形狀填滿顏色。

        沒有參數。

        範例(物件名為「龜」的實例):

        >>> 龜.顏色(黑,紅)
        >>> 龜.開始多邊形()
        >>> 龜.畫圓(60)
        >>> 龜.結束填()

''',

'Turtle.end_poly':
        '''結束多邊形，停止記錄多邊形的頂點。

        沒有參數。

        停止記錄多邊形的頂點。
        將目前 龜指標 位置記錄為多邊形的最後一點。並與第一點相連接。

        範例(物件名為「龜」的實例):

        >>> 龜.結束多邊形()

''',

'Turtle.fillcolor':
        '''填色，回傳或設定 填色。

        參數:
        允許多種輸入格式。:
          - 填色()
            回傳當前設定的填色之顏色，
            可能是十六進制數字格式(見範例)。
            可以作為輸入到另一個 顏色/ 筆色/填色 函數的呼叫。
          - 填色(colorstring)
            colorstring 是一個 Tk 顏色字串，如 紅 或 黃。
          - 填色((r,g,b))
            一個(r,g,b)顏色元組，
            其中，每個 r,g,b 值的範圍大小在 0 .. 色模式，
            其中色模式 是 1.0 或 255(可呼叫 色模式()設定)。
          - 填色(r,g,b)
            與填色((r,g,b))一樣。

        如果 龜指標 是多邊形, 該多邊形的內部顏色用新設定的顏色來填充。

        範例(物件名為「龜」的實例)：

        >>> 龜.填色(紫)
        >>> 色= 龜.筆色()
        >>> 龜.填色(色)
        >>> 龜.填色(0,0.5,0)

''',

'Turtle.filling':
        '''是否正在填色，查看是否正在填色。

        沒有參數。

        範例(物件名為「龜」的實例)：

        >>> 龜.開始多邊形()
        >>>if 龜.正在填色():
        ...     龜.筆大小(5)
        ... else:
        ...     龜.筆大小(3)

''',

'Turtle.forward':
        '''前進，龜前進指定的距離。

        別名: 前進 | forward | fd

        參數:
        distance - 一個數字(整數或浮點數)

        龜前進指定的距離，往 龜指標 的頭之方向。

        範例(物件名為「龜」的實例)：
        
        >>> from turtle_tc import *
        >>> 龜= 龜類()
        >>> 龜.位置()
        (0.00,0.00)
        >>> 龜.前進(25)
        >>> 龜.位置()
        (25.00,0.00)
        >>> 龜.前進(-75)
        >>> 龜.位置()
        (-50.00,0.00)

''',

'Turtle.get_poly':
        '''取多邊形，回傳最近記錄的多邊形。

        沒有參數。

        範例(物件名為「龜」的實例):

        >>> 新形狀 = 龜.取多邊形()
        >>> 龜.登記形狀("最愛形狀", 新形狀)

''',

'Turtle.get_shapepoly':
        '''取形狀多邊形，回傳當前 多邊形 形狀 的 座標 元組。

        沒有參數。

        範例(物件名為「龜」的實例):

        >>> 龜.形狀("正方形")
        >>> 龜.形狀轉換(4,-1,0,2)
        >>> 龜.取形狀多邊形()
        ((50,-20),(30,20),(-50,20),(-30,-20))


''',

'Turtle.getpen':
        '''取筆，回傳 龜類 物件。

        沒有參數。

        合理的使用：作為一個函數來回傳"匿名龜"。

        例如：
        >>>寵物= 取筆()
        >>>寵物.前進(50)
        >>>寵物
        <turtle.Turtle object at 0x0187D810>
        >>>龜群()
        [<turtle.Turtle object at 0x0187D810>]

''',

'Turtle.getscreen':
        '''取幕，回傳 龜螢幕 物件，可讓 龜類 在其上面畫圖。

        沒有參數。

        回傳 龜幕類(TurtleScreen) 物件，可讓 龜類 在其上面畫圖。
        所以 龜幕類的方法可以被該物件呼叫。

        範例(物件名為「龜」的實例)：

        >>> 龜的螢幕 = 龜.取幕()
        >>> 龜的螢幕
        <turtle.TurtleScreen object at 0x0106B770>
        >>> 龜的螢幕.背景色(紅色)

''',

'Turtle.getturtle':
        '''取龜，回傳 龜物件 本身。

        沒有參數。

        合理的使用：作為一個函數來回傳 '匿名龜'。

        例如：
        >>>寵物= 取龜()
        >>>寵物.前進(50)
        >>>寵物
        <turtle.Turtle object at 0x0187D810>
        >>>龜群()
        [<turtle.Turtle object at 0x0187D810>]

''',

'Turtle.goto':
        '''前往，龜前往一個絕對位置。

        別名：前往 | 設位置 | setpos | setposition | goto:

        參數：
        x  - 一個數字  或 一對數字/向量
        y  - 一個數字  或    無

        呼叫：前往(x,y)     # 兩個座標值
        - 或：前往((x,y))   # 一個元組
        - 或：前往(vec)     # 與 位置() 回傳一樣。

        龜指標 移動到一個絕對位置。
        如果筆是下筆狀態，將畫出一條線。龜指標 的方向不會改變。

        範例(物件名為「龜」的實例)：

        >>> 所在座標 = 龜.位置()
        >>> 所在座標
        (0.00,0.00)
        >>> 龜.前往(60,30)
        >>> 龜.位置()
        (60.00,30.00)
        >>> 龜.前往((20,80))
        >>> 龜.位置()
        (20.00,80.00)
        >>> 龜.前往(所在座標)
        >>> 龜.位置()
        (0.00,0.00)

''',

'Turtle.heading':
        '''頭向，回傳當前 龜指標 的方向。

        沒有參數。

        範例(物件名為「龜」的實例)：

        >>> 龜.左轉(67)
        >>> 龜.頭向()
        67.0

''',

'Turtle.hideturtle':
        '''藏龜，把 龜指標 隱藏起來。

        別名: 藏龜 | 藏 | hideturtle | ht

        沒有參數。

        當在畫複雜的圖時，
        把 龜指標 隱藏起來是一個好主意，
        因為可加快畫圖速度。

        範例(物件名為「龜」的實例):

        >>> 龜.藏龜()

''',

'Turtle.home':
        '''回家，讓 龜指標 回到原點 - 座標(0,0)。

        沒有參數。

        讓龜回到原點 - 座標(0,0)，
        並設定其 龜指標 方向為初始狀態。

        範例(物件名為「龜」的實例)：

        >>> 龜.回家()

''',

'Turtle.isdown':
        '''下筆嗎，測試是否為下筆狀態。傳回真假值(True/False)。

        沒有參數。

        範例(物件名為「龜」的實例):

        >>> 龜.提筆()
        >>> 龜.下筆嗎()
        False
        >>> 龜.下筆()
        >>> 龜.下筆嗎()
        True

''',

'Turtle.isvisible':
        '''顯龜嗎，測試龜指標是否為可見狀態。傳回真假值(True/False)。

        沒有參數。

        範例(物件名為「龜」的實例):

        >>> 龜.藏龜()
        >>>龜.顯龜嗎()
        False

''',

'Turtle.left':
        '''左轉， 龜指標 左轉指定角度單位。

        別名: 左轉 | left | lt

        參數:
        angle - 一個數字(整數或浮點數)

        龜左轉一個角度(angle)。(單位預設為「度數」(0~360)
        但可以藉由設定 角度() 和 弳度() 來改變設置。
        角方向取決於 模式() 的設定。(請參閱...。)

        範例(物件名為「龜」的實例):

        >>> 龜.頭向()
        22.0
        >>> 龜.左轉(45)
        >>> 龜.頭向()
        67.0

''',

'Turtle.onclick':
        '''在點擊時，當此畫布的龜指標發生 點擊鼠鍵的事件 (mouse-click event) 時連結到指定函數上。

        參數:
        fun(函數) - 有 2 個參數的函數之名稱，其 2 個參數 代表 鼠鍵 點擊之位置的座標。
        num(鼠鍵號碼) - 1,2,3 代表 左、中、右鍵，預設為 1 (滑鼠左鍵)。
        add(是否加) -  真 或 假。如果為 真，新的連結函數將被加上，假 則將取消之前的連結。
                

        舉例：針對「匿名龜」，即較簡單的程序(procedural)的方式 (非物件導向型):

        >>>def 轉彎(x,y):
        ...     左轉(360)
        ...
        >>>在點擊時(轉彎) # 現在 點擊事件 與 轉彎 函數 連結在一起。
        >>>在點擊時(無) # 事件連結將被刪除

''',

'Turtle.ondrag':
        '''在拖曳時，當此畫布的龜指標發生 移動滑鼠的事件 (mouse-move event) 時連結到指定函數上。

        參數:
        fun(函數名) - 有 2 個參數的函數之名稱，其 2 個參數 代表 鼠鍵 點擊之位置的座標。
        num(鼠鍵號碼) - 1,2,3 代表 左、中、右鍵，預設為 1 (滑鼠左鍵)。

        針對 龜指標 所作的滑鼠移動事件，每一個事件序列前面都有一個點擊鼠鍵的事件。

        範例(物件名為「龜」的實例):

        >>> 龜.在拖曳時(龜.前往)

        隨後的滑鼠點擊拖拉事件會 在螢幕上 移動 龜，
        從而產生 拖曳痕跡。
        (如果目前是處於下筆狀態的話 )。

''',

'Turtle.onrelease':
        '''在鬆開時，當此畫布的龜指標發生 放開鼠鍵的事件 (mouse-button-release event) 時連結到指定函數上。

        參數:
        fun(函數名) - 有 2 個參數的函數之名稱，其 2 個參數 代表 鼠鍵 點擊之位置的座標。
        num(鼠鍵號碼) - 1,2,3 代表 左、中、右鍵，預設為 1 (滑鼠左鍵)。

        範例(物件名 為 喬伊龜 的 我的龜類 實例):
        >>>class 我的龜類(龜類):
        ...     def 發光(自己,x,y):
        ...             自己.填色(紅)
        ...     def 不發光(自己,x,y):
        ...             自己.填色("")
        ...
        >>> 喬伊龜 = 我的龜類()
        >>> 喬伊龜.在點擊時(喬伊龜.發光)
        >>> 喬伊龜.在鬆開時(喬伊龜.不發光)

        點擊 喬伊龜 讓它變成紅色, 不點擊 則變成透明的。

''',
'Turtle.pen':
        '''筆，回傳或設置筆的屬性。

        參數:
            pen(筆) - 一個 Python 字典 資料型態，記錄著下面列出的一些關鍵字。
            **筆字典  - 一個或多個 關鍵字(=參數) 的參數。記錄著下面列出的一些關鍵字。

        回傳或設置畫筆的屬性，在"筆字典"裡。
        用下面的 關鍵字/值 配對:
           "shown"      :   True/False(真/假)
           "pendown"    :   True/False(真/假)
           "pencolor"   :   顏色字串 or 顏色參數(三個數字)
           "fillcolor"  :   顏色字串 or 顏色參數(三個數字)
           "pensize"    :   正數
           "speed"      :   範圍在1~10的數字
           "resizemode" :   "auto" or "user" or "noresize"
           "stretchfactor": (正數, 正數)
           "shearfactor":   數字
           "outline"    :   正數
           "tilt"       :   數字

        這本詞典可以作為參數進行筆()的調用來恢復舊的筆狀態。
        而且可利用這些屬性當作關鍵字參數來進行設置。
        這可以用來在一個語句中設置筆的多個屬性。


        範例(物件名為「龜」的實例):

        >>> 龜.筆(填色="black", pencolor="red", pensize=10)
        >>> 龜.筆()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'red', 'pendown': True, 'fillcolor': 'black',
        'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
        >>> 筆初始=龜.筆()
        >>> 龜.顏色("yellow","")
        >>> 龜.提筆()
        >>> 龜.筆()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'yellow', 'pendown': False, 'fillcolor': '',
        'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
        >>> p.筆(筆初始, fillcolor="green")
        >>> p.筆()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'red', 'pendown': True, 'fillcolor': 'green',
        'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}

''',

'Turtle.pencolor':
        '''筆色，回傳或設定筆色。

        參數:
        允許多種輸入格式。
          -  筆色()
            回傳當前筆色顏色規範字符串，
            可能為十六進制數字格式(見範例)。
            可以作為輸入到另一個顏色/ 筆色 /填色的呼叫。
          -  筆色(colorstring)
            是一個Tk顏色規範字符串，如 紅色 或 黃色。
          -  筆色((R,G,B))
            * R,G,和B,它們代表一個RGB彩色的元組*，
            並且每個R,G,B的範圍在0 .. 色模式。
            其中 色模式 是1.0或255。(可藉由 色模式() 作設定)
          -  筆色(R,G,B)
            r,g,和b表示RGB顏色，各r的,g和b的範圍是0 .. 色模式。

        如果 龜指標 形狀是多邊形，則該多邊形的輪廓繪製為新設置的筆色。

        範例(物件名為「龜」的實例):

        >>> 龜.筆色(紅色)
        >>> 某色 =(0.2,0.8,0.55)
        >>> 龜.筆色(某色)
        >>> 龜.筆色()
        '#33cc8c"

''',

'Turtle.pendown':
        '''下筆，移動時繪製，會畫出移動軌跡。

        別名:下筆| pd | pendown

        沒有參數。

        範例(物件名為「龜」的實例):

        >>> 龜.下筆()

''',

'Turtle.pensize':
        '''筆粗(筆寬)，設置或回傳線條的粗細。

        別名:pensize | width | 筆粗 | 筆寬

        參數:
        寬度 - 正數

        設置線的粗細寬度或回傳。
        如果 重設大小模式() 設置為 "auto" 和 龜指標形狀 是一個多邊形，
        該多邊形的繪製與其為相同的線條粗細。
        如果沒有給予參數，則回傳現在的設置。

        範例(物件名為「龜」的實例):

        >>> 龜.筆粗()
        1
        >>> 龜.筆粗(10) #從現在開始以寬度為10線繪製

''',

'Turtle.penup':
        '''提筆，移動時無畫線。

        別名: 提筆 | pu | penup

        沒有參數

        範例(物件名為「龜」的實例):

        >>> 龜.提筆()

''',

'Turtle.position':
        ''' 位置，回傳 龜的當前位置(X,Y)，資料型態是Vec2D向量。

        別名: pos | position | 位置

        沒有參數。

        範例(物件名為「龜」的實例):

        >>> 龜.位置()
        (0.00,240.00)

''',

'Turtle.radians':
        '''弳度，設置角度測量單位為弧度(單位圓的弧長)。

        沒有參數。

        範例(物件名為「龜」的實例):

        >>> 龜.頭向()
        90
        >>> 龜.弳度()
        >>> 龜.頭向()
        1.5707963267948966

''',

'Turtle.reset':
        '''重設，刪除龜指標的圖和恢復其預設值。

        沒有參數。

        從螢幕中刪除 龜類 的移動軌跡，並重置 龜類。
        將其設定設為初始值(預設值)。

        範例(物件名為「龜」的實例)：

        >>> 龜.位置()
        (0.00,-22.00)
        >>> 龜.頭向()
        100.0
        >>> 龜.重設()
        >>> 龜.位置()
        (0.00,0.00)
        >>> 龜.頭向()
        0.0

''',

'Turtle.resizemode':
        ''' 重設大小模式，"auto", "user", "noresize"。

        (可選)參數:
        rmode  -  "auto", "user", "noresize"，三個字串中之一

        設置不同的模式會有不同的效果：
          - "auto"：對應 筆寬() 的值，自動調整龜形狀大小。
          - "user"：根據 形狀大小() 展延因子及輪廓大小的設置，改變龜形狀大小
          - "noresize"：自動調整為原本形狀及輪廓大小。
        無傳入參數，即可用來查詢目前設定。
        當呼叫 形狀大小() 並設置參數時，則 重設大小模式() 自動切換為"user"。


        範例(物件名為「龜」的實例)：

        >>> 龜.重設大小模式("noresize")
        >>> 龜.重設大小模式()
        "noresize"

''',

'Turtle.right':
        '''右轉，向右轉一個角度。

        別名：右轉 | rt | right

        參數:
        angle  - 一個數字(整數或浮點數)

        將 龜指標 向右轉angle角度。(單位是預設值，但可以通過度()和弳度()函數來設置。)
        角方向設定取決於 模式()。

        範例(物件名為「龜」的實例)：

        >>> 龜.頭向()
        22.0
        >>> 龜.右轉(45)
        >>> 龜.頭向()
        337.0

''',

'Turtle.setheading':
        '''設頭向，設置 龜指標 的方向。

        別名: setheading | 設頭向

        參數:
        to_angle  - 一個數字(整數或浮點數)

        根據 模式()的設定而改變度數方向及設定。
        這裡有度數一些常見的方向:

        'standard'模式   'logo'模式:
        ----------------|------------
           0  - 東      |    北
          90  - 北      |    東
         180  - 西      |    南
         270  - 南      |    西

        範例(物件名為「龜」的實例)：

        >>> 龜.設頭向(90)
        >>> 龜.頭向()
        90

''',

'Turtle.settiltangle':
        '''設傾角，旋轉 龜指標 到指定的方向。

        參數:
        angle - 數字
        旋轉 龜指標形狀 到所指定的方向。
        不會更改 龜指標 的頭向(運動方向)。


        範例(物件名為「龜」的實例)：

        >>> 龜.形狀("turtle")
        >>> 龜.形狀大小(5,2)
        >>> 龜.設傾角(45)
        >>> 蓋章()
        >>> 龜.前進(50)
        >>> 龜.設傾角(-45)
        >>> 蓋章()
        >>> 龜.前進(50)

''',

'Turtle.setundobuffer':
        '''設回復暫存區，設置或禁用回復暫存區。

        參數:
        size - 一個整數 或 無

        如果 size 是整數，則給予安裝指定大小的空白回復暫存區。
        size 決定 龜指標 使用 回復()函數的行動可撤消最大數目量。
        
        如果設定是 無，則不存在回復暫存區。

        範例(物件名為「龜」的實例)：

        >>> 龜.設回復暫存區(42)

''',

'Turtle.setx':
        '''設x座標，設置龜的 x 座標。

        參數:
        x  - 一個數字(整數或浮點數)

        將龜的第一個座標設為x，第二個座標保持不變。

        範例(物件名為「龜」的實例)：

        >>> 龜.位置()
        (0.00,240.00)
        >>> 龜.設x座標(10)
        >>> 龜.位置()
        (10.00,240.00)

''',

'Turtle.sety':
        '''設y座標，設置龜的 y 座標。

        參數:
        y  - 一個數字(整數或浮點數)

        將龜的第二個座標設為y，第一個座標保持不變。

        範例(物件名為「龜」的實例)：

        >>> 龜.位置()
        0.00,40.00)
        >>> 龜.設y座標(-10)
        >>> 龜.位置()
        ((0.00,-10.00)

''',

'Turtle.shape':
        '''形狀，根據指定形狀名稱設置龜形狀，或回傳當前形狀名稱。

        可選參數:
        name  - 一個字符串,它是一個有效的形狀名稱
        
        根據name設置 龜指標 的形狀。
        無傳入參數，即可用來查詢目前設定。
        name必須存在於 龜幕類 的形狀字典裡。
        目前有下列多邊形形狀：
        'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.
        要了解如何處理形狀，可參看 龜幕類 中的函數 登記形狀()。

        範例(物件名為「龜」的實例)：

        >>> 龜.形狀()
        'arrow'
        >>> 龜.形狀('turtle')
        >>> 龜.形狀()
        'turtle'

''',

'Turtle.shapesize':
        '''形狀大小，設置或回傳龜的 展延因子和輪廓。並設置 重設大小模式 為"user"。

        可選參數:
           stretch_wid - 正數
           stretch_len - 正數
           outline - 正數

        設置  龜指標 的展延因子跟輪廓粗細。並設置 重設大小模式() 為"user"。
        無傳入參數，即可用來查詢目前設定。
        當 重設大小模式() 被設置為" user "， 
        龜指標 將根據其展延因子的拉伸被顯示：
        stretch_wid是展延因子的垂直方向。
        stretch_len是展延因子在 龜指標 的定向方向。
        outline為形狀輪廓線的寬度。

        範例(物件名為「龜」的實例)：

        >>> 龜.重設大小模式("user")
        >>> 龜.形狀大小(5,5,12)
        >>> 龜.形狀大小(outline=8)

''',

'Turtle.shapetransform':
        '''形狀轉換，設置或回傳龜指標形狀的當前變換矩陣。

        可選參數：
		t11, t12, t21, t22 -  數字。

        如果沒有給定矩陣元素，則回傳當前變換矩陣。
        否則根據給定的矩陣元素第一行T11,T12和第二行T21,22，
		變換龜指標形狀。
        根據給定的矩陣修改 展延因子、扭曲因子和傾斜角度。

        範例(物件名為「龜」的實例)：

        >>> 龜.形狀("square")
        >>> 龜.形狀大小(4,2)
        >>> 龜.扭曲因子(-0.5)
        >>> 龜.形狀轉換()
        (4.0,-1.0,-0.0,2.0)

''',

'Turtle.shearfactor':
        '''扭曲因子，設置或回傳當前扭曲因子。

        可選參數：
        shear - 數字

        根據給定的 shear 扭曲因子剪切龜指標形狀，
        這是扭曲因子的正切值。
        不會更改 龜指標 的頭向(運動方向)。
        如果 shear 沒有被給定，則回傳當前剪切因子設定，
        即扭曲因子的正切值，通過該線平行於 龜指標方向被扭曲。

        範例(物件名為「龜」的實例)：

        >>> 龜.形狀("circle")
        >>> 龜.形狀大小(5,2)
        >>> 龜.扭曲因子(0.5)
        >>> 龜.扭曲因子()
        >>> 0.5

''',

'Turtle.showturtle':
        '''顯龜，讓 龜指標 可見。

        別名：showturtle | st | 顯龜

        沒有參數。

        範例(物件名為「龜」的實例)：

        >>> 龜.藏龜()
        >>> 龜.顯龜()

''',

'Turtle.speed':
        '''速度，回傳或設置 龜指標 的速度。

        可選參數：
        speed - 範圍為0 .. 10 或 一個速度字串(見下文)

        設定龜指標速度範圍為0 .. 10。
        如果沒有給出參數，則回傳當前速度設定。

        若輸入為大於10於或小於0.5時，
        速度被設定為0。
        速度字串被映射到速度大小，根據下面設定：
            'fastest' :  0
            'fast'    :  10
            'normal'  :  6
            'slow'    :  3
            'slowest' :  1
        速度從1至10代表執行越來越快的畫線和龜指標轉折。

        注意：
        speed= 0 代表*沒有*動畫發生。
        前進/後退 或 左/右 使龜指標瞬間跳到結果。

        範例(物件名為「龜」的實例)：

        >>> 龜.速度(3)

''',

'Turtle.stamp':
        '''蓋章，將 龜指標 的形狀拓印到畫布上，並回傳其 id 編號。

        沒有參數。

        將 龜指標 的形狀根據當前位置拓印到畫布上，
        並回傳蓋章id編號。
        可藉由其id編號使用 清除蓋章()，消除其印在畫布上的拓本。

        範例(物件名為「龜」的實例)：

        >>> 龜.顏色("藍")
        >>> 龜.蓋章()
        13
        >>> 龜.前進(50)

''',

'Turtle.tilt':
        '''傾斜，根據指定角度傾斜龜指標形狀。

        參數:
        angle - 一個數字

        將龜指標形狀目前角度再旋轉指定角度，
        不會更改 龜指標 的頭向(運動方向)。

        範例(物件名為「龜」的實例)：

        >>> 龜.形狀(""circle"")
        >>> 龜.形狀大小(5,2)
        >>> 龜.傾斜(30)
        >>> 龜.前進(50)
        >>> 龜.傾斜(30)
        >>> 龜.前進(50)

''',

'Turtle.tiltangle':
        '''傾斜角度，設置或回傳當前的傾斜角度。

        可選參數：
        angle - 數字

        旋轉龜指標形狀傾斜角度到所指定的方向，
        不管其目前的傾斜角度，
        不會更改 龜指標 的頭向(運動方向)。
        如果沒有給予參數，回傳當前的傾斜角度，
        即與該龜指標形狀的頭向方位角度差。
        

        Python 3.1 不贊成使用

        範例(物件名為「龜」的實例)：

        >>> 龜.形狀("圓")
        >>> 龜.形狀大小(5,2)
        >>> 龜.傾斜(45)
        >>> 龜.傾斜角度()

''',

'Turtle.towards':
        '''朝向，計算並回傳 龜指標 朝向 點(x,y) 的角度，亦即從 龜指標 的位置 到點(x,y) 的直線角度。

        參數:
        x  - 一個數字或數字的一對/向量或 龜類 實例
        y  - 一個數字或 無

        呼叫：朝向(x,y) #兩個座標
        - 或：朝向((x,y)) #一對元組(向量)
        - 或：朝向(VEC) #例如可以藉由 位置() 回傳的向量
        - 或：朝向(mypen) #,其中mypen是另一個 龜類

        回傳的角度為 龜指標 到該指定位置之間直線角度，
        其角度大小與其模式設定有關。(取決於 模式() - "standard"或"logo")
        

        範例(物件名為「龜」的實例)：

        >>> 龜.位置()
        (10.00,10.00)
        >>> 龜.朝向(0,0)
        225.0

''',

'Turtle.undo':
        '''回復，撤消最近的動作。

        沒有參數。

        撤消最後 龜指標 的行動。
        可撤消動作的數量是根據該回復暫存區大小來決定。
        

        範例(物件名為「龜」的實例)：

        >>>for i in 範圍(4):
        ...     龜.前進(50); 龜.左轉(80)
        ...
        >>>for i in 範圍(8):
        ...     龜.回復()
        ...

''',

'Turtle.undobufferentries':
        '''回復暫存區的個數，回傳目前回復暫存區內可撤消動作的數量。

        沒有參數。

        範例(物件名為「龜」的實例)：

        >>>while  回復暫存區的個數():
        ...     回復()

''',

'Turtle.write':
        '''寫，在當前位置寫字。

        參數:
        arg - 信息，將被寫入到 龜幕類 
        move(可選) - 真/假
        align(可選) - "left", "center" 或 right"三個字符串中一個
        font(可選) - 三個變數(字型名稱，字體大小，字體效果)

        寫信息arg的字符串表示形式，
        在當前位置 龜指標 的相對左中右(" left "," "center "或"right ")，
        並根據設定的字體寫字。
        如果move是真，則 龜指標 移動到文字的右下角。
        預設值為 假。

        範例(物件名為「龜」的實例)：

        >>> 龜.寫('首頁=', 真, align="center")
        >>> 龜.寫((0,0),真)

''',

'Turtle.xcor':
        '''x座標，回傳 龜指標 的x座標。

        沒有參數。

        範例(物件名為「龜」的實例)：

        >>>重設()
        >>>龜.左轉(60)
        >>>龜.前進(100)
        >>>龜.x座標()
        50.0

''',

'Turtle.ycor':
        '''y座標，回傳 龜指標 的y座標。
        
        沒有參數。

        範例(物件名為「龜」的實例)：

        >>>重設()
        >>>龜.左轉(60)
        >>>龜.前進(100)
        >>>龜.y座標()
        86.6025403784

''',
'_Screen.bgcolor':
        '''背景色，設置或回傳 龜幕類 的背景顏色。

        參數(可選)：
        一個顏色字串，如 紅色 或 黃色
        或在範圍0 .. 色模式的一個三元組數字

        範例(物件名為「螢幕」的實例)：

        >>> 螢幕.背景色(橙色)
        >>> 螢幕.背景色()
        "orange"
        >>> 螢幕.背景色(0.5,0,0.5)
        >>> 螢幕.背景色()
        '#800080'

''',

'_Screen.bgpic':
        '''背景圖，設置或回傳背景圖片。

        可選參數:
        picname  - 一個GIF文件名稱或"nopic"字符串。

        如果picname是一個文件名，設置相應的圖片作為背景圖。
        如果picname是"nopic"，如果背景圖存在則將其刪除。
        如果沒有picname參數，則回傳當前背景圖的文件名。

        範例(物件名為「螢幕」的實例)：

        >>> 螢幕.背景圖()
        "nopic"
        >>> 螢幕.背景圖("landscape.gif")
        >>> 螢幕.背景圖()
        "landscape.gif"

''',

'_Screen.bye':
        '''再見，關閉龜圖視窗。

        範例(物件名為「螢幕」的實例)：

        >>> 螢幕.再見()

''',

'_Screen.clearscreen':
        '''清除幕，從 龜幕類 刪除所有圖和 龜類。

        沒有參數。

        重設一個空的 龜幕類 到其初始狀態，
        白色背景、沒有背景圖片、沒有事件綁定跟追蹤。

        範例(物件名為「螢幕」的實例)：

        >>> 螢幕.清除幕()

        注意：這個方法不作函數使用。

''',

'_Screen.colormode':
        '''色模式，回傳色模式設定或將其設置為 1.0 或 255。

        可選參數:
        cmode  - 數字 1.0 或 255 中之一

         r, g, b 值必須在範圍0 .. cmode之間。

        範例：

        >>> 色模式()
        1.0
        >>> 色模式(255)
        >>> 筆色(240,160,80)

''',

'_Screen.delay':
        '''延遲，回傳或設置畫面更新的延遲時間，以毫秒為單位。

        可選參數:
        delay - 正整數

        範例(物件名為「螢幕」的實例)：

        >>> 螢幕.延遲(15)
        >>> 螢幕.延遲()
        15

''',

'_Screen.exitonclick':
        '''在點擊時離開，進入主​​迴圈，直到鼠標點擊關閉視窗。

        沒有參數。

        在龜幕類點擊鼠標時綁定 再見() 函數。
        如果"using_IDLE" - 在配置詞典值為 假(默認值)，
        並進入主循環。
        如果在-n模式下的IDLE(無子程式)時 - 
        在 turtle.cfg 值設置為 真。
        在這種情況下，客戶端腳本的IDLE進行主循環。

        這是Screen-class的函數，在 龜幕類 沒有可用的實例。

        範例：

        >>> 在點擊時離開()


''',

'_Screen.getcanvas':
        '''取畫布，回傳一個在 龜幕類 上的 畫布 物件。

        沒有參數。

        範例(物件名為「螢幕」的實例)：

        >>> 畫布 = 螢幕.取畫布()
        >>>畫布
        <龜.ScrolledCanvas instance at 0x010742D8>

''',

'_Screen.getshapes':
        '''取形，取形狀列表，回傳所有當前可用的 龜指標 形狀名稱列表。

        沒有參數。

        範例(物件名為「螢幕」的實例)：

        >>> 螢幕.取形()
        ['arrow', 'blank', 'circle', ... , 'turtle']

''',

'_Screen.listen':
        '''聽，設置聚焦於  龜幕類 之上(為了收集鍵盤事件)。

        沒有參數。
        偽參數為了提供要能夠通過監聽點擊函數。

        範例(物件名為「螢幕」的實例)：

        >>> 螢幕.聽()

''',

'_Screen.mainloop':
        '''主迴圈，進入主迴圈啟動事件循環 - 呼叫 Tkinter的主迴圈函數。

        沒有參數。

        必須是龜畫圖程式的最後一條語句。
        程式不得使用運行在IDLE 內部 -n 模式
        (無子程式) - 亦即在龜畫圖程式互動模式下。

        範例(物件名為「螢幕」的實例)：

        >>> 螢幕.主迴圈()


''',

'_Screen.mode':
        '''模式，設置龜模式('standard', 'logo' or 'world')，並執行 重設()。

        可選參數:
        mode - 'standard' (角度從東開始逆時針)、'logo' (角度從北開始順時針)或 'world' (世界)，三個中之一。

        角度從東開始逆時針('standard')模式，
        龜指標 角度從東開始逆時針算，與turtle.py相容。
        角度從北開始順時針('logo')模式，
        龜指標 角度從東開始順時針算，與原始的logo龜圖相容。
        世界(' world ')模式，
        使用用戶自定義"worldcoordinates"。
        *注意*:如果x / y的單位比不等於1，在世界模式下角度會出現扭曲。
        無傳入參數，即可用來查詢目前設定。

             模式            初始龜指標頭向           角度方向
         ------------ | ------------------------- | ------------------
          'standard'    向右(東)               逆時針
            'logo'      向上(北)               順時針

        範例：
        >>>模式(角度從北開始順時針) # 重設龜指標向北
        >>>模式()
        'logo'

''',

'_Screen.numinput':
        '''輸入數字，彈出一個對話窗口，可以輸入一個數字。

        參數：
        title: 對話框窗口的標題。
        prompt: 提示語，主要是描述需要的輸入文本信息。
        default: 預設值。
        minval: 最小值。
        maxval: 最大值。

        如果最小值跟最大值參數有設定，數字輸入必須在範圍 minval .. maxval。
        如果取消該對話框，則回傳 無(None)。

        範例(物件名為「螢幕」的實例)：

        >>> 螢幕.輸入數字("撲克","你的賭注:",1000,minval=10, maxval=10000)


''',

'_Screen.onkey':
        '''在按鍵時，連結函數 於 鍵盤鍵鬆開事件。

        參數：
        fun - 不帶參數的函數
        key - 一個字串：文字鍵(如"a") 或 符號鍵(如"空白鍵")

        為了能註冊所有鍵盤事件，
        所以龜幕類必須進行監聽事件。可參看 聽() 函數。

        範例(物件名為「螢幕」的實例)：


        >>> def 畫():
        ...     前進(50)
        ...     左轉(60)
        ...
        >>> 螢幕.在按鍵時(畫, 向上鍵)
        >>> 螢幕.聽()

        上面這段程式碼，讓使用者可以藉由重複按 向上鍵 ，
        來畫出一個六邊形。


''',

'_Screen.onkeypress':
        '''在按著鍵時，如果有指定鍵的話，連結函數 於 單一鍵盤鍵按下事件；
        如果沒有指定鍵的話，則連結任何按鍵事件。

        參數：
        fun - 不帶參數的函數
        key - 一個字串：文字鍵(如"a") 或 符號鍵(如"空白鍵")

        為了能註冊所有鍵盤事件，
        所以龜幕類必須進行監聽事件。可參看 聽() 函數。

        範例(物件名為「螢幕」的實例)：



        >>> def 畫():
        ...     前進(50)
        ...     左轉(60)
        ...
        >>> 螢幕.在按著鍵時(畫, 向上鍵)
        >>> 螢幕.聽()

        上面這段程式碼，讓使用者可以藉由重複按 向上鍵 ，
        來畫出一個六邊形。


''',

'_Screen.onkeyrelease':
        '''在按鍵鬆開時，連結函數 於 鍵盤鍵鬆開事件。

        參數：
        fun - 不帶參數的函數
        key - 一個字串：文字鍵(如"a") 或 符號鍵(如"空白鍵")

        為了能註冊所有鍵盤事件，
        所以龜幕類必須進行監聽事件。可參看 聽() 函數。

        範例(物件名為「螢幕」的實例):


        >>> def 畫():
        ...     前進(50)
        ...     左轉(60)
        ...
        >>> 螢幕.在按鍵鬆開時(畫, 向上鍵)
        >>> 螢幕.聽()

        上面這段程式碼，讓使用者可以藉由重複按 向上鍵 ，
        來畫出一個六邊形。


''',

'_Screen.onscreenclick':
        '''在點擊幕時，連結函數 於 畫布上 點擊鼠標的事件。

        參數：
        fun - 有兩個參數 x , y
               代表在畫布上滑鼠點擊的點座標。
        num - 數字預設為1，1,2,3分別代表滑鼠左、中、右鍵。

        舉例(名為「螢幕」的 龜幕類 的實例)：

        >>> 螢幕.在點擊幕時(前往)
        >>> 螢幕.在點擊幕時(無) # 解除連結

''',

'_Screen.ontimer':
        '''在計時後，安裝計時器，t毫秒後呼叫函數。

        參數：
        fun - 不帶參數的函數。
        t - 一個數 > = 0

        範例(物件名為「螢幕」的實例)：


        >>> 正在執行 = 真
        >>> def 畫():
        ...     if 正在執行:
        ...             前進(50)
        ...             左轉(60)
        ...             螢幕.在計時後(畫, 250)
        ...
        >>> 畫()   # 讓 龜類 運行
        >>> 正在執行 = 假

''',

'_Screen.register_shape':
        '''登記形狀，添加一個 龜指標 形狀到 龜幕類 的 形狀列表。

        參數:
        (1)name是一個GIF文件的檔案名而形狀是None。
            安裝相應的圖像形狀。
            ！轉彎時,圖像形狀不會旋轉。
            ！所以也不會顯示龜指標方向。
        (2)name為一個任意的字串，
            形狀是一個元組(tuple)的座標(一對數字)。
            設定相應的多邊形。
        (3)name為一個任意的字串，
            形狀是(複合的) 形狀 物件。
            設定相應的複合形狀。
        要使用登記的形狀，必須呼叫 形狀(name) 指令。

        呼叫:登記形狀("龜.gif")
        - 或者:登記形狀("三角形",((0,0),(10,10),(-10,10)))

        範例(物件名為「螢幕」的實例)：

        >>> 螢幕.登記形狀("三角形",((5,-3),(0,5),(-5,-3)))


''',

'_Screen.resetscreen':
        '''重設幕，重設螢幕上的所有 龜類 為其初始狀態。

        沒有參數。

        範例(物件名為「螢幕」的實例)：

        >>> 螢幕.重設幕()

''',

'_Screen.screensize':
        '''幕大小，重設畫布大小。

        可選參數:
        canvwidth  - 正整數，畫布以像素為單位的寬度
        canvheight  - 正整數，畫布以像素為單位的高度
        bg  -  顏色字串或顏色元組，新的背景顏色
        如果沒有傳入參數，回傳目前設定值(canvaswidth,canvasheight)。

        不要改變繪圖視窗。
        在畫布上使用滾動條可查看被隱蔽部位。
        (可以見到畫布外的動作！)

        範例(物件名為「龜」的實例)：

        >>> 龜.幕大小(2000,1500)
        >>>#例如：可尋找一個犯錯逃脫的龜;-)

''',

'_Screen.setup':
        '''設立，設主視窗的大小和位置。

        參數:
        width： 若為整數就是以像素為單位，若為浮動數則是在螢幕的百分比。
          預設值為螢幕的50%。
        height：若為整數就是以像素為單位，若為浮動數則是在螢幕的百分比。
          預設值為螢幕的75%。
        startx： 如為正數，從左邊螢幕的邊緣開始算位置，
          如為負數，從右邊螢幕的邊緣開始算位置，
          預設情況下，startx = 無 是水平居中。
        starty： 如為正數，從上邊螢幕的邊緣開始算位置，
          如為負數，從下邊螢幕的邊緣開始算位置，
          預設情況下，starty = 無 是垂直居中。

        範例(物件名為「螢幕」的實例)：

        >>> 螢幕.設立(width=200, height=200, startx=0, starty=0)

        設主視窗，寬高為 200×200 像素，在螢幕的左上角位置。

        >>> 螢幕.設立(width=.75, height=0.5, startx=None, starty=None)

        設主視窗的寬高為螢幕寬高的75%及50%。

''',

'_Screen.setworldcoordinates':
        '''設座標系統，設置一個使用者定義的座標系。

        參數：
        llx -- 畫布的左下角x座標
        lly -- 畫布的左下角y座標
        urx -- 畫布的右上角x座標
        ury -- 畫布的右上角y座標

        設置使用者定義座標系統，並在必要時切換到'world'(世界)模式。
        並執行一個螢幕重置。
        如果'world'(世界)模式已經啟動，則所有圖都會根據新的座標系重畫。

        但要注意：在使用者定義的座標系中，角度可能會出現扭曲。(參考 模式())

        範例(物件名為「螢幕」的實例)：

        >>> 螢幕.設座標系統(-10, -0.5, 50, 1.5)
        >>> for _ in 範圍(36):
        ...     左轉(10)
        ...     前進(0.5)

''',

'_Screen.textinput':
        '''輸入文字，彈出一個對話窗，讓使用者輸入一個字串。

        參數：
        title：對話框窗口的標題。
        prompt：提示語，主要是描述需要的輸入文本信息。
        當有傳入參數，則回傳輸入的字串。
        如果取消該對話框，回傳 無(None)。

        範例(物件名為「螢幕」的實例)：

        >>> 螢幕.輸入文字("NIM","第一個球員的名字:")


''',

'_Screen.title':
        '''設標題，設置龜視窗的標題。

        參數:
        titlestring  - 一個字串，出現在龜視窗的標題。


        這是螢幕類的方法。不適用於 龜幕類 物件。

        範例(物件名為「螢幕」的實例)：

        >>> 螢幕.設標題("歡迎來到龜動物園！")

''',

'_Screen.tracer':
        '''追蹤，開/關 龜動畫，並設置更新畫面的延遲時間。

        可選參數:
        n - 非負整數
        dekay - 非負整數

        如果 n 有被指定的，只執行每n次定期螢幕更新。
        (可用於加速複雜圖形的繪製。)
        第二個參數設置延遲值(見 RawTurtle.delay() )

        範例(物件名為「螢幕」的實例)：


        >>>螢幕.追蹤(8,25)
        >>>距離= 2
        >>>for i in 範圍(200):
        ...     前進(距離)
        ...     右轉(90)
        ...     距離 += 2

''',

'_Screen.turtles':
        '''龜群，回傳螢幕上龜列表。

        範例(物件名為「螢幕」的實例)：


        >>> 螢幕.龜群()
        [<turtle.Turtle object at 0x00E11FB0>]

''',

'_Screen.update':
        '''更新，執行 龜幕類 更新。

''',

'_Screen.window_height':
        '''取幕高，回傳龜視窗的高度。

        範例(物件名為「螢幕」的實例)：


        >>> 螢幕.取幕高()
        480

''',

'_Screen.window_width':
        '''取幕寬，回傳龜視窗的寬度。

        範例(物件名為「螢幕」的實例)：


        >>> 螢幕.取幕寬()
        640

'''

}
# ver01, by Renyuan, 2014/03/16 01:49 am