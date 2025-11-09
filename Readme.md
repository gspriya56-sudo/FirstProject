# First_Project_Python — Playwright + Python test automation

Short README describing project layout and steps to run Playwright tests with Python.

## Project
- Repository: UI test automation using Playwright (Python).
- Typical layout:
    - README.md
    - requirements.txt
    - tests/                 # pytest tests, e.g. tests/test_login.py
    - playwright_tests/      # optional library helpers, fixtures
    - conftest.py            # pytest fixtures (page, browser setup)

## Prerequisites
- Python 3.8+ installed
- Git (optional)
- Node is NOT required for Playwright Python (binaries installed by Playwright tool)
- Recommended: use a virtual environment

## Setup (local)
1. Create and activate a venv
     - macOS / Linux
         - python -m venv .venv
         - source .venv/bin/activate
     - Windows (PowerShell)
         - python -m venv .venv
         - .\.venv\Scripts\Activate.ps1

2. Install dependencies
     - Create a simple requirements.txt (example):
         ```
         pytest
         playwright
         pytest-asyncio         # if you use async tests
         pytest-html            # optional: HTML report
         ```
     - Install:
         - pip install -r requirements.txt

3. Install Playwright browser binaries
     - python -m playwright install
     - (Optional) install specific browser drivers:
         - python -m playwright install chromium
         - python -m playwright install firefox
         - python -m playwright install webkit

## Running tests
- Run all tests:
    - pytest tests/
- Run a single test file:
    - pytest tests/test_example.py
- Run a single test function:
    - pytest tests/test_example.py::test_my_case

- Headed (show browser) vs headless
    - By default tests are headless. To run headed, either:
        - Configure the browser launch in your fixtures to use headless=False; or
        - Export an environment variable your fixtures read (example: PLAYHEADLESS=0) and set headless accordingly.
    - Example (POSIX) to run headed if your fixtures read PLAYHEADLESS:
        - PLAYHEADLESS=0 pytest tests/

- Generate HTML report (requires pytest-html)
    - pytest tests/ --html=report.html --self-contained-html

## Example conftest.py (minimal)
- Provide a fixture that creates a Playwright browser and page (synchronous example):
    ```
    import pytest
    from playwright.sync_api import sync_playwright

    @pytest.fixture(scope="session")
    def browser_context():
            with sync_playwright() as p:
                    browser = p.chromium.launch(headless=True)
                    context = browser.new_context()
                    yield context
                    context.close()
                    browser.close()

    @pytest.fixture
    def page(browser_context):
            page = browser_context.new_page()
            yield page
            page.close()
    ```

## CI example (GitHub Actions)
- Minimal workflow steps:
    ```
    jobs:
        test:
            runs-on: ubuntu-latest
            steps:
                - uses: actions/checkout@v4
                - name: Setup Python
                    uses: actions/setup-python@v4
                    with:
                        python-version: '3.11'
                - name: Install deps
                    run: |
                        python -m venv .venv
                        source .venv/bin/activate
                        pip install -r requirements.txt
                        python -m playwright install
                - name: Run tests
                    run: |
                        source .venv/bin/activate
                        pytest tests/ --junitxml=results.xml
    ```

## Tips
- Keep tests isolated (new browser context per test) to avoid flakiness.
- Use page.wait_for_selector / expect assertions to avoid timing issues.
- Capture screenshots or traces on failures:
    - page.screenshot(path="fail.png")
    - Use Playwright trace for debugging: start tracing in fixture, save trace on failure.
- Pin dependency versions in requirements.txt for reproducible runs.

If you want, I can:
- generate a starter requirements.txt,
- create a conftest.py tailored to your preferred API (sync/async),
- add example test files.