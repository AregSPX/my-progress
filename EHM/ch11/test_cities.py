from city_functions import location

def test_city_country():
    """whether code works with city-country pair"""
    x = location('santiago', 'chile')
    assert x == 'Santiago, Chile'

def test_city_country_population():
    """whether code works with city-country-population"""
    y = location('santiago', 'chile', 5000000)
    assert y == 'Santiago, Chile - population 5000000'