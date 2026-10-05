#US2: click on Daily standup button through First button

import re

from playwright.sync_api import Page, expect

BASE_URL = "https://lejonmanen.github.io/agile-helper/"

def test_daily_standup(page: Page):
    """Testa att det går att se Daily standup"""
    page.goto(BASE_URL)

    # Klicka på button "First"
    locator = page.get_by_role("button")
    first_button = locator.get_by_text("Första")
    first_button.click(timeout=1500)

    # Hitta button med texten "Daily standup"
    sp_button = page.get_by_role("button").get_by_text(re.compile("Daily standup"))
    expect(sp_button).to_be_visible()

    # Klicka på den
    sp_button.click(timeout=100)

    # Finns rubriken "Daily standup"?
    sp_heading = page.get_by_role("heading").get_by_text("Daily standup")
    expect(sp_heading).to_be_visible()


#US3: click on Daily standup button through Någonstans mitt i

def test_daily_standup_mitt(page: Page):
    """Testa att det går att se Daily standup från Mitt"""
    page.goto(BASE_URL)

    # Klicka på button "Någonstans i mitt"
    locator = page.get_by_role("button")
    first_button = locator.get_by_text("Någonstans")
    first_button.click(timeout=1500)

    # Hitta button med texten "Daily standup"
    sp_button = page.get_by_role("button").get_by_text(re.compile("Daily standup"))
    expect(sp_button).to_be_visible()

    # Klicka på den
    sp_button.click(timeout=100)

    # Finns rubriken "Daily standup"?
    sp_heading = page.get_by_role("heading").get_by_text("Daily standup")
    expect(sp_heading).to_be_visible()


#US4: Klicka på button från "Sista"

def test_daily_standup_sista(page: Page):
    """Testa att det går att se Daily standup från sista"""
    page.goto(BASE_URL)

    # Klicka på button "Sista"
    locator = page.get_by_role("button")
    first_button = locator.get_by_text("Sista")
    first_button.click(timeout=1500)

    # Hitta button med texten "Daily standup"
    sp_button = page.get_by_role("button").get_by_text(re.compile("Daily standup"))
    expect(sp_button).to_be_visible()

    # Klicka på den
    sp_button.click(timeout=100)

    # Finns rubriken "Daily standup"?
    sp_heading = page.get_by_role("heading").get_by_text("Daily standup")
    expect(sp_heading).to_be_visible()
