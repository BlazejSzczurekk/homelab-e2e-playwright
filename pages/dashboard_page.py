from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.menu_button = page.get_by_role("button", name="Menu")
        self.start_button = page.get_by_role("button", name="Start")
        self.movies_button = page.get_by_role("link", name="Filmy", description="Filmy", exact=True)
        self.logout_button = page.get_by_role("link", name="Wyloguj się")
    def movies_section(self):
        self.movies_button.click()
        
    def logout(self):
        self.menu_button.click()
        self.logout_button.click()    