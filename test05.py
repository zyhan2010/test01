#!/usr/bin/env Python
# coding=utf-8

from __future__ import division
import random

score = [random.randint(0,100) for i in range(40)]    #0 到 100 之间，随机得到 40 个整数，组成列表
print score

num = len(score)
sum_score = sum(score)               #对列表中的整数求和
ave_num = sum_score/num              #计算平均数
less_ave = len([i for i in score if i<ave_num])    #将小于平均数的找出来，组成新的列表，并度量该列表的长度
print "the average score is:%.1f" % ave_num
print "There are %d students less than average." % less_ave

sorted_score = sorted(score, reverse=True)    #对原列表排序
print sorted_score
