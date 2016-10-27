#!/usr/bin/env Python
# coding=utf-8

string = "I     love code."    #在 code 前面有两个空格，应该删除一个
print string                #为了能够清楚看到每步的结果，把过程中的量打印出来

str_lst = string.split(" ")    #以空格为分割，得到词汇的列表
print str_lst

words = [s for s in str_lst if s!=""]    #去除单词两边的空格
print words

new_string = " ".join(words)    #以空格为连接符，将单词链接起来
print new_string