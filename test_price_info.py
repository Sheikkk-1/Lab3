import price_info

def test_total_cost_shopping():
    total_cost = 0
    for key in price_info.price_list:
        if key in price_info.quantity_list:
            total_cost += price_info.price_list[key] * price_info.quantity_list[key]
    
    assert total_cost == (
        5 * 1.20 + 5 * 1.40 + 1 * 6.50 + 2 * 2.70 +
        10 * 0.90 + 1 * 2.95 + 2 * 4.95
    )

def test_cost_of_fruits():
    fruit = 'apple'
    quantity = 10
    calculated_cost = 1.20 * 10
    actual_cost = price_info.price_list[fruit] * quantity
    assert calculated_cost == actual_cost