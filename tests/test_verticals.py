


import pytest

from pages.verticals import vertical

@pytest.mark.smoke
def test_trading(page):
    trading_obj=vertical(page)
    trading_obj.trading_options_clicking()

@pytest.mark.smoke
def test_rande(page):
    rande_obj=vertical(page)
    rande_obj.rande_options_clicking()

@pytest.mark.smoke
def test_healthcare(page):
    health_obj=vertical(page)
    health_obj.healthcare_options_clicking()

@pytest.mark.smoke
def test_fintech(page):
    fintech_obj=vertical(page)
    fintech_obj.fintech_options_clicking()

@pytest.mark.smoke
def test_customapp(page):
    customapp_obj=vertical(page)
    customapp_obj.customapp_options_clicking()