from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.menu_button = page.get_by_role("button", name="Menu")
        self.start_button = page.get_by_role("button", name="Start")
        