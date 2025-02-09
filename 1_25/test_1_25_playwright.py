import pytest
import playwright


@pytest.fixture
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context =browser.new_context(viewport={"width":1920,"height":1080})
        page = context.new_page()
        yield  page
        page.close()
        browser.close()
        context.close()

# import re
#
# from playwright.sync_api import Playwright, sync_playwright, expect
#
#
# def test_run(page) -> None:
#
#     page.goto("https://mail.ru/")
#     page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
#     page.get_by_role("button", name="Закрыть").click()
#     page.get_by_role("link", name="Москва").first.click()
#     with page.expect_popup() as page1_info:
#         page.get_by_role("link", name="Снежный покров в Москве может достигнуть 10 см к 23").click()
#     page1 = page1_info.value
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(page) -> None:
    page.goto("https://mail.ru/")
    page.locator(".geomap-tooltip__icon-close").click()
    page.locator("iframe[name=\"\\31 739866124315\"]").content_frame.get_by_role("option", name="мтс банк").click()
    with page.expect_popup() as page1_info:
        page.locator("iframe").content_frame.get_by_role("link", name="МТС Банк — Кредиты, кредитные карты, вклады").click()
    page1 = page1_info.value
    page1.get_by_role("link", name="Карты", exact=True).click()
    page1.get_by_role("link", name="Кредитная карта МТС Деньги").first.click()
    page1.get_by_role("button", name="Оформить карту", exact=True).click()
    page1.get_by_role("button", name="Оформить карту", exact=True).click()
    page1.get_by_role("tab", name="Требования к заемщику").click()