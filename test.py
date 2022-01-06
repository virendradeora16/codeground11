from conversion.currency import Currency
def test_usd():
    c1=Currency("USD")
    result = c1.get_money_after_purchase( "$200", "$49.21")
    assert 'Total change: $150.79' == result

def test_usd2():
    c1=Currency("USD")
    result = c1.get_money_after_purchase( "$100", "$50")
    assert 'Total change: $50.0' == result
