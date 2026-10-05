import re # regular expression == regex
from playwright.sync_api import Page, expect

def test_has_title(page:Page):
    page.goto('home')