import pytest

from pages.countries import countries

@pytest.mark.countries
def test_countries(page):
    countries_obj=countries(page)
    countries_obj.country_list_options()