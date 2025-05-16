import employee_info

def test_calculate_average_salary():
    for item in employee_info.employee_data:
        actual_average = employee_info.calculate_average_salary()
        calculated_average =   (50000 + 60000 + 56000 + 70000 + 65000 + 60000) / 6
        for item in employee_info.employee_data:
            assert actual_average == calculated_average

def test_get_employees_by_age_range():
    age_lower_limit = 20
    age_upper_limit = 40 
    result = employee_info.get_employees_by_age_range(age_lower_limit, age_upper_limit)
    expected = [item for item in employee_info.employee_data 
                if age_lower_limit < item["age"] < age_upper_limit]
    assert result == expected

def test_get_employees_by_dept():
    department = "Engineering"
    expected = [{"name": "Chloe", "age": 35, "department": "Engineering", "salary": 70000},
                {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    result = employee_info.get_employees_by_dept(department)
    
    assert result == expected


    