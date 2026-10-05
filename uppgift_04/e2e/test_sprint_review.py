#US5
import re

from playwright.sync_api import Page, expect

BASE_URL = "https://lejonmanen.github.io/agile-helper/"

def test_sprint_review(page: Page):
    # open web page
    page.goto(BASE_URL)

    # click on "sista" button
    locator = page.get_by_role("button")
    sista_button = locator.get_by_text("Sista")
    sista_button.click(timeout=1500)

    #find the button with text "sprint review"
    sr_button = page.get_by_role("button").get_by_text("Sprint review")
    expect(sr_button).to_be_visible()

    #click the button
    sr_button.click(timeout=1500)

    #sprint review text is visible
    sr_heading = page.get_by_role("heading").get_by_text("Sprint review")
    expect(sr_heading).to_be_visible()
