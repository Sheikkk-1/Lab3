import Lab2.bmi as bmi
def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.8, 50) 
    assert result[1] == -1

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.7, 60)  
    assert result[1] == 0

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.6, 80)  
    assert result[1] == 1
    