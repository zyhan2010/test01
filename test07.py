#! /usr/bin/nev python
#coding:utf-8

syudent=['zhangsan','lisi','wangwu',['hansi','zhengzhou','shangqiu',['suixian','hutang']],'baige']

for lgd in syudent:
    if isinstance(lgd,list):
        for lgd1 in lgd:
            if isinstance(lgd1,list):
                for lgd2 in lgd1:
                    print lgd2
            else:
                print lgd1
    else:
        print lgd

