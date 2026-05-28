from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.get_by_role("textbox", name="Użytkownik")
        self.password_input = page.get_by_role("textbox", name="Hasło")
        self.login_button = page.get_by_role("button", name="Zaloguj się")
        self.error_message = page.get_by_text("Nieprawidłowa nazwa użytkownika lub hasło. Spróbuj ponownie.")
     
    def login(self,username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()   