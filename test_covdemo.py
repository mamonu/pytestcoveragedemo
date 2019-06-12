import covdemo
import pytest

print(dir(covdemo))


def test_no_letters():
    assert(covdemo.howmanyletters('')=="no data")


def test_less_than_3_letters():
    assert(covdemo.howmanyletters('NO')=="less than three letters!?")

def test_more_than_or_3_letters():
    assert(covdemo.howmanyletters('lol :)')==['lol',':)'])
