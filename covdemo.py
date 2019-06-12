import pytest



def howmanyletters(input):
    if len(input)<1:
        output="no data"
    elif len(input)< 3:
        output="less than three letters!?"
    else: 
        output=str(input).split(' ')
    return output




