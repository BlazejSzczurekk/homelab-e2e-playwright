from playwright.sync_api import expect
from pages.loginpage import LoginPage
from pages.dashboard_page import DashboardPage
import pytest

def test_user_logout(page, config):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    
    login_page.navigate(config["url"])
    login_page.login(config["user"],config["password"])
    dashboard_page.logout()
    expect(login_page.username_input).to_be_visible
