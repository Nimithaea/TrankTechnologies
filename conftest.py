import base64
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright
import pytest_html
from config import BASE_URL


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(request, browser):
    recordings_dir = Path("test-recordings").resolve()
    recordings_dir.mkdir(parents=True, exist_ok=True)

    context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir=str(recordings_dir),
    )
    page = context.new_page()

    try:
        page.goto(BASE_URL)
        page.wait_for_load_state("load")
        yield page
    finally:
        context.close()
        if page.video is not None:
            request.node._video_path = page.video.path()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "teardown":
        video_path = getattr(item, "_video_path", None)
        if video_path is not None:
            extra = getattr(report, "extras", [])
            extra.append(
                pytest_html.extras.video(
                    base64.b64encode(Path(video_path).read_bytes()).decode("ascii"),
                    name=f"Recording: {item.name}",
                    mime_type="video/webm",
                    extension="webm",
                )
            )
            report.extras = extra

    if report.when == "call":
        extra = getattr(report, "extras", [])
        test_module = Path(str(item.path))
        extra.append(
            pytest_html.extras.text(
                test_module.read_text(encoding="utf-8"),
                name=f"Test script: {test_module.name}",
            )
        )

        if report.failed:
            page = item.funcargs.get("page")

            if page:
                screenshots_dir = Path("screenshots")
                screenshots_dir.mkdir(exist_ok=True)

                file_name = screenshots_dir / f"{item.name}.png"

                page.screenshot(path=str(file_name))

                extra.append(pytest_html.extras.image(str(file_name)))

        report.extras = extra
