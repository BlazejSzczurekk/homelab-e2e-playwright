import pytest
from playwright.sync_api import expect
from pages.loginpage import LoginPage
from pages.dashboard_page import DashboardPage
from pages.movies_page import MoviesPage

@pytest.mark.parametrize("movie_title",[
    "Incepcja",
    "John Wick",
    "Lighthouse",
    "Casablanca",
    "Interstellar"
])


def test_movie_visibility(page, config, movie_title):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    movies_page = MoviesPage(page)
    
    login_page.navigate(config["url"])
    login_page.login(config["user"],config["password"])
    dashboard_page.movies_section()
    movie_locator = movies_page.get_movie_locator(movie_title)
    expect(movie_locator).to_be_visible(timeout=5000)
    
    