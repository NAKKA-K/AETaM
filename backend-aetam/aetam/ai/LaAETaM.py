# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:16:20 2018
@author: 鳥井
"""
import MeCab
import json

class LaAETaM:
    def __init__(self,string):
        self.text = string
        self.seikaku = {"serious" : 0, "hot" : 0, "strong" : 0, "kind" : 0}
        self.seikaku2 = ("kind","strong","hot","serious")
        self.hinsi = ("連体詞*","接頭詞形容詞接続","接頭詞数接続","接頭詞動詞接続","接頭詞名詞接続","名詞引用文字列","名詞サ変接続","名詞ナイ形容詞語幹","名詞形容動詞語幹","名詞動詞非自立的","名詞副詞可能","名詞一般","名詞数","名詞接続詞的","名詞固有名詞","名詞接尾","名詞代名詞","名詞非自立","名詞特殊","動詞自立","動詞接尾","動詞非自立","形容詞自立","形容詞接尾","形容詞非自立","副詞一般","副詞助詞類接続","接続詞*","助詞格助詞","助詞係助詞","助詞終助詞","助詞接続助詞","助詞特殊","助詞副詞化","助詞副助詞","助詞副助詞／並立助詞／終助詞","助詞並立助詞","助詞連体化","助動詞*","感動詞*","記号句点","記号読点","記号空白","記号アルファベット","記号一般","記号括弧開","記号括弧閉","フィラー*","その他間投","未知語*",)
        #0:null,1:plus,2:minus
        self.point = (100,1,1200,10,1000,1201,0000,1000,1001,121,1200,0000,1200,1200,0000,1001,100,2020,2020,0,1000,1,100,2000,1000,2000,1021,1220,1201,0,110,1021,2020,1020,1,12,2021,111,0000,1,1200,1200,1002,1202,2000,200,200,2121,21,2110)

    def execute(self):
        tagger = MeCab.Tagger('-Ochasen')
        tagger.parse('')
        print(type(self.text), isinstance(self.text, str))
        if not isinstance(self.text, str):
            self.text = self.text.encode('utf-8')
        result = tagger.parseToNode(self.text)
        print("\n", self.text)
        while result:
            print("feature: ", result.feature, "\tsurface: ",  result.surface)
            for x in range(0,50):
                if ((result.feature.split(',')[0])+(result.feature.split(',')[1])) == self.hinsi[x]:
                    for i in range(4,0,-1):
                        if int((self.point[x] % 10**i)/10**(i-1)) == 1:
                            self.seikaku[self.seikaku2[i-1]] += 1
                        elif int((self.point[x] % 10**i)/10**(i-1)) == 2:
                            self.seikaku[self.seikaku2[i-1]] -= 1

            result = result.next

        return self.seikaku

#a = LaAETaM("こんにちは")
#a.execute()
