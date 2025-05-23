import Lab2.bmi as bmi

def test_bmi_under_weight():
    bmi_value, result = bmi.calculate_bmi(1.85, 50) 
    assert result == -1

def test_bmi_normal_weight():
    bmi_value, result = bmi.calculate_bmi(1.75, 60)  
    assert result == 0

def test_bmi_over_weight():
    bmi_value, result = bmi.calculate_bmi(1.65, 80)  
    assert result == 1
