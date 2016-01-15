#!/usr/bin/env python
#coding=gbk

def fib(n):
    print "n=", n
    if n > 1: 
        return n * fib(n-1)
    else:
        print "end of line"
        return 1


if __name__ == '__main__':
    num = raw_input('请输入阶乘最后位数字:')
    num = int(num) if int(num) > 0 else 1
    print fib(num)
