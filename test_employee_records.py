import employee_records as emp
def test_get_employees_by_age_range():
    expected = [    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    ]
    result = emp.get_employees_by_age_range(23,35)
    assert (result == expected)
def test_calculate_average_salary():
    result = emp.calculate_average_salary()
    expected = (50000 + 60000 + 65000 + 56000 + 70000 + 60000)/6
    exp_rounded = round(expected,3)
    assert (result == exp_rounded)
def test_get_employees_by_dept():
    result = emp.get_employees_by_dept("Engineering")
    expected = [    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    assert (result == expected)