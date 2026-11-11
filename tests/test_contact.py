import pytest

from pages.contact import contact

def test_contact(page):
    contact_object=contact(page)
    contact_object.contact_options_clicking()