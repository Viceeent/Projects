from calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_divide_by_zero():
    calc = Calculator()
    assert calc.divide(10, 0) is None
def test_subtract():
    calc = Calculator()
    assert calc.subtract(2, 3) == -1
def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
def test_power():
    calc = Calculator()
    assert calc.power(2, 3) == 8
def test_modulus():
    calc = Calculator()
    assert calc.modulus(2, 3) == 2
def test_floordivision():
    calc = Calculator()
    assert calc.floordivision(10, 2) == 5
def test_floordivisionbyzero():
    calc = Calculator()
    assert calc.floordivision(2, 0) is None
def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
def test_history_records_result():
    calc = Calculator()
    calc.add(2, 3)
    assert calc.history == [5]
def test_clear_history():
    calc = Calculator()
    calc.clear_history()
    assert calc.history == []
