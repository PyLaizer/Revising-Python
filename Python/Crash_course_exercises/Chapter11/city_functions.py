#Exercise 11.1 and 11.2

def city_info(city,country,population=''):
    """Returns a city name and its country"""
    result = f"{city}, {country}-population {population}"
    return result.title()

# print(city_info("Lagos","Nigeria",150_000_000))    