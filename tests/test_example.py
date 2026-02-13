def test_browser(driver):
    driver.get("https://example.com")
    assert "Example Domain" in driver.title