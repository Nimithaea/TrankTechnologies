import pytest

from pages.technologies import technologies

@pytest.mark.smoke
def test_ecomm(page):
    ecomm_obj=technologies(page)
    ecomm_obj.tech_ecomm_options_clicking()

@pytest.mark.smoke
def test_mobappdev(page):
    mobapp_obj=technologies(page)
    mobapp_obj.mobapp_dev_options_clicking()
