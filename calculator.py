#!/usr/bin/env python3

import sys

if __name__=='__main__':
    a = (float(sys.argv[1]))*(1-(0.08+0.02+0.005+0.06))-3500.00
    b = (float(sys.argv[1]))*(1-(0.08+0.02+0.005+0.06))
    if a<=0:
        ss=0
    elif a<=1500:
        ss=a*0.03
    elif a<=4500:
        ss=a*0.1-105
    elif a<=9000:
        ss=a*0.2-555
    elif a<=35000:
        ss=a*0.25-1005
    elif a<=55000:
        ss=a*0.3-2755
    elif a<=80000:
        ss=a*0.35-5505
    elif a>80000:
        ss=a*0.45-13505
    else:
        print("Parameter Error")
    gongzi= b-ss
    print('%.2f'%gongzi)