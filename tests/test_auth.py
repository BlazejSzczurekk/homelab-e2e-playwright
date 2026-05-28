from pages.loginpage import LoginPage
from pages.dashboard_page import DashboardPage
from playwright.sync_api import expect

def test_succesful_login(page,config):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    login_page.navigate(config["url"])
    login_page.login(config["user"],config["password"])
    
    expect(dashboard_page.start_button).to_be_visible(timeout=3000)
    
def test_failed_login(page,config):
    login_page = LoginPage(page)
    login_page.navigate(config["url"])
    login_page.login("bledny_user","bledne_haslo")
    expect(login_page.error_message).to_be_visible(timeout=500)
    
      
    