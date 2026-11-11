

import pytest
from pages.blog import blog

@pytest.mark.smoke
def test_blog(page):
    blog_obj=blog(page)
    blog_obj.blog_options_clicking()
