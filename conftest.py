import os
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def config():
    """Fixture zwracająca konfigurację z pliku .env"""
    url = os.getenv("JELLYFIN_URL")
    user = os.getenv("JELLYFIN_USER")
    password = os.getenv("JELLYFIN_PASSWORD")
    
    if not all([url, user, password]):
        pytest.fail("Błąd: Brakuje zmiennych środowiskowych w pliku .env! Sprawdź .env.example")
        
    return {
        "url": url,
        "user": user,
        "password": password
    }