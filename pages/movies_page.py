from pages.base_page import BasePage

class MoviesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
    
    def get_movie_locator(self, movie_title:str):
        return self.page.get_by_text(movie_title, exact=True)