from evenodd import even_odd


def test_even():
    assert even_odd(10)=="Even"
    
def test_odd():
    assert even_odd(15)=="Odd"