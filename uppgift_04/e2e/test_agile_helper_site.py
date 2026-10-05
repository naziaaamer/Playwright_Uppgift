from playwright.sync_api import Page, expect
from environment import BASE_URL

def test_page_title(page: Page):
    page.goto(BASE_URL)
    page.wait_for_timeout(1000)

    title = page.get_by_text("Agile Helper")
    expect(title).to_be_visible()