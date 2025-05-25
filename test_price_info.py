import price_info

def test_total_cost_shopping():
    expected = 46.75
    result = price_info.total_cost_shopping()
    assert (result == expected)

def test_cost_of_fruit():  
    result = price_info.cost_of_fruits('pear',5)
    expected = 0.9 * 5
    assert (result == expected)