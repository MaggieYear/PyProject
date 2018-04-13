#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

class KeyWords:
    """用来保存关键字和对应发言的模块"""

    def __init__(self):
        self.key_word = {1: ("狗子", "柴狗"), 2: ("狸花猫", "布偶猫"), 3: ("麻辣鸡爪", "泡椒鸡爪")}
        self.index = random.randint(1,len(self.key_word))
        self.key_content = {}
        self.key_content[1] = [("四条腿","会走的","人们都很喜欢","被用来称呼人","别人的男朋友","接地气的动物","耳朵竖起来","毛茸茸","贼可爱"),("很好几种颜色","讨人喜欢","不太粘人","会看家护院","喜欢散步","喜欢同伴玩")]
        self.key_content[2] = [("毛茸茸","有尾巴",'比较活泼','不太粘人','喜欢自己玩','爪子肉肉的','喜欢吃鱼','喜欢捉蝴蝶','好动','长得很匀称','很机灵'),("很多毛","经常掉毛",'粘人','喜欢吃肉','耳朵立起来','喜欢睡觉','长得很好看')]
        self.key_content[3] = [("辣的","吃起来有点麻烦",'吃了头皮发麻','吃完会长痘','某种动物的脚','很好吃','吃完一飞冲天'),('吃到出汗','很刺激','后劲很足','适合追剧的时候吃','肠胃不好的人不适合吃')]

    #返回一个随机的关键字组合
    def randomKeyWord(self):
        # 生成一个随机的关键字组合
        key_index = random.randint(1,2)
        return self.key_word[key_index]

    def getKeyContent(self,keyWord_index):
        contents =  self.key_content[keyWord_index]
        return contents

if __name__ == '__main__':
    key_word = KeyWords()
    key_words = key_word.randomKeyWord()
    contents = key_word.getKeyContent(key_word.index)
    print '关键字组合：' + str(key_words)
    print '关键字答复：' + str(contents)


