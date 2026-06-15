import pytest

from pages.dashboard.dashboard_page import DashboardPage
from pages.authentification.registration_page import RegistrationPage


@pytest.mark.registration
@pytest.mark.regression
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.registration_form.fill(email="user@gmail.com", password="password", username="username")
    registration_page.registration_form.check_visible(email="user@gmail.com", password="password", username="username")
    registration_page.click_registration_button()
    dashboard_page.dashboard_toolbar_view.check_visible()
