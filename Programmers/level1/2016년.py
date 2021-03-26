# 2016년

from datetime import date

def solution(a, b):
    day=date(2016,a,b).strftime('%a').upper()
    
    return day