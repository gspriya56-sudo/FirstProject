import pytest
from playwright.sync_api import Page, expect


def test_login(page:Page):   

        page.goto("https://bstackdemo.com/")
        page.click('#signin')
        page.get_by_text("Select Username").click()
        page.locator("#react-select-2-option-0-0").click()
        page.get_by_text("Select Password").click()
        page.locator("#react-select-3-option-0-0").click()
        page.get_by_role("button", name="Log In").click()
        assert page.get_by_text("demouser").is_visible()
    