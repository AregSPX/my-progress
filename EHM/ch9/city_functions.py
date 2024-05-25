def location(city, country, population = ''):
    if population:
        L = f'{city.title()}, {country.title()} - population {population}'
    else:
        L = f'{city.title()}, {country.title()}'
    return L 