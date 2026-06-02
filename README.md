# Homelab E2E Automated Testing Framework

An automated End-to-Edn testing framework designed for self-hosted **JellyFin** media server. This project shows QA automation practices.

Built with **Python**, **Playwright** and **PyTest**

---

## Key Features and Architecture
* **Page Object Model (POM)**: Clean separation of UI locators/actions from the actual test assertions to ensure high maintainability.
* **Environment and Secret Security**: Zero hardcoded credentials. All configuration and sensitive data are managed via decoupled environment variables (`python-dotenv`).
* **Robust Selectors**: Strictly utilizing Playwright's user-first locators (`get_by_label`, `get_by_role`) to minimize test flakiness.

---

## Project Structure

homelab-e2e-playwright/
├── pages/               # Page Object Model classes
│   ├── base_page.py     # Base wrapper for Playwright Page object
│   ├── login_page.py    # Login screen locators and actions
│   └── dashboard_page.py# Post-auth dashboard locators
├── tests/               # Test suites (Happy & Negative paths)
│   └── test_auth.py
├── conftest.py          # Global Pytest fixtures & configuration setup
├── .env.example         # Template for environment variables (safe for Git)
├── .gitignore           # Prevents uploading venv, reports, and real .env secrets
├── requirements.txt     # Locked dependencies and versions
└── README.md            # Project documentation

---

Prequisities and Setup

1. Clone the repository:
   git clone https://github.com/BlazejSzczurekk/homelab-e2e-playwright.git
   cd homelab-e2e-playwright
  
2. Set up Virtual Environment
   python -m venv venv
   #On Windows:
   .\venv\Scripts\activate
   #On Mac/Linux
   source venv/bin/activate

3. Install Dependencies
   pip install -r requirements.txt
   playwright install

4. Configure Environment Variables
   
   Create a .env file in root directory (based on .env.example)

5. Run the Tests!

   pytest [test_name.py]
