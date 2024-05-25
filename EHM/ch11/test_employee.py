import pytest
from employee import Employee

@pytest.fixture
def x_for_all():
    x = Employee('Areg', 'Sargsyan', 16000)
    return x



def test_give_default_d(x):
    x.give_raise()
    assert x.w == 21000
    
def test_give_custom_d(x):
    x.give_raise(1000)
    assert x.w == 17000