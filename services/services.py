from math import ceil

def get_rate_turkey(msg: float):
    if 1 <= msg <= 299:
        return ceil(msg * 4.2)
    elif 300 <= msg <= 399:
        return ceil(msg * 4.1)
    elif 400 <= msg <= 499:
        return ceil(msg * 4)
    elif 500 <= msg <= 599:
        return ceil(msg * 3.9)
    elif 600 <= msg <= 999:
        return ceil(msg * 3.8)
    else:
        return ceil(msg * 3.5)
    

def get_rate_ukraine(msg: float):
    if 1 <= msg <= 999:
        return ceil(msg * 3.3)
    elif 1000 <= msg <= 1999:
        return ceil(msg * 3.2)
    elif 2000 <= msg <= 3999:
        return ceil(msg * 3.1)
    else:
        return ceil(msg * 3)
    

def get_rate_kazah(msg: float):
    if 1 <= msg <= 999:
        return ceil(msg * 0.35)
    elif 1000 <= msg <= 9999:
        return ceil(msg * 0.29)
    elif 10000 <= msg <= 29999:
        return ceil(msg * 0.26)  
    elif 30000 <= msg <= 59999:
        return ceil(msg * 0.25)
    else:
        return ceil(msg * 0.24)