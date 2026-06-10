from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_button = page.get_by_test_id("registration-form-email-input").locator("input")
    email_button.fill("user.name@gmail.com")
    username_button = page.get_by_test_id("registration-form-username-input").locator("input")
    username_button.fill("username")
    password_button = page.locator("[type='password']")
    password_button.fill("password")

    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    dashboard_header = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashboard_header).to_be_visible()
